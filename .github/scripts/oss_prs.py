"""Rewrite the README's oss block with merged PRs to open-source repos the user does not own."""
import datetime, json, os, re, sys, urllib.request
from zoneinfo import ZoneInfo

# OSI-approved SPDX ids GitHub detects; anything else (NOASSERTION, OTHER, CC-BY, BSL, SSPL) is left out.
OSI = {
    "0BSD", "AFL-3.0", "AGPL-3.0", "Apache-2.0", "Artistic-2.0", "BSD-2-Clause", "BSD-3-Clause",
    "BSD-3-Clause-Clear", "BSL-1.0", "ECL-2.0", "EPL-1.0", "EPL-2.0", "EUPL-1.1", "EUPL-1.2",
    "GPL-2.0", "GPL-3.0", "ISC", "LGPL-2.1", "LGPL-3.0", "LPPL-1.3c", "MIT", "MIT-0", "MPL-2.0",
    "MS-PL", "MS-RL", "MulanPSL-2.0", "NCSA", "OFL-1.1", "OSL-3.0", "PostgreSQL", "UPL-1.0",
    "Unlicense", "Zlib",
}

QUERY = """query($q: String!, $after: String) {
  search(type: ISSUE, query: $q, first: 100, after: $after) {
    pageInfo { hasNextPage endCursor }
    nodes { ... on PullRequest {
      title url mergedAt
      repository { nameWithOwner url isPrivate isFork stargazerCount owner { login } licenseInfo { spdxId } }
    } }
  }
}"""


def graphql(q, after=None):
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"q": q, "after": after}}).encode(),
        headers={"Authorization": f"bearer {os.environ['GITHUB_TOKEN']}", "Content-Type": "application/json"},
    )
    body = json.load(urllib.request.urlopen(req, timeout=30))
    if "errors" in body:
        sys.exit(f"graphql: {body['errors']}")
    return body["data"]["search"]


def merged_prs(cfg):
    q = f"is:pr is:merged is:public author:{cfg['user']} " + " ".join(f"-user:{o}" for o in cfg["exclude_owners"])
    after, prs = None, []
    while True:
        page = graphql(q, after)
        prs += [n for n in page["nodes"] if n]
        if not page["pageInfo"]["hasNextPage"]:
            return prs
        after = page["pageInfo"]["endCursor"]


def license_of(repo, cfg):
    # An override is for a license file GitHub reads as NOASSERTION but a human has checked.
    return cfg["license_overrides"].get(repo["nameWithOwner"]) or (repo["licenseInfo"] or {}).get("spdxId")


def keep(pr, cfg):
    r = pr["repository"]
    return (not r["isPrivate"] and not r["isFork"]
            and r["owner"]["login"].lower() not in {o.lower() for o in cfg["exclude_owners"]}
            and r["nameWithOwner"] not in cfg["exclude_repos"]
            and license_of(r, cfg) in OSI)


def esc(s):
    return s.replace("[", "\\[").replace("]", "\\]").replace("|", "\\|").replace("<", "&lt;").replace(">", "&gt;")


def render(prs, cfg):
    repos = {}
    for pr in prs:
        repos.setdefault(pr["repository"]["nameWithOwner"], []).append(pr)
    order = sorted(repos.values(), key=lambda p: (-len(p), -p[0]["repository"]["stargazerCount"]))
    n = cfg["max_prs_per_repo"]
    today = datetime.datetime.now(ZoneInfo("Asia/Kolkata")).strftime("%Y-%m-%d")
    lines = [
        f"**{len(prs)}** merged PRs across **{len(repos)}** open-source projects I don't own"
        f" · <sub>refreshed daily by an Action, last {today}</sub>",
        "",
        "| project | license | merged | latest |",
        "|:--|:--|--:|:--|",
    ]
    for group in order:
        r = group[0]["repository"]
        group.sort(key=lambda p: p["mergedAt"], reverse=True)
        latest = "<br>".join(f"[{esc(p['title'])}]({p['url']})" for p in group[:n])
        if len(group) > n:
            latest += f"<br><sub>+{len(group) - n} more</sub>"
        stars = f"<br><sub>★ {r['stargazerCount']:,}</sub>"
        lines.append(f"| [{r['nameWithOwner']}]({r['url']}){stars} | `{license_of(r, cfg)}` | {len(group)} | {latest} |")
    return "\n".join(lines)


def main():
    cfg = json.load(open(".github/oss.json"))
    prs = [p for p in merged_prs(cfg) if keep(p, cfg)]
    readme = open("README.md").read()
    block = render(prs, cfg)
    new, count = re.subn(r"(<!-- oss:start -->).*?(<!-- oss:end -->)",
                         lambda m: f"{m.group(1)}\n{block}\n{m.group(2)}", readme, flags=re.S)
    if count != 1:
        sys.exit("README needs exactly one <!-- oss:start --> ... <!-- oss:end --> block")
    open("README.md", "w").write(new)
    print(f"{len(prs)} PRs, {len(set(p['repository']['nameWithOwner'] for p in prs))} repos")


if __name__ == "__main__":
    main()
