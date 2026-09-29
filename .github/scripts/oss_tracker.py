#!/usr/bin/env python3
"""Refresh oss/tracker.csv and oss/README.md from GitHub.

Usage: python3 .github/scripts/oss_tracker.py [--user NAME] [--dir oss]
Needs the gh CLI and GH_TOKEN. Only the `notes` column of the CSV is hand-edited; a refresh keeps it.
"""
import argparse
import csv
import datetime as dt
import json
import os
import re
import subprocess
import sys
import time

EXCLUDE_OWNERS = ["tradomate-tech", "Programming373", "thoughtbots", "Hash-Credit", "anvitra-ai", "apphireai"]
EXCLUDE_REPOS = ["blackbird71SR/Hello-World"]
PRACTICE_REPOS = {"Aniket965/Hello-world", "my-first-pr/hacktoberfest-2018", "rishabh-malik/Hacktoberfest-2018",
                  "firstcontributions/first-contributions"}
BOT_NAMES = {"codecov-commenter", "copilot", "cla-assistant", "github-advanced-security", "kubernetes-prow", "codspeed",
             "k8s-ci-robot", "mergify", "netlify", "vercel", "dependabot", "sonarcloud", "linux-foundation-easycla"}
COLUMNS = ["counts", "repo", "number", "title", "state", "waiting_on", "blockers", "ci", "failing_checks",
           "review_decision", "human_responders", "requested_reviewers", "last_human_activity", "age_days",
           "days_since_response", "created", "merged_at", "merged_by", "draft", "merge_state", "labels",
           "linked_issue", "url", "last_change", "last_change_date", "notes"]
WATCHED = ("state", "waiting_on", "review_decision")
RECENT_DAYS = 7

QUERY = """query($q:String!,$endCursor:String){search(type:ISSUE,query:$q,first:20,after:$endCursor){
pageInfo{hasNextPage endCursor} nodes{... on PullRequest{
number title url state isDraft createdAt updatedAt mergedAt closedAt mergedBy{login} headRefOid
mergeStateStatus reviewDecision body repository{nameWithOwner isPrivate}
labels(first:20){nodes{name}}
reviewRequests(first:8){nodes{requestedReviewer{... on User{login} ... on Team{name}}}}
reviews(first:30){nodes{author{login} state submittedAt}}
comments(first:40){nodes{author{login} createdAt}}
reviewThreads(first:30){nodes{comments(first:5){nodes{author{login} createdAt}}}}
closingIssuesReferences(first:3){nodes{number}}
commits(last:1){nodes{commit{committedDate statusCheckRollup{state}}}}
}}}}"""


def gh(*args):
    for attempt in range(4):
        out = subprocess.run(["gh", *args], capture_output=True, text=True)
        if out.returncode == 0:
            return out.stdout
        if not re.search(r"HTTP 5\d\d|timed? ?out|respond to your request", out.stderr) or attempt == 3:
            break
        time.sleep(3 * (attempt + 1))
    sys.exit(f"gh {' '.join(args[:3])} failed: {out.stderr.strip()[:300]}")


def is_bot(login):
    low = (login or "").lower()
    return not low or low.endswith("[bot]") or low in BOT_NAMES or "bot" in low


def parse(ts):
    return dt.datetime.fromisoformat(ts.replace("Z", "+00:00")) if ts else None


def fetch(user):
    scope = " ".join([f"-org:{o}" for o in EXCLUDE_OWNERS] + [f"-user:{user}"] + [f"-repo:{r}" for r in EXCLUDE_REPOS])
    raw = gh("api", "graphql", "--paginate", "--slurp", "-f", f"q=is:pr author:{user} is:public {scope}", "-f", f"query={QUERY}")
    return [n for page in json.loads(raw) for n in page["data"]["search"]["nodes"] if n and not n["repository"]["isPrivate"]]


def failing_checks(repo, sha):
    try:
        runs = json.loads(gh("api", f"repos/{repo}/commits/{sha}/check-runs?per_page=100"))["check_runs"]
    except SystemExit:
        return []
    bad = {"failure", "timed_out", "cancelled", "action_required"}
    return sorted({c["name"] if c["conclusion"] == "failure" else f'{c["name"]} ({c["conclusion"]})' for c in runs if c["conclusion"] in bad})


