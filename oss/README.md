# Open-source contributions

Refreshed daily by `.github/workflows/oss-tracker.yml`, last run 2026-11-14 00:14 UTC. The data is in [tracker.csv](tracker.csv); this page is generated from it. Only the `notes` column of the CSV is edited by hand.

**51 merged, 41 open, 17 closed without merging**, across 26 projects. Pull requests to repositories I own or that belong to my employers are not listed.

## Changed in the last 7 days

- 2026-11-14 [grafana/grafana#137670](https://github.com/grafana/grafana/pull/137670) Folders: Return 404 instead of 500 when a folder is not found: state: open → merged; waiting on: re-approval (pstibrany dismissed) → done; review decision: review_required → approved
- 2026-11-14 [grafana/mcp-grafana#1591](https://github.com/grafana/mcp-grafana/pull/1591) fix(alerting): page rules until label selectors fill rule_limit: new PR
- 2026-11-14 [grafana/pyroscope#6090](https://github.com/grafana/pyroscope/pull/6090) fix(store-gateway): close blocks that have been idle: state: open → closed; waiting on: first review → done
- 2026-11-12 [EleutherAI/lm-evaluation-harness#4584](https://github.com/EleutherAI/lm-evaluation-harness/pull/4584) make trust_remote_code=false block task-level remote code: new PR
- 2026-11-12 [grafana/grafana#137669](https://github.com/grafana/grafana/pull/137669) Auth: Let signed-out probes reach /livez and /readyz: new PR
- 2026-11-12 [grafana/grafana-cloudwatch-datasource#714](https://github.com/grafana/grafana-cloudwatch-datasource/pull/714) fix: bound the OAM monitoring-account lookup before Logs queries: new PR
- 2026-11-12 [grafana/loki#26414](https://github.com/grafana/loki/pull/26414) fix: Match non-ASCII case pairs in case-insensitive contains filters: new PR
- 2026-11-12 [grafana/mcp-grafana#1572](https://github.com/grafana/mcp-grafana/pull/1572) feat(loki): optional format=loki for loki's native query_range shape: new PR
- 2026-11-12 [grafana/pyroscope#6092](https://github.com/grafana/pyroscope/pull/6092) feat(vcs): add .NET source finder: new PR
- 2026-11-12 [pytorch/rl#4718](https://github.com/pytorch/rl/pull/4718) [Test] Fix flaky test_complex_replay_buffer_configuration: new PR
- 2026-11-12 [vllm-project/semantic-router#5281](https://github.com/vllm-project/semantic-router/pull/5281) [Feature] Skip shadow dispatch when the shadow model lacks a requested modality: waiting on: re-approval (wilsonwu dismissed) → merge (approved); review decision: review_required → approved
- 2026-11-12 [grafana/loki#26382](https://github.com/grafana/loki/pull/26382) fix(deps): Update hedgedhttp to v0.9.2 to stop leaking request contexts: state: open → merged; waiting on: reviewer follow-up → done; review decision: review_required → approved
- 2026-11-12 [grafana/mcp-grafana#1567](https://github.com/grafana/mcp-grafana/pull/1567) fix: send the docs index fetch and usage stats through the socks5 proxy: state: open → merged; waiting on: first review → done; review decision: review_required → approved
- 2026-11-12 [grafana/mcp-grafana#1566](https://github.com/grafana/mcp-grafana/pull/1566) fix: default --grafana-timeout to 30s: new PR
- 2026-11-12 [grafana/mcp-grafana#1563](https://github.com/grafana/mcp-grafana/pull/1563) fix(ds-query): use --grafana-timeout for datasource query tools: new PR
- 2026-11-12 [grafana/mcp-grafana#1552](https://github.com/grafana/mcp-grafana/pull/1552) fix(alerting): treat a missing alertmanager implementation as cortex: state: open → merged; waiting on: first review → done; review decision: review_required → approved
- 2026-11-12 [grafana/mcp-grafana#1540](https://github.com/grafana/mcp-grafana/pull/1540) fix(cloudwatch): keep series separate when a query returns several: state: open → merged; waiting on: author (draft) → done; review decision: review_required → approved
- 2026-11-12 [vllm-project/semantic-router#4203](https://github.com/vllm-project/semantic-router/pull/4203) [Feature] Configure streamed_body through the SemanticRouter CRD: review decision: review_required → none
- 2026-11-10 [NVIDIA-NeMo/Gym#5923](https://github.com/NVIDIA-NeMo/Gym/pull/5923) fix(judge): read the last verdict label in text_to_sql, labbench2_vlm and math_with_autograder: new PR
- 2026-11-10 [NVIDIA-NeMo/Gym#5919](https://github.com/NVIDIA-NeMo/Gym/pull/5919) fix(math_with_judge): verify only the final boxed answer: new PR
- 2026-11-10 [grafana/faro-javascript-bundler-plugins#704](https://github.com/grafana/faro-javascript-bundler-plugins/pull/704) fix(faro-cli): upload with fetch instead of curl: new PR
- 2026-11-10 [grafana/faro-web-sdk#2373](https://github.com/grafana/faro-web-sdk/pull/2373) feat(web-sdk): make frustration detection thresholds configurable: new PR
- 2026-11-10 [grafana/loki#26383](https://github.com/grafana/loki/pull/26383) fix(querier): Log cancelled queries at debug instead of error: new PR
- 2026-11-10 [grafana/loki#24781](https://github.com/grafana/loki/pull/24781) fix: Apply the configured log level to AWS SDK log output: waiting on: first review → reviewer follow-up
- 2026-11-10 [grafana/pyroscope#6077](https://github.com/grafana/pyroscope/pull/6077) feat(helm): validate architecture.storage values: new PR
- 2026-11-10 [grafana/pyroscope#6076](https://github.com/grafana/pyroscope/pull/6076) fix(vcs): resolve Kotlin files from Java mappings: new PR
- 2026-11-10 [open-thought/reasoning-gym#590](https://github.com/open-thought/reasoning-gym/pull/590) Keep bf difficulty 3 programs inside 8-bit cells: new PR
- 2026-11-10 [open-thought/reasoning-gym#589](https://github.com/open-thought/reasoning-gym/pull/589) Check puzzle24 answers use the item's numbers: new PR
- 2026-11-10 [open-thought/reasoning-gym#588](https://github.com/open-thought/reasoning-gym/pull/588) Fix game_of_life density config and trivial-answer reward: new PR
- 2026-11-10 [shridarpatil/whatomate#578](https://github.com/shridarpatil/whatomate/pull/578) fix(contacts): use the bs_uid column when storing and looking up BSUID: waiting on: CI fix → first review
- 2026-11-10 [vllm-project/semantic-router#4935](https://github.com/vllm-project/semantic-router/pull/4935) [Feature] Add the AMD AI PC CPU profile and recipe: waiting on: first review → reviewer follow-up
- 2026-11-10 [vllm-project/semantic-router#4299](https://github.com/vllm-project/semantic-router/pull/4299) [Feature] Add extraContainers to the semantic-router Helm chart: waiting on: issue acceptance → reviewer follow-up
- 2026-11-10 [element-hq/synapse#20282](https://github.com/element-hq/synapse/pull/20282) Fix federated media downloads failing when a multipart response is split across chunks: state: open → merged; waiting on: re-review (fix pushed) → done; review decision: changes_requested → approved
- 2026-11-10 [grafana/mcp-grafana#1554](https://github.com/grafana/mcp-grafana/pull/1554) fix(loki): default label tools to the last hour: new PR
- 2026-11-10 [grafana/mcp-grafana#1548](https://github.com/grafana/mcp-grafana/pull/1548) fix(incident): use basic auth when no service account token is set: new PR
- 2026-11-10 [grafana/mcp-grafana#1547](https://github.com/grafana/mcp-grafana/pull/1547) fix(oncall): return one page in proxy mode when page is omitted: new PR
- 2026-11-10 [grafana/mcp-grafana#1546](https://github.com/grafana/mcp-grafana/pull/1546) fix(rendering): convert RFC3339 time ranges in get_panel_image: new PR
- 2026-11-10 [grafana/mcp-grafana#1539](https://github.com/grafana/mcp-grafana/pull/1539) fix(elasticsearch): say unix timestamps are milliseconds: new PR
- 2026-11-10 [grafana/mcp-grafana#1538](https://github.com/grafana/mcp-grafana/pull/1538) fix(pyroscope): wrap bare matchers in the label list tools: new PR
- 2026-11-10 [grafana/mcp-grafana#1537](https://github.com/grafana/mcp-grafana/pull/1537) fix(run_panel_query): support Amazon and Azure Prometheus datasources: new PR
- 2026-11-10 [grafana/mcp-grafana#1536](https://github.com/grafana/mcp-grafana/pull/1536) fix(tempo): send a time range when listing attribute names and values: new PR
- 2026-11-10 [grafana/mcp-grafana#1530](https://github.com/grafana/mcp-grafana/pull/1530) fix(loki): return logs for instant queries on VictoriaLogs: new PR
- 2026-11-10 [grafana/mcp-grafana#1529](https://github.com/grafana/mcp-grafana/pull/1529) refactor(quickwit): reuse esTimestamp: new PR
- 2026-11-10 [grafana/mcp-grafana#1527](https://github.com/grafana/mcp-grafana/pull/1527) fix(run_panel_query): honour panel and datasource interval limits in $__interval: new PR
- 2026-11-10 [grafana/mcp-grafana#1525](https://github.com/grafana/mcp-grafana/pull/1525) fix(dashboard): reject variables saved without a value: new PR
- 2026-11-10 [grafana/mcp-grafana#1524](https://github.com/grafana/mcp-grafana/pull/1524) fix(run_panel_query): round $__interval and $__auto like Grafana: new PR
- 2026-11-10 [grafana/mcp-grafana#1522](https://github.com/grafana/mcp-grafana/pull/1522) fix(dashboard): keep macro-like variable values literal: new PR
- 2026-11-10 [BerriAI/litellm#40712](https://github.com/BerriAI/litellm/pull/40712) fix: record vertex_location on the generate_content path so cost uses the configured region: state: open → closed; waiting on: CI fix → done
- 2026-11-10 [vllm-project/semantic-router#5305](https://github.com/vllm-project/semantic-router/pull/5305) [Feature] Pin selector features in a content-addressed snapshot and stop stale embedding-cache reuse: state: open → closed; waiting on: CI fix → done
- 2026-11-10 [vllm-project/semantic-router#4483](https://github.com/vllm-project/semantic-router/pull/4483) [Feature] Report KMeans held-out results against the shared baselines: state: open → closed; waiting on: author (draft) → done
- 2026-11-10 [vllm-project/semantic-router#4452](https://github.com/vllm-project/semantic-router/pull/4452) [Feature] Evaluate selectors on the held-out split against baselines and the oracle: state: open → closed; waiting on: author (draft) → done
- 2026-11-10 [vllm-project/semantic-router#4351](https://github.com/vllm-project/semantic-router/pull/4351) [Feature] Load KMeans v2 artifacts natively and pick the best eligible candidate: state: open → closed; waiting on: author (draft) → done
- 2026-11-08 [vllm-project/semantic-router#4349](https://github.com/vllm-project/semantic-router/pull/4349) [Feature] Fit KMeans selectors on unique queries with a v2 artifact contract: state: open → closed; waiting on: merge (approved) → done

## Open (41)

| PR | Waiting on | Blockers | CI | Days since a reply | Notes |
|---|---|---|---|---|---|
| [BerriAI/litellm#44084](https://github.com/BerriAI/litellm/pull/44084) perf(router): read cooldown state only for the request's candidate deployments | reviewer follow-up |  | pass | 42 |  |
| [EleutherAI/lm-evaluation-harness#4584](https://github.com/EleutherAI/lm-evaluation-harness/pull/4584) make trust_remote_code=false block task-level remote code | reviewer follow-up |  | pass | 2 |  |
| [NVIDIA-NeMo/Gym#5923](https://github.com/NVIDIA-NeMo/Gym/pull/5923) fix(judge): read the last verdict label in text_to_sql, labbench2_vlm and math_with_autograder | first review |  | pass | 3 |  |
| [NVIDIA-NeMo/Gym#5919](https://github.com/NVIDIA-NeMo/Gym/pull/5919) fix(math_with_judge): verify only the final boxed answer | first review |  | pass | 3 |  |
| [actions/actions-runner-controller#4594](https://github.com/actions/actions-runner-controller/pull/4594) fix: ignore duplicate workflow_job completed events for a job already scaled down | first review | CI not run or pending | none | 100 | Brought up to date with master and tested locally. CI needs a maintainer's approval to run. |
| [actions/actions-runner-controller#4593](https://github.com/actions/actions-runner-controller/pull/4593) fix: don't double-count webhook capacity reservations in PercentageRunnersBusy | first review | CI not run or pending | none | 101 | Brought up to date with master and tested locally. CI needs a maintainer's approval to run. |
| [element-hq/dendrite#3715](https://github.com/element-hq/dendrite/pull/3715) fix(docker): pass the TLS flags the compose file's own README requires | reviewer follow-up |  | pass | 56 |  |
| [grafana/faro-javascript-bundler-plugins#704](https://github.com/grafana/faro-javascript-bundler-plugins/pull/704) fix(faro-cli): upload with fetch instead of curl | first review | conflicts | pass | 3 |  |
| [grafana/faro-web-sdk#2373](https://github.com/grafana/faro-web-sdk/pull/2373) feat(web-sdk): make frustration detection thresholds configurable | first review |  | pass | 3 |  |
| [grafana/grafana#137669](https://github.com/grafana/grafana/pull/137669) Auth: Let signed-out probes reach /livez and /readyz | first review | CI not run or pending | pending | 1 |  |
| [grafana/grafana-cloudwatch-datasource#714](https://github.com/grafana/grafana-cloudwatch-datasource/pull/714) fix: bound the OAM monitoring-account lookup before Logs queries | first review | behind base | pass | 1 |  |
| [grafana/loki#26414](https://github.com/grafana/loki/pull/26414) fix: Match non-ASCII case pairs in case-insensitive contains filters | first review |  | pass | 2 |  |
| [grafana/loki#26383](https://github.com/grafana/loki/pull/26383) fix(querier): Log cancelled queries at debug instead of error | first review |  | pass | 3 |  |
| [grafana/loki#24781](https://github.com/grafana/loki/pull/24781) fix: Apply the configured log level to AWS SDK log output | reviewer follow-up |  | pass | 3 |  |
| [grafana/loki#24421](https://github.com/grafana/loki/pull/24421) fix: Anchor label filter regexes to the whole label value | reviewer follow-up |  | pass | 56 |  |
| [grafana/loki#23784](https://github.com/grafana/loki/pull/23784) fix: Give each tenant its own request in multi-tenant queries | first review |  | pass | 99 |  |
| [grafana/mcp-grafana#1572](https://github.com/grafana/mcp-grafana/pull/1572) feat(loki): optional format=loki for loki's native query_range shape | reviewer follow-up |  | pass | 2 |  |
| [grafana/pyroscope#6092](https://github.com/grafana/pyroscope/pull/6092) feat(vcs): add .NET source finder | first review |  | pass | 2 |  |
| [grafana/pyroscope#6077](https://github.com/grafana/pyroscope/pull/6077) feat(helm): validate architecture.storage values | first review |  | pass | 3 |  |
| [grafana/pyroscope#6076](https://github.com/grafana/pyroscope/pull/6076) fix(vcs): resolve Kotlin files from Java mappings | first review |  | pass | 3 |  |
| [gravitational/teleport#69818](https://github.com/gravitational/teleport/pull/69818) Web: Load every role in the user roles dropdown | CI fix | CI failing | fail | 43 |  |
| [gravitational/teleport#69817](https://github.com/gravitational/teleport/pull/69817) Web: Do not repeat a label filter that is already applied | CI fix | CI failing | fail | 43 |  |
| [helm/helm#32721](https://github.com/helm/helm/pull/32721) fix(list): honor AllNamespaces in action.List without mutating the config | first review |  | pass | 40 |  |
| [helm/helm#32720](https://github.com/helm/helm/pull/32720) fix(schema): resolve relative $ref in values.schema.json from the chart's files | first review |  | pass | 40 |  |
| [helm/helm#32719](https://github.com/helm/helm/pull/32719) fix(plugin): stop the git fsmonitor daemon before copying a cloned plugin | first review |  | pass | 40 |  |
| [helm/helm-www#2272](https://github.com/helm/helm-www/pull/2272) docs(topics): describe relative $ref in values.schema.json | first review |  | pass | 40 |  |
| [kubernetes-sigs/karpenter#3308](https://github.com/kubernetes-sigs/karpenter/pull/3308) fix: attribute failed disruption validations to a NodePool and policy | first review | conflicts; CI not run or pending | pending | 66 |  |
| [kubernetes/autoscaler#10269](https://github.com/kubernetes/autoscaler/pull/10269) fix: guard optional AcceleratorCount when building the AWS template node | reviewer follow-up | CI not run or pending | pending | 36 |  |
| [ollama/ollama#17548](https://github.com/ollama/ollama/pull/17548) server: return the upstream status from /api/embeddings | first review | CI not run or pending | none | 101 |  |
| [ollama/ollama#17542](https://github.com/ollama/ollama/pull/17542) llm: warn when a model is loaded entirely on CPU | reviewer follow-up | CI not run or pending | none | 102 |  |
| [open-thought/reasoning-gym#590](https://github.com/open-thought/reasoning-gym/pull/590) Keep bf difficulty 3 programs inside 8-bit cells | first review | CI not run or pending | none | 3 |  |
| [open-thought/reasoning-gym#589](https://github.com/open-thought/reasoning-gym/pull/589) Check puzzle24 answers use the item's numbers | first review | CI not run or pending | none | 3 |  |
| [open-thought/reasoning-gym#588](https://github.com/open-thought/reasoning-gym/pull/588) Fix game_of_life density config and trivial-answer reward | first review | CI not run or pending | none | 3 |  |
| [pytorch/rl#4718](https://github.com/pytorch/rl/pull/4718) [Test] Fix flaky test_complex_replay_buffer_configuration | reviewer follow-up |  | pass | 2 |  |
| [shridarpatil/whatomate#578](https://github.com/shridarpatil/whatomate/pull/578) fix(contacts): use the bs_uid column when storing and looking up BSUID | first review | behind base | pass | 49 |  |
| [shridarpatil/whatomate#572](https://github.com/shridarpatil/whatomate/pull/572) fix(queue): recreate the consumer group when Redis loses it | first review | behind base | pass | 51 |  |
| [vllm-project/semantic-router#5281](https://github.com/vllm-project/semantic-router/pull/5281) [Feature] Skip shadow dispatch when the shadow model lacks a requested modality | merge (approved) |  | pass | 0 |  |
| [vllm-project/semantic-router#4935](https://github.com/vllm-project/semantic-router/pull/4935) [Feature] Add the AMD AI PC CPU profile and recipe | reviewer follow-up |  | pass | 3 |  |
| [vllm-project/semantic-router#4323](https://github.com/vllm-project/semantic-router/pull/4323) [Bug] Derive Anthropic content extension checks from the direction-aware variant allow-list | re-review (fix pushed) | CI not run or pending | pending | 3 | Related to #4319. Handling of toolset_name on responses is being discussed in review. |
| [vllm-project/semantic-router#4299](https://github.com/vllm-project/semantic-router/pull/4299) [Feature] Add extraContainers to the semantic-router Helm chart | reviewer follow-up | CI not run or pending | pending | 3 | Blocked until the linked issue #3794 is accepted. |
| [vllm-project/semantic-router#2767](https://github.com/vllm-project/semantic-router/pull/2767) [Config] Gate canonical input on a supported version | re-review (fix pushed) | CI not run or pending | pending | 1 |  |

## Merged (51)

| PR | Merged | By |
|---|---|---|
| [grafana/grafana#137670](https://github.com/grafana/grafana/pull/137670) Folders: Return 404 instead of 500 when a folder is not found | 2026-11-13 | pstibrany |
| [grafana/mcp-grafana#1591](https://github.com/grafana/mcp-grafana/pull/1591) fix(alerting): page rules until label selectors fill rule_limit | 2026-11-13 | sd2k |
| [grafana/loki#26382](https://github.com/grafana/loki/pull/26382) fix(deps): Update hedgedhttp to v0.9.2 to stop leaking request contexts | 2026-11-12 | chaudum |
| [grafana/mcp-grafana#1567](https://github.com/grafana/mcp-grafana/pull/1567) fix: send the docs index fetch and usage stats through the socks5 proxy | 2026-11-12 | sd2k |
| [grafana/mcp-grafana#1566](https://github.com/grafana/mcp-grafana/pull/1566) fix: default --grafana-timeout to 30s | 2026-11-11 | sd2k |
| [grafana/mcp-grafana#1563](https://github.com/grafana/mcp-grafana/pull/1563) fix(ds-query): use --grafana-timeout for datasource query tools | 2026-11-11 | sd2k |
| [grafana/mcp-grafana#1552](https://github.com/grafana/mcp-grafana/pull/1552) fix(alerting): treat a missing alertmanager implementation as cortex | 2026-11-11 | sd2k |
| [grafana/mcp-grafana#1540](https://github.com/grafana/mcp-grafana/pull/1540) fix(cloudwatch): keep series separate when a query returns several | 2026-11-11 | sd2k |
| [element-hq/synapse#20282](https://github.com/element-hq/synapse/pull/20282) Fix federated media downloads failing when a multipart response is split across chunks | 2026-11-10 | devonh |
| [grafana/mcp-grafana#1554](https://github.com/grafana/mcp-grafana/pull/1554) fix(loki): default label tools to the last hour | 2026-11-10 | sd2k |
| [grafana/mcp-grafana#1548](https://github.com/grafana/mcp-grafana/pull/1548) fix(incident): use basic auth when no service account token is set | 2026-11-10 | sd2k |
| [grafana/mcp-grafana#1547](https://github.com/grafana/mcp-grafana/pull/1547) fix(oncall): return one page in proxy mode when page is omitted | 2026-11-10 | sd2k |
| [grafana/mcp-grafana#1546](https://github.com/grafana/mcp-grafana/pull/1546) fix(rendering): convert RFC3339 time ranges in get_panel_image | 2026-11-10 | sd2k |
| [grafana/mcp-grafana#1539](https://github.com/grafana/mcp-grafana/pull/1539) fix(elasticsearch): say unix timestamps are milliseconds | 2026-11-10 | sd2k |
| [grafana/mcp-grafana#1538](https://github.com/grafana/mcp-grafana/pull/1538) fix(pyroscope): wrap bare matchers in the label list tools | 2026-11-10 | sd2k |
| [grafana/mcp-grafana#1537](https://github.com/grafana/mcp-grafana/pull/1537) fix(run_panel_query): support Amazon and Azure Prometheus datasources | 2026-11-10 | sd2k |
| [grafana/mcp-grafana#1536](https://github.com/grafana/mcp-grafana/pull/1536) fix(tempo): send a time range when listing attribute names and values | 2026-11-10 | sd2k |
| [grafana/mcp-grafana#1530](https://github.com/grafana/mcp-grafana/pull/1530) fix(loki): return logs for instant queries on VictoriaLogs | 2026-11-10 | sd2k |
| [grafana/mcp-grafana#1529](https://github.com/grafana/mcp-grafana/pull/1529) refactor(quickwit): reuse esTimestamp | 2026-11-10 | sd2k |
| [grafana/mcp-grafana#1527](https://github.com/grafana/mcp-grafana/pull/1527) fix(run_panel_query): honour panel and datasource interval limits in $__interval | 2026-11-10 | sd2k |
| [grafana/mcp-grafana#1525](https://github.com/grafana/mcp-grafana/pull/1525) fix(dashboard): reject variables saved without a value | 2026-11-10 | sd2k |
| [grafana/mcp-grafana#1524](https://github.com/grafana/mcp-grafana/pull/1524) fix(run_panel_query): round $__interval and $__auto like Grafana | 2026-11-10 | sd2k |
| [grafana/mcp-grafana#1522](https://github.com/grafana/mcp-grafana/pull/1522) fix(dashboard): keep macro-like variable values literal | 2026-11-10 | sd2k |
| [vllm-project/semantic-router#4022](https://github.com/vllm-project/semantic-router/pull/4022) [Feature] Define one versioned selector objective | 2026-10-31 | mergify |
| [vllm-project/semantic-router#4938](https://github.com/vllm-project/semantic-router/pull/4938) [Feature] Gate RAG and memory retrieval on request and backend capabilities | 2026-10-16 | mergify |
| [shridarpatil/whatomate#598](https://github.com/shridarpatil/whatomate/pull/598) docs: link the community Helm chart from the quickstart | 2026-10-14 | shridarpatil |
| [vllm-project/semantic-router#4298](https://github.com/vllm-project/semantic-router/pull/4298) [Bug] Reject bodyless inference requests at the header stage | 2026-10-09 | mergify |
| [Tencent/WeKnora#3722](https://github.com/Tencent/WeKnora/pull/3722) fix(storage): use virtual-hosted addressing for Tencent COS through the S3 driver | 2026-10-07 | lyingbug |
| [vllm-project/semantic-router#4533](https://github.com/vllm-project/semantic-router/pull/4533) [Feature] Add a locked uv environment for the intent classifier LoRA scripts | 2026-10-07 | mergify |
| [vllm-project/semantic-router#4577](https://github.com/vllm-project/semantic-router/pull/4577) [Feature] Add a locked uv environment for the PII LoRA scripts | 2026-10-06 | mergify |
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

## Closed without merging (17)

| PR | Notes |
|---|---|
| [BerriAI/litellm#44079](https://github.com/BerriAI/litellm/pull/44079) fix(anthropic): emit one tool_use block per call when a chunk carries several |  |
| [BerriAI/litellm#43729](https://github.com/BerriAI/litellm/pull/43729) test(interactions): follow Google's redesigned Interactions OpenAPI spec | Repairs a test that fails on many litellm PRs since Google changed its API spec. |
| [BerriAI/litellm#40712](https://github.com/BerriAI/litellm/pull/40712) fix: record vertex_location on the generate_content path so cost uses the configured region | The red check comes from Google changing an API spec. The fix is BerriAI/litellm#43729. |
| [Tencent/WeKnora#3415](https://github.com/Tencent/WeKnora/pull/3415) test(im): give each lifecycle test its own sqlite database |  |
| [The-PR-Agent/pr-agent#3501](https://github.com/The-PR-Agent/pr-agent/pull/3501) feat(litellm): allow declaring adaptive-thinking models by id |  |
| [grafana/pyroscope#6090](https://github.com/grafana/pyroscope/pull/6090) fix(store-gateway): close blocks that have been idle |  |
| [ollama/ollama#17543](https://github.com/ollama/ollama/pull/17543) server: warn when embedding input is truncated |  |
| [shridarpatil/whatomate#591](https://github.com/shridarpatil/whatomate/pull/591) feat(deploy): add a Helm chart |  |
| [vllm-project/semantic-router#5305](https://github.com/vllm-project/semantic-router/pull/5305) [Feature] Pin selector features in a content-addressed snapshot and stop stale embedding-cache reuse |  |
| [vllm-project/semantic-router#4483](https://github.com/vllm-project/semantic-router/pull/4483) [Feature] Report KMeans held-out results against the shared baselines |  |
| [vllm-project/semantic-router#4452](https://github.com/vllm-project/semantic-router/pull/4452) [Feature] Evaluate selectors on the held-out split against baselines and the oracle |  |
| [vllm-project/semantic-router#4351](https://github.com/vllm-project/semantic-router/pull/4351) [Feature] Load KMeans v2 artifacts natively and pick the best eligible candidate | Slice 2 of 3 for #3665 (native loader). Draft, stacked on #4349. |
| [vllm-project/semantic-router#4349](https://github.com/vllm-project/semantic-router/pull/4349) [Feature] Fit KMeans selectors on unique queries with a v2 artifact contract | Slice 1 of 3 for #3665 (Python trainer). Stacked on #4022. |
| [vllm-project/semantic-router#3847](https://github.com/vllm-project/semantic-router/pull/3847) [Bug] Run static global validators on Kubernetes startup, not just after CRD merge |  |
| [vllm-project/semantic-router#3814](https://github.com/vllm-project/semantic-router/pull/3814) [Bug] Let the config write API patch the ConfigMap directly on Kubernetes | Absorbed by a maintainer's PR (#4125). |
| [vllm-project/semantic-router#3632](https://github.com/vllm-project/semantic-router/pull/3632) [Bug] Update the catalog inventory assertion to the 20 added evaluations |  |
| [vllm-project/semantic-router#3617](https://github.com/vllm-project/semantic-router/pull/3617) [Security] Block SSRF in dashboard outbound fetches with one shared policy | Absorbed by a maintainer's PR (#4125). |
