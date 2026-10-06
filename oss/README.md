# Open-source contributions

Refreshed daily by `.github/workflows/oss-tracker.yml`, last run 2026-10-06 22:56 UTC. The data is in [tracker.csv](tracker.csv); this page is generated from it. Only the `notes` column of the CSV is edited by hand.

**21 merged, 35 open, 8 closed without merging**, across 17 projects. Pull requests to repositories I own or that belong to my employers are not listed.

## Changed in the last 7 days

- 2026-10-06 [BerriAI/litellm#44084](https://github.com/BerriAI/litellm/pull/44084) perf(router): read cooldown state only for the request's candidate deployments: review decision: none → review_required
- 2026-10-06 [BerriAI/litellm#44079](https://github.com/BerriAI/litellm/pull/44079) fix(anthropic): emit one tool_use block per call when a chunk carries several: review decision: none → review_required
- 2026-10-06 [BerriAI/litellm#40712](https://github.com/BerriAI/litellm/pull/40712) fix: record vertex_location on the generate_content path so cost uses the configured region: review decision: none → review_required
- 2026-10-06 [vllm-project/semantic-router#4577](https://github.com/vllm-project/semantic-router/pull/4577) [Feature] Add a locked uv environment for the PII LoRA scripts: waiting on: CI fix → merge (approved); review decision: review_required → approved
- 2026-10-06 [vllm-project/semantic-router#4533](https://github.com/vllm-project/semantic-router/pull/4533) [Feature] Add a locked uv environment for the intent classifier LoRA scripts: waiting on: first review → merge (approved); review decision: review_required → approved
- 2026-10-06 [vllm-project/semantic-router#4298](https://github.com/vllm-project/semantic-router/pull/4298) [Bug] Reject bodyless inference requests at the header stage: waiting on: re-approval (Bevisy, wilsonwu dismissed) → merge (approved); review decision: review_required → approved
- 2026-10-06 [vllm-project/semantic-router#4576](https://github.com/vllm-project/semantic-router/pull/4576) [Feature] Add a locked uv environment for the fact-check LoRA scripts: state: open → merged; waiting on: first review → done; review decision: review_required → approved
- 2026-10-06 [BerriAI/litellm#43729](https://github.com/BerriAI/litellm/pull/43729) test(interactions): follow Google's redesigned Interactions OpenAPI spec: review decision: none → review_required
- 2026-10-04 [helm/helm#32721](https://github.com/helm/helm/pull/32721) fix(list): honor AllNamespaces in action.List without mutating the config: new PR
- 2026-10-04 [helm/helm#32720](https://github.com/helm/helm/pull/32720) fix(schema): resolve relative $ref in values.schema.json from the chart's files: new PR
- 2026-10-04 [helm/helm#32719](https://github.com/helm/helm/pull/32719) fix(plugin): stop the git fsmonitor daemon before copying a cloned plugin: new PR
- 2026-10-04 [helm/helm-www#2272](https://github.com/helm/helm-www/pull/2272) docs(topics): describe relative $ref in values.schema.json: new PR
- 2026-10-03 [vllm-project/semantic-router#4483](https://github.com/vllm-project/semantic-router/pull/4483) [Feature] Report KMeans held-out results against the shared baselines: new PR
- 2026-10-03 [BerriAI/litellm#44160](https://github.com/BerriAI/litellm/pull/44160) feat(scaleway): add rerank support: state: open → merged; waiting on: reviewer follow-up → done; review decision: none → approved
- 2026-10-03 [vllm-project/semantic-router#4450](https://github.com/vllm-project/semantic-router/pull/4450) [Feature] Add a locked uv environment for the model_eval scripts: state: open → merged; waiting on: merge (approved) → done
- 2026-10-02 [vllm-project/semantic-router#4452](https://github.com/vllm-project/semantic-router/pull/4452) [Feature] Evaluate selectors on the held-out split against baselines and the oracle: new PR
- 2026-10-02 [vllm-project/semantic-router#4349](https://github.com/vllm-project/semantic-router/pull/4349) [Feature] Fit KMeans selectors on unique queries with a v2 artifact contract: waiting on: first review → merge (approved); review decision: review_required → approved
- 2026-10-02 [vllm-project/semantic-router#4022](https://github.com/vllm-project/semantic-router/pull/4022) [Feature] Define one versioned selector objective: waiting on: re-review (fix pushed) → merge (approved); review decision: changes_requested → approved
- 2026-10-01 [gravitational/teleport#69818](https://github.com/gravitational/teleport/pull/69818) Web: Load every role in the user roles dropdown: new PR
- 2026-10-01 [gravitational/teleport#69817](https://github.com/gravitational/teleport/pull/69817) Web: Do not repeat a label filter that is already applied: new PR
- 2026-10-01 [shridarpatil/whatomate#591](https://github.com/shridarpatil/whatomate/pull/591) feat(deploy): add a Helm chart: new PR
- 2026-10-01 [vllm-project/aibrix#2885](https://github.com/vllm-project/aibrix/pull/2885) [Bug] Drop pool policy activity records of pods that stopped reporting: new PR
- 2026-10-01 [vllm-project/aibrix#2884](https://github.com/vllm-project/aibrix/pull/2884) [Bug] Scale KPA on the total load, not the per-pod mean: new PR
- 2026-09-30 [actions/actions-runner-controller#4688](https://github.com/actions/actions-runner-controller/pull/4688) Release AutoscalingRunnerSet deletion when the GitHub config secret is gone: state: open → merged; waiting on: re-review (fix pushed) → done; review decision: changes_requested → approved
- 2026-09-30 [vllm-project/semantic-router#4324](https://github.com/vllm-project/semantic-router/pull/4324) [Bug] Budget context compression in the engine's own token unit: state: open → merged; waiting on: merge (approved) → done
- 2026-09-29 [vllm-project/semantic-router#4351](https://github.com/vllm-project/semantic-router/pull/4351) [Feature] Load KMeans v2 artifacts natively and pick the best eligible candidate: opened
- 2026-09-29 [BerriAI/litellm#43553](https://github.com/BerriAI/litellm/pull/43553) fix(otel): send cache and reasoning tokens in langfuse usage_details: merged
- 2026-09-29 [shridarpatil/whatomate#584](https://github.com/shridarpatil/whatomate/pull/584) perf(contacts): load unread counts for a contact page in one query: merged

## Open (35)

| PR | Waiting on | Blockers | CI | Days since a reply | Notes |
|---|---|---|---|---|---|
| [BerriAI/litellm#44084](https://github.com/BerriAI/litellm/pull/44084) perf(router): read cooldown state only for the request's candidate deployments | reviewer follow-up |  | pass | 4 |  |
| [BerriAI/litellm#44079](https://github.com/BerriAI/litellm/pull/44079) fix(anthropic): emit one tool_use block per call when a chunk carries several | reviewer follow-up |  | pass | 4 |  |
| [BerriAI/litellm#40712](https://github.com/BerriAI/litellm/pull/40712) fix: record vertex_location on the generate_content path so cost uses the configured region | CI fix | CI failing | fail | 5 | The red check comes from Google changing an API spec. The fix is BerriAI/litellm#43729. |
| [Tencent/WeKnora#3722](https://github.com/Tencent/WeKnora/pull/3722) fix(storage): use virtual-hosted addressing for Tencent COS through the S3 driver | first review |  | pass | 11 |  |
| [actions/actions-runner-controller#4594](https://github.com/actions/actions-runner-controller/pull/4594) fix: ignore duplicate workflow_job completed events for a job already scaled down | first review | CI not run or pending | none | 62 | Brought up to date with master and tested locally. CI needs a maintainer's approval to run. |
| [actions/actions-runner-controller#4593](https://github.com/actions/actions-runner-controller/pull/4593) fix: don't double-count webhook capacity reservations in PercentageRunnersBusy | first review | CI not run or pending | none | 63 | Brought up to date with master and tested locally. CI needs a maintainer's approval to run. |
| [element-hq/dendrite#3715](https://github.com/element-hq/dendrite/pull/3715) fix(docker): pass the TLS flags the compose file's own README requires | reviewer follow-up |  | pass | 18 |  |
| [element-hq/synapse#20282](https://github.com/element-hq/synapse/pull/20282) Fix federated media downloads failing when a multipart response is split across chunks | first review |  | pass | 8 | Also fixes a regression on the oldest supported python-multipart. |
| [grafana/loki#24781](https://github.com/grafana/loki/pull/24781) fix: Apply the configured log level to AWS SDK log output | first review |  | pass | 8 |  |
| [grafana/loki#24421](https://github.com/grafana/loki/pull/24421) fix: Anchor label filter regexes to the whole label value | reviewer follow-up |  | pass | 18 |  |
| [grafana/loki#23784](https://github.com/grafana/loki/pull/23784) fix: Give each tenant its own request in multi-tenant queries | first review |  | pass | 61 |  |
| [gravitational/teleport#69818](https://github.com/gravitational/teleport/pull/69818) Web: Load every role in the user roles dropdown | CI fix | CI failing | fail | 5 |  |
| [gravitational/teleport#69817](https://github.com/gravitational/teleport/pull/69817) Web: Do not repeat a label filter that is already applied | CI fix | CI failing | fail | 5 |  |
| [helm/helm#32721](https://github.com/helm/helm/pull/32721) fix(list): honor AllNamespaces in action.List without mutating the config | first review |  | pass | 2 |  |
| [helm/helm#32720](https://github.com/helm/helm/pull/32720) fix(schema): resolve relative $ref in values.schema.json from the chart's files | first review |  | pass | 2 |  |
| [helm/helm#32719](https://github.com/helm/helm/pull/32719) fix(plugin): stop the git fsmonitor daemon before copying a cloned plugin | first review |  | pass | 2 |  |
| [helm/helm-www#2272](https://github.com/helm/helm-www/pull/2272) docs(topics): describe relative $ref in values.schema.json | first review |  | pass | 2 |  |
| [kubernetes-sigs/karpenter#3308](https://github.com/kubernetes-sigs/karpenter/pull/3308) fix: attribute failed disruption validations to a NodePool and policy | first review | CI not run or pending | pending | 28 |  |
| [kubernetes/autoscaler#10269](https://github.com/kubernetes/autoscaler/pull/10269) fix: guard optional AcceleratorCount when building the AWS template node | /ok-to-test | needs /ok-to-test from a member; CI not run or pending | pending | 26 |  |
| [ollama/ollama#17548](https://github.com/ollama/ollama/pull/17548) server: return the upstream status from /api/embeddings | first review | CI not run or pending | none | 63 |  |
| [ollama/ollama#17542](https://github.com/ollama/ollama/pull/17542) llm: warn when a model is loaded entirely on CPU | reviewer follow-up | CI not run or pending | none | 64 |  |
| [shridarpatil/whatomate#591](https://github.com/shridarpatil/whatomate/pull/591) feat(deploy): add a Helm chart | author (draft) |  | pass | 5 |  |
| [shridarpatil/whatomate#578](https://github.com/shridarpatil/whatomate/pull/578) fix(contacts): use the bs_uid column when storing and looking up BSUID | first review | behind base | pass | 11 |  |
| [shridarpatil/whatomate#572](https://github.com/shridarpatil/whatomate/pull/572) fix(queue): recreate the consumer group when Redis loses it | first review | behind base; CI not run or pending | none | 13 |  |
| [vllm-project/semantic-router#4577](https://github.com/vllm-project/semantic-router/pull/4577) [Feature] Add a locked uv environment for the PII LoRA scripts | merge (approved) | behind base; CI not run or pending | pending | 0 |  |
| [vllm-project/semantic-router#4533](https://github.com/vllm-project/semantic-router/pull/4533) [Feature] Add a locked uv environment for the intent classifier LoRA scripts | merge (approved) | behind base | pass | 0 |  |
| [vllm-project/semantic-router#4483](https://github.com/vllm-project/semantic-router/pull/4483) [Feature] Report KMeans held-out results against the shared baselines | author (draft) | conflicts | pass | 3 |  |
| [vllm-project/semantic-router#4452](https://github.com/vllm-project/semantic-router/pull/4452) [Feature] Evaluate selectors on the held-out split against baselines and the oracle | author (draft) | behind base | pass | 4 |  |
| [vllm-project/semantic-router#4351](https://github.com/vllm-project/semantic-router/pull/4351) [Feature] Load KMeans v2 artifacts natively and pick the best eligible candidate | author (draft) | conflicts | pass | 7 | Slice 2 of 3 for #3665 (native loader). Draft, stacked on #4349. |
| [vllm-project/semantic-router#4349](https://github.com/vllm-project/semantic-router/pull/4349) [Feature] Fit KMeans selectors on unique queries with a v2 artifact contract | merge (approved) | conflicts; merge-queue rule not yet satisfied | pending | 4 | Slice 1 of 3 for #3665 (Python trainer). Stacked on #4022. |
| [vllm-project/semantic-router#4323](https://github.com/vllm-project/semantic-router/pull/4323) [Bug] Derive Anthropic content extension checks from the direction-aware variant allow-list | re-review (fix pushed) | behind base | pass | 7 | Related to #4319. Handling of toolset_name on responses is being discussed in review. |
| [vllm-project/semantic-router#4299](https://github.com/vllm-project/semantic-router/pull/4299) [Feature] Add extraContainers to the semantic-router Helm chart | issue acceptance | linked issue not accepted; conflicts; CI failing | fail | 8 | Blocked until the linked issue #3794 is accepted. |
| [vllm-project/semantic-router#4298](https://github.com/vllm-project/semantic-router/pull/4298) [Bug] Reject bodyless inference requests at the header stage | merge (approved) | behind base | pass | 0 | A test-only commit fixed a conflict with #4266 and reset the approvals. |
| [vllm-project/semantic-router#4022](https://github.com/vllm-project/semantic-router/pull/4022) [Feature] Define one versioned selector objective | merge (approved) | behind base | pass | 2 | Foundation for the KMeans work in #4349 and #4351. |
| [vllm-project/semantic-router#2767](https://github.com/vllm-project/semantic-router/pull/2767) [Config] Gate canonical input on a supported version | re-review (fix pushed) | conflicts | pass | 4 |  |

## Merged (21)

| PR | Merged | By |
|---|---|---|
| [vllm-project/semantic-router#4576](https://github.com/vllm-project/semantic-router/pull/4576) [Feature] Add a locked uv environment for the fact-check LoRA scripts | 2026-10-06 | mergify |
| [BerriAI/litellm#44160](https://github.com/BerriAI/litellm/pull/44160) feat(scaleway): add rerank support | 2026-10-03 | krrish-berri-2 |
| [vllm-project/semantic-router#4450](https://github.com/vllm-project/semantic-router/pull/4450) [Feature] Add a locked uv environment for the model_eval scripts | 2026-10-03 | Xunzhuo |
| [vllm-project/aibrix#2885](https://github.com/vllm-project/aibrix/pull/2885) [Bug] Drop pool policy activity records of pods that stopped reporting | 2026-10-01 | varungup90 |
| [vllm-project/aibrix#2884](https://github.com/vllm-project/aibrix/pull/2884) [Bug] Scale KPA on the total load, not the per-pod mean | 2026-10-01 | varungup90 |
| [actions/actions-runner-controller#4688](https://github.com/actions/actions-runner-controller/pull/4688) Release AutoscalingRunnerSet deletion when the GitHub config secret is gone | 2026-09-30 | nikola-jokic |
| [vllm-project/semantic-router#4324](https://github.com/vllm-project/semantic-router/pull/4324) [Bug] Budget context compression in the engine's own token unit | 2026-09-30 | mergify |
| [BerriAI/litellm#43553](https://github.com/BerriAI/litellm/pull/43553) fix(otel): send cache and reasoning tokens in langfuse usage_details | 2026-09-29 | krrish-berri-2 |
| [shridarpatil/whatomate#584](https://github.com/shridarpatil/whatomate/pull/584) perf(contacts): load unread counts for a contact page in one query | 2026-09-29 | shridarpatil |
| [element-hq/synapse#20274](https://github.com/element-hq/synapse/pull/20274) Fix 500 error when user-interactive auth requests send a null or non-object `auth` | 2026-09-28 | devonh |
| [element-hq/synapse#20241](https://github.com/element-hq/synapse/pull/20241) fix: reject user creation via the admin API when delegating to MAS | 2026-09-28 | anoadragon453 |
| [vllm-project/aibrix#2820](https://github.com/vllm-project/aibrix/pull/2820) [Bug] Chain each block of a multi-block BlockStored event from its predecessor | 2026-09-28 | varungup90 |
| [grafana/mcp-grafana#1249](https://github.com/grafana/mcp-grafana/pull/1249) fix(auth): ignore unsubstituted MCPB user_config placeholders in env | 2026-09-27 | sd2k |
| [vllm-project/semantic-router#4203](https://github.com/vllm-project/semantic-router/pull/4203) [Feature] Configure streamed_body through the SemanticRouter CRD | 2026-09-26 | Xunzhuo |
| [vllm-project/aibrix#2735](https://github.com/vllm-project/aibrix/pull/2735) [Bug] Purge a pod's prefix cache when the engine sleep-state metric shows it went to sleep | 2026-09-25 | varungup90 |
| [Tencent/WeKnora#3460](https://github.com/Tencent/WeKnora/pull/3460) fix(knowledge): stop synthesizing never-run stages as failed | 2026-09-22 | lyingbug |
| [vllm-project/semantic-router#3999](https://github.com/vllm-project/semantic-router/pull/3999) feat(training): add query-outcome snapshots and query-level splitting | 2026-09-21 | mergify |
| [Tencent/WeKnora#3433](https://github.com/Tencent/WeKnora/pull/3433) test(im): close the lifecycle test database and keep its name unique | 2026-09-20 | lyingbug |
| [vllm-project/semantic-router#2784](https://github.com/vllm-project/semantic-router/pull/2784) fix(cli): forward the api keys a config actually names | 2026-08-09 | mergify |
| [vllm-project/semantic-router#2776](https://github.com/vllm-project/semantic-router/pull/2776) test(config): unfence the apiserver doc needles so a table is not a failure | 2026-08-05 | mergify |
| [vllm-project/semantic-router#2769](https://github.com/vllm-project/semantic-router/pull/2769) config: honour enabled on the domain and PII classifiers | 2026-08-05 | mergify |

## Closed without merging (8)

| PR | Notes |
|---|---|
| [BerriAI/litellm#43729](https://github.com/BerriAI/litellm/pull/43729) test(interactions): follow Google's redesigned Interactions OpenAPI spec | Repairs a test that fails on many litellm PRs since Google changed its API spec. |
| [Tencent/WeKnora#3415](https://github.com/Tencent/WeKnora/pull/3415) test(im): give each lifecycle test its own sqlite database |  |
| [The-PR-Agent/pr-agent#3501](https://github.com/The-PR-Agent/pr-agent/pull/3501) feat(litellm): allow declaring adaptive-thinking models by id |  |
| [ollama/ollama#17543](https://github.com/ollama/ollama/pull/17543) server: warn when embedding input is truncated |  |
| [vllm-project/semantic-router#3847](https://github.com/vllm-project/semantic-router/pull/3847) [Bug] Run static global validators on Kubernetes startup, not just after CRD merge |  |
| [vllm-project/semantic-router#3814](https://github.com/vllm-project/semantic-router/pull/3814) [Bug] Let the config write API patch the ConfigMap directly on Kubernetes | Absorbed by a maintainer's PR (#4125). |
| [vllm-project/semantic-router#3632](https://github.com/vllm-project/semantic-router/pull/3632) [Bug] Update the catalog inventory assertion to the 20 added evaluations |  |
| [vllm-project/semantic-router#3617](https://github.com/vllm-project/semantic-router/pull/3617) [Security] Block SSRF in dashboard outbound fetches with one shared policy | Absorbed by a maintainer's PR (#4125). |