def row(n, user, now):
    repo = n["repository"]["nameWithOwner"]
    state = "merged" if n["mergedAt"] else n["state"].lower()
    events = [(r["author"], r["submittedAt"]) for r in n["reviews"]["nodes"]]
    events += [(c["author"], c["createdAt"]) for c in n["comments"]["nodes"]]
    events += [(c["author"], c["createdAt"]) for t in n["reviewThreads"]["nodes"] for c in t["comments"]["nodes"]]
    human = [(a["login"], ts) for a, ts in events if a and a["login"] != user and not is_bot(a["login"])]
    humans = sorted({login for login, _ in human})
    last_human = max((ts for _, ts in human), default="")
    commit = (n["commits"]["nodes"] or [{}])[0].get("commit") or {}
    rollup = (commit.get("statusCheckRollup") or {}).get("state")
    ci = {"SUCCESS": "pass", "FAILURE": "fail", "ERROR": "fail", "PENDING": "pending", "EXPECTED": "pending"}.get(rollup, "none")
    labels = [l["name"] for l in n["labels"]["nodes"]]
    decision = n["reviewDecision"] or ""
    failed = failing_checks(repo, n["headRefOid"]) if state == "open" and ci == "fail" else []
    only_rule = bool(failed) and all(f.startswith("Rule:") for f in failed)
    only_cancelled = bool(failed) and all(f.endswith("(cancelled)") for f in failed)
    if only_rule:
        ci = "pending"
    elif only_cancelled:
        ci = "cancelled"
    latest = {}
    for r in sorted(n["reviews"]["nodes"], key=lambda r: r["submittedAt"] or ""):
        who = (r["author"] or {}).get("login")
        if who and who != user and not is_bot(who):
            latest[who] = r["state"]
    dismissed = [who for who, st in latest.items() if st == "DISMISSED"]
    refs = re.findall(r"(?:closes|fixes|resolves|related to|related)\s+#(\d+)", n["body"] or "", re.I)
    linked = sorted({str(i["number"]) for i in n["closingIssuesReferences"]["nodes"]} | set(refs), key=int)
    blockers = []
    if any("linked accepted issue" in f.lower() for f in failed):
        blockers.append("linked issue not accepted")
    if "needs-ok-to-test" in labels:
        blockers.append("needs /ok-to-test from a member")
    if n["mergeStateStatus"] in ("BEHIND", "DIRTY"):
        blockers.append("behind base" if n["mergeStateStatus"] == "BEHIND" else "conflicts")
    if only_rule:
        blockers.append("merge-queue rule not yet satisfied")
    elif only_cancelled:
        blockers.append("run cancelled, needs a re-run")
    elif ci == "fail":
        blockers.append("CI failing")
    elif ci in ("none", "pending") and state == "open":
        blockers.append("CI not run or pending")
    if state != "open":
        waiting = "done"
    elif n["isDraft"]:
        waiting = "author (draft)"
    elif decision == "CHANGES_REQUESTED":
        cr = max((r["submittedAt"] for r in n["reviews"]["nodes"] if r["state"] == "CHANGES_REQUESTED"), default="")
        waiting = "re-review (fix pushed)" if (commit.get("committedDate") or "") > cr else "author fix"
    elif decision == "APPROVED":
        waiting = "merge (approved)"
    elif dismissed:
        waiting = "re-approval (" + ", ".join(dismissed) + " dismissed)"
    elif "linked issue not accepted" in blockers:
        waiting = "issue acceptance"
    elif "needs /ok-to-test from a member" in blockers:
        waiting = "/ok-to-test"
    elif only_cancelled:
        waiting = "CI re-run"
    elif ci == "fail":
        waiting = "CI fix"
    elif not humans:
        waiting = "first review"
    else:
        waiting = "reviewer follow-up"
    created = parse(n["createdAt"])
    since = parse(last_human) if last_human else created
    end = parse(n["mergedAt"] or n["closedAt"]) if state != "open" else now
    return {
        "counts": "no" if repo in PRACTICE_REPOS else "yes", "repo": repo, "number": n["number"], "title": n["title"],
        "state": state, "waiting_on": waiting, "blockers": "; ".join(blockers), "ci": ci if state == "open" else "",
        "failing_checks": "; ".join(failed), "review_decision": decision.lower(), "human_responders": ", ".join(humans),
        "requested_reviewers": ", ".join(filter(None, [(x["requestedReviewer"] or {}).get("login") or (x["requestedReviewer"] or {}).get("name")
                                                        for x in n["reviewRequests"]["nodes"]])),
        "last_human_activity": last_human[:10], "age_days": (end - created).days,
        "days_since_response": max(0, (now - since).days) if state == "open" else "", "created": n["createdAt"][:10],
        "merged_at": (n["mergedAt"] or "")[:10], "merged_by": (n["mergedBy"] or {}).get("login", ""),
        "draft": "yes" if n["isDraft"] else "", "merge_state": n["mergeStateStatus"].lower() if state == "open" else "",
        "labels": "; ".join(l for l in labels if l.startswith(("pr/", "needs-", "wg/", "accepted", "area/", "kind/"))),
        "linked_issue": ", ".join("#" + i for i in linked), "url": n["url"],
    }


