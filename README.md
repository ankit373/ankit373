<h1 align="center">Ankit Jha</h1>

<p align="center">
  <b>I build and run the control planes underneath things</b> — Kubernetes platforms on AWS &amp; GCP, and now AI model routing.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Lead_DevOps-Tradomate-0A66C2?style=flat-square" alt="Lead DevOps at Tradomate">
  <img src="https://img.shields.io/badge/Bengaluru,_India-1a1a1a?style=flat-square" alt="Bengaluru, India">
  <img src="https://img.shields.io/badge/6%2B_years-platform_%26_cloud-00ADD8?style=flat-square" alt="6+ years platform and cloud">
  <img src="https://img.shields.io/github/followers/ankit373?style=flat-square&label=followers&color=555" alt="GitHub followers">
  <img src="https://komarev.com/ghpvc/?username=ankit373&style=flat-square&label=profile+views&color=555" alt="Profile views">
</p>

---

I'm a platform and cloud architect who came up through electronics and never stopped caring about what's actually happening under the abstraction. Six years across fintech, healthcare and AI: I design the Kubernetes platforms, cut the cloud bills, wire up the observability, and write the Go and Python that holds it together. Lately I've been building **[Hydra](https://github.com/ankit373/hydra)** — a control plane that routes prompts across every model on your machine by capability, cost and confidence of correctness.

### By the numbers

| | |
|---|---|
| **Cloud cost reduced** | **40%** at Tradomate (AWS) · **35%** on an enterprise LLM product · **27%** at Wipro |
| **Experience** | 6+ years · 5 roles · 4 companies · led a team of 5 |
| **On GitHub since** | May 2015 · 27 repositories of my own |
| **Shipped in 2026** | 296 pull requests · 283 issues · 1,377 contributions |
| **Certified** | GCP Associate Cloud Engineer · HashiCorp Terraform Associate |

### Where I've worked

| | Role | Company | What I was there to do |
|---|---|---|---|
| **2025 →** | Lead DevOps, Innovation Unit | **Tradomate** | Own platform &amp; cloud architecture for a fintech trading platform. Cut AWS spend 40%, built the observability stack, run EKS across two regions. |
| 2024 – 2025 | Platform Engineer | **Tiger Analytics** | Built the GCP practice from scratch — hired and mentored the engineers, set the standards, drove adoption org-wide. |
| 2022 – 2024 | Senior Platform Engineer | **Quantiphi** | Led 5 engineers building a cloud-agnostic Contact Center AI platform. SOC 2 and HIPAA readiness, 35% cost cut on an LLM product. |
| 2021 – 2022 | Platform Engineer, R&amp;D (QIH) | **Quantiphi** | NLP-powered search app on GKE via Terraform. GitLab CI + SonarQube pipelines, AWS chaos engineering. |
| 2019 – 2021 | Cloud Engineer | **Wipro** | Day-two GCP operations and incident handling. 27% monthly cost reduction, Cloud Armor WAF, a PITR recovery I still tell people about. |

### What I'm building

