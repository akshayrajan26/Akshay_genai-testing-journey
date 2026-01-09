# 🚀 GenAI Testing Journey: 52 Weeks to AI Test Developer/Architect

<div align="center">

![Week](https://img.shields.io/badge/Current_Week-1%2F52-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-In_Progress-green?style=for-the-badge)
![Followers](https://img.shields.io/badge/Community-Growing-orange?style=for-the-badge)

**A structured 52-week journey from QA/SDET to GenAI Test Framework Developer**

*Learning in public. Building in public. Growing together.*

[📚 Full Roadmap](#-the-52-week-roadmap) • [🎯 Weekly Progress](#-weekly-progress-tracker) • [🤝 Join the Journey](#-join-the-community) • [📖 Resources](#-resources)

</div>

---

## 🎯 What This Is

After 10 years as a Lead SDET, I asked myself: **"How do you test non-deterministic systems?"**

This repository documents my 52-week journey to answer that question — learning GenAI testing in public, building real projects, and sharing everything along the way.

### Why QA Engineers Are Uniquely Positioned for AI Testing

```
Traditional QA Mindset          →    AI Testing Application
─────────────────────────────────────────────────────────────
Think in edge cases             →    Adversarial prompt testing
Break things systematically     →    Red teaming LLMs
"It works on my machine" ≠ OK   →    Non-deterministic output validation
Build automation frameworks     →    LLM evaluation pipelines
Test for regression             →    Prompt drift detection
Validate against requirements   →    Evaluate against metrics
```

---

## 📊 The 52-Week Roadmap

<details>
<summary><b>🔵 Phase 0: Foundation (Weeks 1-8)</b> — Python & Data Handling for AI Testing</summary>

| Week | Focus | Mini-Project | Skills |
|------|-------|--------------|--------|
| 1 | Python Basics | `prompt-formatter` — String manipulation for prompts | Variables, strings, f-strings |
| 2 | Data Structures | `test-case-manager` — Manage test cases with lists/dicts | Lists, dicts, sets, tuples |
| 3 | Functions & Control Flow | `llm-response-validator` — Validate outputs | Functions, loops, error handling |
| 4 | Modules & Packages | `llm-test-utils` — First reusable package | Modules, pip, virtualenv |
| 5 | File Handling & JSON | `dataset-loader` — Load JSONL datasets | JSON, file I/O, validation |
| 6 | Error Handling & Logs | `robust-api-caller` — Resilient API wrapper | try/except, logging, retries |
| 7 | pytest Fundamentals | `test-suite-basics` — Testing your package | pytest basics, assertions |
| 8 | pytest Advanced | `parametrized-test-suite` — Data-driven tests | Fixtures, parametrization |

**Phase Outcome:** Python proficiency for LLM testing, first GitHub projects published.
</details>

<details>
<summary><b>🟣 Phase 1: LLM Fundamentals (Weeks 9-18)</b> — Understanding What You're Testing</summary>

| Week | Focus | Mini-Project | Skills |
|------|-------|--------------|--------|
| 9 | How LLMs Work | `llm-concepts-notebook` — Visualizing concepts | Tokens, temperature, sampling |
| 10 | Transformers | `attention-explainer` — Attention visualization | Attention mechanism, context |
| 11 | Tokenization | `tokenizer-explorer` — Tokenizer deep dive | BPE, tiktoken, limits |
| 12 | OpenAI API | `openai-test-client` — API wrapper | API auth, chat completions |
| 13 | Claude API (Multi-Model) | `multi-provider-client` — Unified interface | Anthropic API, abstraction |
| 14 | Prompt Engineering | `prompt-tester` — Prompt experiments | CoT, few-shot, system prompts |
| 15 | Failure Modes 1 | `hallucination-examples` — Hallucination catalog | Hallucination types |
| 16 | Failure Modes 2 | `consistency-tester` — Inconsistency tests | Non-determinism, drift |
| 17 | Failure Modes 3 | `edge-case-generator` — Edge case suite | Boundary testing, inputs |
| 18 | LangChain Basics | `simple-chain-tester` — Chain testing | Chains, PromptTemplates |

**Phase Outcome:** Understand LLM internals, can interact with APIs, documented failure taxonomy.
</details>

<details>
<summary><b>🟢 Phase 2: Evaluation Core (Weeks 19-28)</b> — Measuring AI Quality</summary>

| Week | Focus | Mini-Project | Skills |
|------|-------|--------------|--------|
| 19 | Eval Philosophy | `evaluation-framework-design` — Rubric design | Evaluation dimensions |
| 20 | Classic Metrics | `classic-metrics` — NLP metrics | F1, BLEU, ROUGE |
| 21 | Semantic Similarity | `semantic-scorer` — Embedding similarity | Embeddings, cosine similarity |
| 22 | LLM-as-Judge | `llm-judge` — AI evaluating AI | G-Eval, rubric scoring |
| 23 | RAG Fundamentals | `simple-rag` — Build minimal RAG | Vector stores, retrieval |
| 24 | RAG Retrieval Eval | `retrieval-evaluator` — Test retrieval | Precision@k, Recall@k |
| 25 | RAG Generation Eval | `generation-evaluator` — Test generation | Faithfulness, relevancy |
| 26 | Hallucination Detection | `hallucination-detector` — Claim verification | Claims extraction, grounding |
| 27 | Custom Metrics | `custom-metric` — Domain specific metric | Metric design, calibration |
| 28 | Eval at Scale | `eval-pipeline` — Automated pipeline | Synthetic data, automation |

**Phase Outcome:** Can evaluate LLM outputs, understand key metrics, first custom metric built.
</details>

<details>
<summary><b>🟡 Phase 3: Testing Frameworks (Weeks 23-34)</b> — Mastering Production Tools</summary>

| Week | Focus | Mini-Project | Skills |
|------|-------|--------------|--------|
| 23 | DeepEval Setup | `deepeval-starter` — First DeepEval tests | Installation, basic usage |
| 24 | DeepEval Metrics | `deepeval-metrics-demo` — All built-in metrics | 14+ metrics mastery |
| 25 | DeepEval Advanced | `deepeval-custom` — Custom metrics in DeepEval | Custom metric integration |
| 26 | DeepEval CI/CD | `deepeval-pipeline` — GitHub Actions integration | CI/CD for LLM tests |
| 27 | RAGAS Fundamentals | `ragas-intro` — First RAGAS evaluation | Core RAGAS metrics |
| 28 | RAGAS Deep Dive | `ragas-advanced` — Synthetic data generation | Full RAGAS pipeline |
| 29 | Promptfoo Setup | `promptfoo-starter` — Prompt comparison testing | Promptfoo basics |
| 30 | Promptfoo Advanced | `prompt-ab-tester` — Full A/B testing pipeline | Advanced comparisons |
| 31 | Tool Comparison | `tool-benchmark` — Compare all 3 frameworks | When to use what |
| 32 | LangSmith Tracing | `langsmith-monitor` — Production monitoring | Observability |
| 33 | Combined Pipeline | `unified-evaluator` — All tools together | Integration patterns |
| 34 | Open Source Contribution #1 | `first-pr` — First PR to DeepEval/RAGAS | OSS contribution |

**Phase Outcome:** Proficient in all major frameworks, first open source contribution merged.
</details>

<details>
<summary><b>🔴 Phase 4: Red Teaming & Safety (Weeks 35-42)</b> — Security Testing for LLMs</summary>

| Week | Focus | Mini-Project | Skills |
|------|-------|--------------|--------|
| 35 | Garak Introduction | `garak-scanner` — First vulnerability scan | Garak basics |
| 36 | Prompt Injection | `injection-tester` — Test injection attacks | Attack patterns |
| 37 | Jailbreak Testing | `jailbreak-suite` — Comprehensive jailbreak tests | Jailbreak techniques |
| 38 | Custom Garak Probes | `custom-probes` — Build domain-specific probes | Probe development |
| 39 | OWASP LLM Top 10 | `owasp-tester` — Test all OWASP vulnerabilities | Security framework |
| 40 | DeepTeam Red Teaming | `deepteam-harness` — Structured adversarial testing | DeepTeam usage |
| 41 | Security Report | `security-reporter` — Generate security reports | Documentation |
| 42 | Red Team Capstone | `red-team-suite` — Complete red team toolkit | Full security testing |

**Phase Outcome:** Can conduct comprehensive LLM security assessments, OWASP expertise.
</details>

<details>
<summary><b>🟠 Phase 5: Agentic AI Testing (Weeks 43-48)</b> — Testing Systems That Think</summary>

| Week | Focus | Mini-Project | Skills |
|------|-------|--------------|--------|
| 43 | Agent Architecture | `agent-anatomy` — Understand ReAct pattern | Agent concepts |
| 44 | Tool Use Testing | `tool-tester` — Test function calling | Tool validation |
| 45 | Multi-Agent Systems | `multi-agent-tester` — Test agent collaboration | Agent orchestration |
| 46 | Agent Evaluation | `agent-evaluator` — Metrics for agents | Task completion metrics |
| 47 | LangGraph Testing | `langgraph-tester` — Test stateful agents | LangGraph patterns |
| 48 | Agent Safety | `agent-guardrails` — Test agent boundaries | Permission testing |

**Phase Outcome:** Can test complex agentic systems, understand agent failure modes.
</details>

<details>
<summary><b>⭐ Phase 6: Capstone (Weeks 49-52)</b> — Building LLMTestKit</summary>

| Week | Focus | Capstone Milestone | Deliverable |
|------|-------|-------------------|-------------|
| 49 | Architecture Design | Core framework structure | Design doc, folder structure |
| 50 | Core Implementation | Evaluation engine, metrics | Working evaluator |
| 51 | Advanced Features | Red team probes, reporting | Feature complete |
| 52 | Polish & Launch | Documentation, CI/CD, launch | **LLMTestKit v1.0** 🚀 |

**Capstone Deliverable: LLMTestKit** — An open-source LLM testing framework featuring:
- ✅ Modular evaluation engine
- ✅ 10+ built-in metrics
- ✅ Red team probe library
- ✅ CI/CD GitHub Action
- ✅ HTML/JSON report generator
- ✅ Full documentation
</details>

<details>
<summary><b>🔮 Optional: Advanced Track (Weeks 53+)</b> — For Staff/Principal Level</summary>

**ML/DL Deep Dive (12 weeks)** — Understanding the math behind metrics
- Neural network foundations
- Transformer architecture deep dive
- Build custom evaluation metric from scratch
- Contribute advanced features to open source

**Job Search Sprint (14 weeks)** — Landing the ₹75 LPA role
- Portfolio optimization
- Strategic networking
- Interview preparation
- Offer negotiation

*This track is optional but recommended for Staff/Principal AI Test Architect roles.*
</details>

---

## 📈 Weekly Progress Tracker

| Phase | Weeks | Status | Progress |
|-------|-------|--------|----------|
| 🔵 Foundation | 1-6 | 🟡 In Progress | ████░░░░░░ 16% |
| 🟣 LLM Fundamentals | 7-14 | ⚪ Not Started | ░░░░░░░░░░ 0% |
| 🟢 Evaluation | 15-22 | ⚪ Not Started | ░░░░░░░░░░ 0% |
| 🟡 Frameworks | 23-34 | ⚪ Not Started | ░░░░░░░░░░ 0% |
| 🔴 Red Teaming | 35-42 | ⚪ Not Started | ░░░░░░░░░░ 0% |
| 🟠 Agentic AI | 43-48 | ⚪ Not Started | ░░░░░░░░░░ 0% |
| ⭐ Capstone | 49-52 | ⚪ Not Started | ░░░░░░░░░░ 0% |

**Overall: Week 1/52** — 2% Complete

---

## 🗂️ Repository Structure

```
genai-testing-journey/
├── README.md                    # You are here
├── ROADMAP.md                   # Detailed weekly breakdown
├── PROGRESS.md                  # Detailed progress tracking
├── RESOURCES.md                 # Curated learning resources
│
├── weeks/                       # Weekly learning & projects
│   ├── week-01/
│   │   ├── notes/              # Learning notes
│   │   ├── practice/           # Practice code
│   │   ├── project/            # Mini-project
│   │   └── README.md           # Week summary
│   ├── week-02/
│   └── ...
│
├── projects/                    # Major projects
│   ├── test-suite-v1/          # Week 4 project
│   ├── rag-evaluator/          # Week 20 project
│   ├── red-team-suite/         # Week 42 project
│   └── LLMTestKit/             # Capstone (Weeks 49-52)
│
└── templates/                   # Reusable templates
    ├── test-case-template.json
    ├── evaluation-report.html
    └── weekly-update.md
```

---

## 🤝 Join the Community

**Learning alone is hard. Learning together is fun.**

### Ways to Participate:

1. **⭐ Star the Repo** — The best way to follow the journey.
2. **💬 Join Discussions** — Use the **Discussions tab** to share your weekly progress, find accountability partners, or ask questions.
3. **🍴 Fork & Build** — Don't just read—build! Fork this repo and follow the weekly guides.
4. **📺 Watch & Learn** — (Coming Soon) I break down complex GenAI testing concepts into simple explanations on [YouTube](https://youtube.com/@YOUR_CHANNEL_HANDLE).
5. **🔗 Connect** — Share your wins on [LinkedIn](https://www.linkedin.com/in/srv-sngh).

### Community Stats

| Metric | Count |
|--------|-------|
| GitHub Stars | 🌟 Growing |
| Forks | 🍴 Growing |
| Learning Together | 👥 Many! |

---

## 📖 Resources

### Quick Links
- [Full Detailed Roadmap](./ROADMAP.md)
- [Progress Tracker](./PROGRESS.md)
- [Resource Library](./RESOURCES.md)

### Key Tools We'll Master
| Tool | Purpose | Phase |
|------|---------|-------|
| [DeepEval](https://github.com/confident-ai/deepeval) | LLM evaluation framework | Phase 3 |
| [RAGAS](https://github.com/explodinggradients/ragas) | RAG evaluation | Phase 3 |
| [Promptfoo](https://github.com/promptfoo/promptfoo) | Prompt testing | Phase 3 |
| [Garak](https://github.com/NVIDIA/garak) | LLM vulnerability scanning | Phase 4 |
| [LangSmith](https://smith.langchain.com/) | LLM observability | Phase 3 |

### Essential Blogs
- [Jay Alammar](https://jalammar.github.io/) — Visual LLM explanations
- [Simon Willison](https://simonwillison.net/) — Prompt injection, LLM security
- [Eugene Yan](https://eugeneyan.com/) — LLM evaluation, MLOps
- [Confident AI Blog](https://www.confident-ai.com/blog) — LLM testing practices

---

## 📝 License

This project is licensed under the MIT License — feel free to use, modify, and share.

---

## 🙏 Acknowledgments

Special thanks to:
- The QA community for the incredible support on Day 1
- [Confident AI](https://confident-ai.com) for DeepEval
- [NVIDIA](https://nvidia.com) for Garak
- Everyone learning in public

---

<div align="center">

**Week 1/52 — The journey of a thousand miles begins with a single step.**

*Started: January 2026 | Target Completion: January 2027*

[![LinkedIn](https://img.shields.io/badge/Follow_the_Journey-LinkedIn-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/srv-sngh)
[![YouTube](https://img.shields.io/badge/Subscribe-YouTube-FF0000?style=for-the-badge&logo=youtube)](https://youtube.com/@YOUR_CHANNEL_HANDLE)
[![Twitter](https://img.shields.io/badge/Updates-Twitter-1DA1F2?style=for-the-badge&logo=twitter)](https://twitter.com/YOUR_HANDLE)

</div>