def carry(rows, previous, today):
    """Keep notes, and remember what changed and when. A first run only knows recent merges and new PRs."""
    recent_from = (dt.date.fromisoformat(today) - dt.timedelta(days=RECENT_DAYS)).isoformat()
    for r in rows:
        old = previous.get(r["url"])
        r["notes"] = old["notes"] if old else ""
        r["last_change"], r["last_change_date"] = (old["last_change"], old["last_change_date"]) if old else ("", "")
        if old is None and previous:
            r["last_change"], r["last_change_date"] = "new PR", today
        elif old is None and r["merged_at"] >= recent_from:
            r["last_change"], r["last_change_date"] = "merged", r["merged_at"]
        elif old is None and r["created"] >= recent_from:
            r["last_change"], r["last_change_date"] = "opened", r["created"]
        elif old is not None:
            moved = [f"{k.replace('_', ' ')}: {old[k] or 'none'} → {r[k] or 'none'}" for k in WATCHED if old[k] != r[k]]
            if moved:
                r["last_change"], r["last_change_date"] = "; ".join(moved), today


def cell(text):
    return str(text).replace("|", "\\|").replace("\n", " ")


def link(r):
    return f"[{r['repo']}#{r['number']}]({r['url']})"


def render(rows, stamp, today):
    real = [r for r in rows if r["counts"] == "yes"]
    by = {s: [r for r in real if r["state"] == s] for s in ("open", "merged", "closed")}
    cutoff = (dt.date.fromisoformat(today) - dt.timedelta(days=RECENT_DAYS)).isoformat()
    recent = sorted((r for r in real if r["last_change_date"] >= cutoff and r["last_change"]), key=lambda r: r["last_change_date"], reverse=True)
    out = [
        "# Open-source contributions", "",
        f"Refreshed daily by `.github/workflows/oss-tracker.yml`, last run {stamp}. The data is in [tracker.csv](tracker.csv); "
        "this page is generated from it. Only the `notes` column of the CSV is edited by hand.", "",
        f"**{len(by['merged'])} merged, {len(by['open'])} open, {len(by['closed'])} closed without merging**, "
        f"across {len({r['repo'] for r in real})} projects. Pull requests to repositories I own or that belong to my employers are not listed.", "",
        f"## Changed in the last {RECENT_DAYS} days", "",
    ]
    out += [f"- {r['last_change_date']} {link(r)} {cell(r['title'])}: {cell(r['last_change'])}" for r in recent] or ["- nothing yet"]
    out += ["", f"## Open ({len(by['open'])})", "", "| PR | Waiting on | Blockers | CI | Days since a reply | Notes |", "|---|---|---|---|---|---|"]
    out += [f"| {link(r)} {cell(r['title'])} | {cell(r['waiting_on'])} | {cell(r['blockers'])} | {r['ci']} | {r['days_since_response']} | {cell(r['notes'])} |"
            for r in by["open"]]
    out += ["", f"## Merged ({len(by['merged'])})", "", "| PR | Merged | By |", "|---|---|---|"]
    out += [f"| {link(r)} {cell(r['title'])} | {r['merged_at']} | {r['merged_by']} |" for r in sorted(by["merged"], key=lambda r: r["merged_at"], reverse=True)]
    out += ["", f"## Closed without merging ({len(by['closed'])})", "", "| PR | Notes |", "|---|---|"]
    out += [f"| {link(r)} {cell(r['title'])} | {cell(r['notes'])} |" for r in by["closed"]]
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--user", default=os.environ.get("GITHUB_REPOSITORY_OWNER", "ankit373"))
    ap.add_argument("--dir", default="oss")
    args = ap.parse_args()
    now = dt.datetime.now(dt.timezone.utc)
    csv_path = os.path.join(args.dir, "tracker.csv")
    previous = {}
    if os.path.exists(csv_path):
        with open(csv_path, newline="", encoding="utf-8") as f:
            previous = {r["url"]: r for r in csv.DictReader(f)}
    rows = [row(n, args.user, now) for n in fetch(args.user)]
    rank = {"open": 0, "merged": 1, "closed": 2}
    rows.sort(key=lambda r: (rank[r["state"]], r["repo"], -int(r["number"])))
    carry(rows, previous, now.strftime("%Y-%m-%d"))
    os.makedirs(args.dir, exist_ok=True)
    with open(csv_path + ".tmp", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        w.writeheader()
        w.writerows(rows)
    os.replace(csv_path + ".tmp", csv_path)
    with open(os.path.join(args.dir, "README.md"), "w", encoding="utf-8") as f:
        f.write(render(rows, now.strftime("%Y-%m-%d %H:%M UTC"), now.strftime("%Y-%m-%d")))
    counts = {k: sum(1 for r in rows if r["state"] == k and r["counts"] == "yes") for k in rank}
    print(f"wrote {len(rows)} rows | counting: {counts}")


if __name__ == "__main__":
    main()