**[Hydra](https://github.com/ankit373/hydra)** &nbsp;·&nbsp; Go &nbsp;·&nbsp; ![stars](https://img.shields.io/github/stars/ankit373/hydra?style=flat-square&label=%E2%98%85&color=555) ![license](https://img.shields.io/github/license/ankit373/hydra?style=flat-square&color=555)
> One CLI for every model on your machine. Discovers 13+ tools and 14 API providers in under 2 seconds, then routes by capability, cost and a sequential-probability-ratio test for confidence — not just whichever model is cheapest. Blocks PII at the dispatch layer. ~1.1µs routing overhead, 75–85% cheaper than going all-frontier on typical coding workloads.
> ```bash
> brew install ankit373/hydra/hyctl
> ```

**[Mainspring](https://github.com/ankit373/mainspring)** &nbsp;·&nbsp; Go
> Backend-agnostic local inference server. One OpenAI-compatible API, pluggable engines (llama.cpp, MLX, Ollama). Build the control plane, not the kernels.

**[Vyuha](https://github.com/ankit373/vyuha)** &nbsp;·&nbsp; Python
> Multi-agent orchestration engine for high-stakes software development.

### Upstream

I send patches to the infrastructure I run in production, which is the only way I know to actually learn it:

[**grafana/loki**](https://github.com/grafana/loki) — cross-tenant leakage and a marshal panic on multi-tenant queries &nbsp;·&nbsp; [**ollama/ollama**](https://github.com/ollama/ollama) — upstream status propagation, CPU-fallback and truncation warnings &nbsp;·&nbsp; [**vllm-project/semantic-router**](https://github.com/vllm-project/semantic-router) — config correctness for PII/domain classifiers and API-key forwarding &nbsp;·&nbsp; [**actions/actions-runner-controller**](https://github.com/actions/actions-runner-controller) — duplicate `workflow_job` events and webhook capacity double-counting

### Stack

**Languages** &nbsp;
![Go](https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white)

**Platform** &nbsp;
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat-square)
![GCP](https://img.shields.io/badge/GCP-4285F4?style=flat-square&logo=googlecloud&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=flat-square&logo=terraform&logoColor=white)
![Helm](https://img.shields.io/badge/Helm-0F1689?style=flat-square&logo=helm&logoColor=white)
![Karpenter](https://img.shields.io/badge/Karpenter-FF9900?style=flat-square&logoColor=white)
![Cloudflare](https://img.shields.io/badge/Cloudflare-F38020?style=flat-square&logo=cloudflare&logoColor=white)

**Observability** &nbsp;
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=flat-square&logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=flat-square&logo=grafana&logoColor=white)
![Loki](https://img.shields.io/badge/Loki-F5A800?style=flat-square&logo=grafana&logoColor=white)
![Tempo](https://img.shields.io/badge/Tempo-F46800?style=flat-square&logo=grafana&logoColor=white)

**Data** &nbsp;
![ClickHouse](https://img.shields.io/badge/ClickHouse-FFCC01?style=flat-square&logo=clickhouse&logoColor=black)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white)

<details>
<summary><b>Things I've done that don't fit in a bullet list</b></summary>

<br>

**Built a GCP practice from nothing.** At Tiger Analytics I was hired to stand up cloud practice as a discipline — I did the hiring, wrote the standards, built a Terraform accelerator and reusable module library, and drove adoption across teams. The hardest part was never the infrastructure.

**Migrated transactional email off SendGrid onto Amazon SES**, then built a DMARC-based monitoring system on top of it that ingests and parses aggregate reports so spoofing shows up on a dashboard instead of in a support ticket.

**Tuned ClickHouse down to millisecond query latency** for high-frequency analytical workloads — schema design, indexing, query rewriting. Did the same kind of work on MongoDB with workload-driven indexing.

**Ran a point-in-time recovery on a large truncated CloudSQL database**, wrote the RCA, and implemented the safeguards so it couldn't happen again. Early-career, high-stakes, extremely educational.

**Chaos engineering on AWS** to prove resilience claims rather than assert them, plus SOC 2 controls and disaster-recovery drills.

</details>

<details>
<summary><b>Where I started: brain-computer interfaces and fuzzy logic</b></summary>

<br>

I did my B.Tech in **Electronics &amp; Communication at BVM, Anand**, and my early projects were all hardware:

- **[BCI Wheelchair](https://github.com/ankit373/BCI-wheelchair)** — a wheelchair steered by brain waves.
- **[BCI Home Automation](https://github.com/ankit373/BCI-Home-Automation)** — controlling home appliances through EEG detection and analysis.
- **[Greenhouse Climate Controller](https://github.com/ankit373/Greenhouse_Climate_Controller)** — fuzzy-logic algorithms driving actuators for variable output.

Then a stretch of teaching myself data science in the open — [algorithms and data structures](https://github.com/ankit373/DS-A), [data analysis](https://github.com/ankit373/Data-Analysis-Tutorlals), [computational thinking](https://github.com/ankit373/Computational-Thinking-and-Data-Science-Tutorials) — before moving into cloud and platform work in 2019.

**Along the way:** finalist at Idea Chaupal '18 (national pitching competition, IRMA Anand) · distinguished participant in Smart India Hackathon 2018 for both hardware and software · organizer for Gujarat SIH · featured in Quantiphi's *Inspire* newsletter as "Brilliance Personified" · Group of Talent and Avenger awards for H2 2023.

</details>

---

<p align="center">
  <a href="https://linkedin.com/in/ankit-jha"><img src="https://img.shields.io/badge/LinkedIn-let's_talk-0A66C2?style=for-the-badge&logo=data:image/svg%2Bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0yMC40NDcgMjAuNDUyaC0zLjU1NHYtNS41NjljMC0xLjMyOC0uMDI3LTMuMDM3LTEuODUyLTMuMDM3LTEuODUzIDAtMi4xMzYgMS40NDUtMi4xMzYgMi45Mzl2NS42NjdIOS4zNTFWOWgzLjQxNHYxLjU2MWguMDQ2Yy40NzctLjkgMS42MzctMS44NSAzLjM3LTEuODUgMy42MDEgMCA0LjI2NyAyLjM3IDQuMjY3IDUuNDU1djYuMjg2ek01LjMzNyA3LjQzM2MtMS4xNDQgMC0yLjA2My0uOTI2LTIuMDYzLTIuMDY1IDAtMS4xMzguOTItMi4wNjMgMi4wNjMtMi4wNjMgMS4xNCAwIDIuMDY0LjkyNSAyLjA2NCAyLjA2MyAwIDEuMTM5LS45MjUgMi4wNjUtMi4wNjQgMi4wNjV6bTEuNzgyIDEzLjAxOUgzLjU1NVY5aDMuNTY0djExLjQ1MnpNMjIuMjI1IDBIMS43NzFDLjc5MiAwIDAgLjc3NCAwIDEuNzI5djIwLjU0MkMwIDIzLjIyNy43OTIgMjQgMS43NzEgMjRoMjAuNDUxQzIzLjIgMjQgMjQgMjMuMjI3IDI0IDIyLjI3MVYxLjcyOUMyNCAuNzc0IDIzLjIgMCAyMi4yMjIgMGguMDAzeiIvPjwvc3ZnPgo=" alt="LinkedIn"></a>
</p>

<p align="center">
  <sub>Currently: making AI model routing boring and predictable, the same way we did it for servers.</sub>
</p>
