<a name="readme-top"></a>

<h1 align="center">🧠 Awesome Agent Memory</h1>

<p align="center">
    A curated map of memory for AI agents — the systems, benchmarks, and research that give LLM and multimodal agents long-term context, persistent recall, and the ability to improve from experience.
</p>

<p align="center">
   👀 <b>Open-source</b> resources (e.g. papers with reproducible code publicly available on Github) are marked in bold font and ranked higher.
</p>

<p align="center">
   <a href="https://github.com/sindresorhus/awesome"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
   <a href="LICENSE"><img src="https://img.shields.io/badge/License-Apache_2.0-blue.svg" alt="License: Apache 2.0"></a>
   <a href="CONTRIBUTING.md"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome"></a>
   <a href="https://github.com/TeleAI-UAGI/Awesome-Agent-Memory/commits/main"><img src="https://img.shields.io/github/last-commit/TeleAI-UAGI/Awesome-Agent-Memory" alt="Last Commit"></a>
</p>

---

### 🧭 Start Here

| If you want to… | Jump to |
|---|---|
| Add a memory layer to an agent you're building | [💿 Products](#-products) |
| Choose a benchmark to evaluate a memory system | [📏 Benchmarks](#-benchmarks) |
| Get oriented in the field | [📖 Tutorials](#-tutorials) · [📚 Surveys](#-surveys) |
| Follow research on memory architectures | [🔤 Nonparametric Memory](#-papers---nonparametric-memory) · [🔢 Parametric Memory](#-papers---parametric-memory) |
| Build agents that learn from experience | [📈 Memory for Agent Evolution](#-papers---memory-for-agent-evolution) |
| Protect agent memory from poisoning and abuse | [🔒 Memory Security & Defense](#-memory-security--defense) |

<details>
  <summary>📋 <b>How this list is curated</b></summary>

  - Open-source products are ordered by GitHub star count — an objective, CI-checked popularity signal, not a quality ranking or an endorsement. Products with fewer than 100 stars sit in a collapsed **Emerging projects** section and graduate into the main list once they cross that threshold.
  - **Bold** marks resources with reproducible code publicly available.
  - Descriptions are factual, not promotional (see the [contributing guide](CONTRIBUTING.md)).
  - This list is maintained by [Bloo-Mind AI](https://www.bloo-mind.ai/) and the Ubiquitous AGI team at TeleAI. Entries affiliated with the maintainers are marked with † and follow exactly the same ranking, format, and style rules as every other entry.
  - Projects that are inactive, archived, or whose claims are disputed move to the [Archival](#archival) subsection with a neutral status label, links to the evidence, and the date the status was last checked.

</details>

<details>
  <summary>📰 <b>In the News</b></summary>

- 📰 [[Perplexity (2026-06-18)] Perplexity launches Brain, a self-improving memory system](https://www.perplexity.ai/hub/blog/self-improving-memory-for-agents)
- 📰 [[OpenAI (2026-06-04)] Dreaming: Better memory for a more helpful ChatGPT](https://openai.com/index/chatgpt-memory-dreaming/)
- 📰 [[Bloo-Mind AI (2026-05-20)] The Benchmark Theatre: Why Almost Nothing You’ve Read About Agent Memory Scores Is True](https://essays.bloo-mind.ai/posts/2026-05-20-mem-eval/) †
- 📰 [[Jiayi Weng (2026-05-09)] Learning Beyond Gradients](https://trinkle23897.github.io/learning-beyond-gradients/)
- 📰 [[Anthropic (2026-05-08)] Three key areas Anthropic is working on for their next models](https://www.reddit.com/r/singularity/comments/1t5q53r/three_key_areas_anthropic_is_working_on_for_their/)
- 📰 [[InfoQ (2026-04-30)] Cloudflare Announces Agent Memory, a Managed Persistent Memory Service for AI Agents](https://www.infoq.com/news/2026/04/cloudflare-agent-memory-beta/)
- 📰 [[OpenAI (2026-04-22)] Chronicle: Build Codex Memories from Recent Screen Context](https://developers.openai.com/codex/memories/chronicle)
    *  _Open-Source Alternatives_: [OpenChronicle](https://github.com/Einsia/OpenChronicle), [MemScreen](https://github.com/smileformylove/MemScreen) 
- 📰 [[a16z (2026-04-22)] Why We Need Continual Learning](https://a16z.com/why-we-need-continual-learning/)
- 📰 [[AI Godfather (2026-04-08)] MemPalace - How Milla Jovovich's AI Project Scammed the Internet](https://www.youtube.com/watch?v=WlxNNvDHJkE) 
- 📰 [[Troy Hua (2026-03-31)] How Anthropic Built 7 Layers of Memory and a Dreaming System for Claude Code](https://x.com/troyhua/status/2039052328070734102)
- 📰 [[VelvetShark (2026-03-05)] OpenClaw Memory Masterclass: The complete guide to agent memory that survives](https://velvetshark.com/openclaw-memory-masterclass)
- 📰 [[Business Insider (2026-01-08)] AI still needs a breakthrough in one key area to reach superintelligence, according to those who build it](https://www.businessinsider.com/superintelligent-ai-memory-sam-altman-2026-1)

</details>

---

<details open>
  <summary>🗂️ <b>Table of Contents</b> </summary>
  <ul>
    <li><a href="#-products">💿 Products</a></li>
    <li><a href="#-tutorials">📖 Tutorials</a></li>
    <li><a href="#-surveys">📚 Surveys</a></li>
    <li><a href="#-benchmarks">📏 Benchmarks</a></li>
    <ul>
        <li><a href="#-plain-text-benchmarks">💬 Plain-Text Benchmarks</a></li>
        <li><a href="#-multimodal-benchmarks">🎬 Multimodal Benchmarks</a></li>
        <li><a href="#-dynamic-benchmarks--simulation-environments">🎮 Dynamic Benchmarks & Simulation Environments</a></li>
    </ul>
    <li><a href="#-papers---nonparametric-memory">🔤 Papers - Nonparametric Memory</a></li>
    <ul>
        <li><a href="#-text-memory">📝 Text Memory</a></li>
        <li><a href="#-graph-memory">🌐 Graph Memory</a></li>
        <li><a href="#-multimodal-memory-for-understanding">🎥 Multimodal Memory (for Understanding)</a></li>
        <li><a href="#-multimodal-memory-for-generation">🎥 Multimodal Memory (for Generation)</a></li>
    </ul>
    <li><a href="#-papers---parametric-memory">🔢 Papers - Parametric Memory</a></li>
    <li><a href="#-papers---memory-for-agent-evolution">📈 Papers - Memory for Agent Evolution</a></li>
    <ul>
        <li><a href="#-reinforcement-learning--continual-learning">🧭 Reinforcement Learning & Continual Learning</a></li>
        <li><a href="#-context-engineering--harness-engineering">🧩 Context Engineering & Harness Engineering</a></li>
    </ul>
    <li><a href="#-papers---memory-in-cognitive-science">🔬 Papers - Memory in Cognitive Science</a></li>      
    <li><a href="#-memory-security--defense">🔒 Memory Security & Defense</a></li>
    <li><a href="#-articles">📰 Articles</a></li>
    <li><a href="#-workshops">👥 Workshops</a></li>
  </ul>
</details>

<div align="left">
    
**If you find this page helpful, please give it a ⭐️ — starring also keeps updates in your GitHub feed.**

_🤝 Contributions welcome! Feel free to open an issue or submit a pull request to add papers, fix links, or improve categorization — see the [contributing guide](CONTRIBUTING.md) for entry formats._

</div>

---

## 💿 Products

### Open-Source

_Ordered by the number of GitHub stars. Products with fewer than 100 stars continue the list inside the collapsed **Emerging projects** section below — they graduate into the main list once they cross that threshold._

1. **[Claude-Mem (A Plug-in for Claude-Code)](https://claude-mem.ai/)** 
     ![Star](https://img.shields.io/github/stars/thedotmack/claude-mem.svg?style=social&label=Star)
     [[code](https://github.com/thedotmack/claude-mem)]
     [[docs](https://docs.claude-mem.ai/introduction)]
     _Session capture and compression that re-injects past activity into future sessions across coding agents._

2. **[Mem0](https://mem0.ai/)** 
     ![Star](https://img.shields.io/github/stars/mem0ai/mem0.svg?style=social&label=Star)
     [[code](https://github.com/mem0ai/mem0)]
     [[docs](https://docs.mem0.ai/)]
     [[paper](https://arxiv.org/abs/2504.19413)]
     [[blog](https://mem0.ai/blog)]
     _Universal memory layer for AI agents._

    - **[TeleMem](https://github.com/TeleAI-UAGI/TeleMem)** †
        ![Star](https://img.shields.io/github/stars/TeleAI-UAGI/TeleMem.svg?style=social&label=Star)
        [[code](https://github.com/TeleAI-UAGI/TeleMem)]
        [[docs](https://teleai-uagi.github.io/telemem/)]
        [[paper](https://arxiv.org/abs/2601.06037)]
        _API-compatible drop-in replacement for Mem0 (`import telemem as mem0`); listed as a sub-item of Mem0 rather than ranked by stars. Maintainer-affiliated._

3. **[Zep (powered by Graphiti)](https://www.getzep.com/)** 
     ![Star](https://img.shields.io/github/stars/getzep/graphiti.svg?style=social&label=Star)
     [[code](https://github.com/getzep/graphiti)]
     [[paper](https://arxiv.org/abs/2501.13956)]
     [[blog](https://blog.getzep.com/)]
     _Real-time temporal knowledge graphs for AI agents._

4. **[Cognee](https://www.cognee.ai/)** 
     ![Star](https://img.shields.io/github/stars/topoteretes/cognee.svg?style=social&label=Star)
     [[code](https://github.com/topoteretes/cognee)]
     [[paper](https://arxiv.org/abs/2505.24478)]
     [[blog](https://www.cognee.ai/blog)]
     _Memory engine that ingests data into a hybrid graph + vector knowledge graph for cross-session agent recall._

5. **[gbrain](https://github.com/garrytan/gbrain)** 
     ![Star](https://img.shields.io/github/stars/garrytan/gbrain.svg?style=social&label=Star)
     [[code](https://github.com/garrytan/gbrain)]
     _Garry's opinionated OpenClaw/Hermes agent brain._

6. **[agentmemory](https://www.agent-memory.dev/)** 
     ![Star](https://img.shields.io/github/stars/rohitg00/agentmemory.svg?style=social&label=Star)
     [[code](https://github.com/rohitg00/agentmemory)]
     _Persistent memory for AI coding agents._

7. **[Letta (formerly MemGPT)](https://www.letta.com/)** 
     ![Star](https://img.shields.io/github/stars/letta-ai/letta.svg?style=social&label=Star)
     [[code](https://github.com/letta-ai/letta)]
     [[paper](https://arxiv.org/abs/2310.08560)]
     [[research](https://www.letta.com/research)]
     [[blog](https://www.letta.com/blog)]
     _Stateful-agent platform with hierarchical memory that learns and self-improves over time._

8. **[Hindsight](https://hindsight.vectorize.io/)** 
     ![Star](https://img.shields.io/github/stars/vectorize-io/hindsight.svg?style=social&label=Star)
     [[code](https://github.com/vectorize-io/hindsight)]
     [[paper](https://arxiv.org/abs/2512.12818)]
      _Agent memory layer that learns from interaction feedback to improve recall over time._

9. **[Second Me](https://home.second.me/)** 
     ![Star](https://img.shields.io/github/stars/mindverse/Second-Me.svg?style=social&label=Star)
     [[code](https://github.com/mindverse/Second-Me)]
     [[paper](https://arxiv.org/abs/2503.08102)]
     _Personal AI trained on the user to represent them across applications._

10. **[MemU](https://memu.pro/)** 
      ![Star](https://img.shields.io/github/stars/NevaMind-AI/memU.svg?style=social&label=Star)
      [[code](https://github.com/NevaMind-AI/memU)]
      [[blog](https://memu.pro/blog)]
      _Memory layer for 24/7 proactive agents._

11. **[EverOS (part of EverMind)](https://evermind-ai.com/)** 
      ![Star](https://img.shields.io/github/stars/EverMind-AI/EverOS.svg?style=social&label=Star)
      [[code](https://github.com/EverMind-AI/EverOS)]
      [[blog](https://evermind-ai.com/blog/)]
      _Toolkit for building, evaluating, and integrating long-term memory in self-evolving agents._

12. **[MemOS (by MemTensor)](https://memos.openmem.net/)** 
      ![Star](https://img.shields.io/github/stars/MemTensor/MemOS.svg?style=social&label=Star)
      [[code](https://github.com/MemTensor/MemOS)]
      [[paper](https://arxiv.org/abs/2507.03724)]
      _Memory OS for LLM agents with hybrid retrieval and cross-task skill reuse._

13. **[TencentDB Agent Memory](https://github.com/Tencent/TencentDB-Agent-Memory)** 
      ![Star](https://img.shields.io/github/stars/Tencent/TencentDB-Agent-Memory.svg?style=social&label=Star)
      [[code](https://github.com/Tencent/TencentDB-Agent-Memory)]
      _Fully local long-term memory for AI agents via a 4-tier progressive pipeline, with zero external API dependencies._

14. **[Honcho](https://honcho.dev/)** 
      ![Star](https://img.shields.io/github/stars/plastic-labs/honcho.svg?style=social&label=Star)
      [[code](https://github.com/plastic-labs/honcho)]
      [[research](https://blog.plasticlabs.ai/research/)]
      [[blog](https://blog.plasticlabs.ai/)]
      [[evals](https://evals.honcho.dev/)]
      _Memory library for stateful agents with a focus on user modeling._

15. **[engram](https://github.com/Gentleman-Programming/engram)** 
      ![Star](https://img.shields.io/github/stars/Gentleman-Programming/engram.svg?style=social&label=Star)
      [[code](https://github.com/Gentleman-Programming/engram)]
      _Persistent memory for AI coding agents — agent-agnostic single Go binary with SQLite + FTS5, exposed via MCP server, HTTP API, CLI, and TUI._

16. **[MemoryBear](https://www.memorybear.ai/)** 
      ![Star](https://img.shields.io/github/stars/SuanmoSuanyangTechnology/MemoryBear.svg?style=social&label=Star)
      [[code](https://github.com/SuanmoSuanyangTechnology/MemoryBear)]
      [[paper](https://arxiv.org/abs/2512.20651)]
      _Memory framework providing human-like episodic and semantic recall to AI agents._

17. **[memory-lancedb-pro](https://github.com/CortexReach/memory-lancedb-pro)** 
      ![Star](https://img.shields.io/github/stars/CortexReach/memory-lancedb-pro.svg?style=social&label=Star)
      [[code](https://github.com/CortexReach/memory-lancedb-pro)]
      [[blog](https://lancedb.com/blog/openclaw-lancedb-memory-layer/)]
      [[video](https://www.youtube.com/watch?v=bhuGrjuCM_g)]
      _Enhanced [LanceDB](https://lancedb.com/) memory plugin for [OpenClaw](https://openclaw.ai/)_

18. **[OpenMemory](https://openmemory.cavira.app/)** 
      ![Star](https://img.shields.io/github/stars/caviraoss/openmemory.svg?style=social&label=Star)
      [[code](https://github.com/caviraoss/openmemory)]
      _Local persistent memory store for LLM apps (Claude Desktop, Copilot, Codex, etc.)._

19. **[MIRIX](https://mirix.io/)** 
      ![Star](https://img.shields.io/github/stars/Mirix-AI/MIRIX.svg?style=social&label=Star)
      [[code](https://github.com/Mirix-AI/MIRIX)]
      [[paper](https://arxiv.org/abs/2507.07957)]
      [[blog](https://mirix.io/#/blog)]
      _Multi-agent personal assistant that captures on-screen activity and consolidates it into structured memory._

20. **[MemMachine](https://memmachine.ai/)** 
      ![Star](https://img.shields.io/github/stars/MemMachine/MemMachine.svg?style=social&label=Star)
      [[code](https://github.com/MemMachine/MemMachine)]
      [[blog](https://memmachine.ai/blog/)]
      _Interoperable memory layer providing extensible storage and retrieval primitives for AI agents._

21. **[Memobase](https://memobase.io/)** 
      ![Star](https://img.shields.io/github/stars/memodb-io/memobase.svg?style=social&label=Star)
      [[code](https://github.com/memodb-io/memobase)]
      [[blog](https://www.memobase.io/blog)]
      _User profile-based long-term memory for AI chatbot applications._

22. **[Memanto](https://memanto.ai/)** ![Star](https://img.shields.io/github/stars/moorcheh-ai/memanto.svg?style=social&label=Star)
      [[code](https://github.com/moorcheh-ai/memanto)]
      [[paper](https://arxiv.org/abs/2604.22085)]
      [[docs](https://docs.memanto.ai)]
      _Typed semantic memory with `remember`/`recall`/`answer` operations and information-theoretic retrieval._

23. **[LangMem](https://langchain-ai.github.io/langmem/)** 
      ![Star](https://img.shields.io/github/stars/langchain-ai/langmem.svg?style=social&label=Star)
      [[code](https://github.com/langchain-ai/langmem)]
      [[blog](https://blog.langchain.com/)]
      _LangChain's memory primitives for storing, recalling, and managing agent state in LangGraph workflows._

24. **[Mem9](https://mem9.ai/)** 
      ![Star](https://img.shields.io/github/stars/mem9-ai/mem9.svg?style=social&label=Star)
      [[code](https://github.com/mem9-ai/mem9)]
      [[blog](https://addozhang.medium.com/keep-memory-local-building-a-private-openclaw-memory-hub-with-mem9-tidb-5b305345b40a)]
      _Local private memory hub for OpenClaw and similar coding agents._

25. **[Omnigraph](https://github.com/ModernRelay/omnigraph)** 
      ![Star](https://img.shields.io/github/stars/ModernRelay/omnigraph.svg?style=social&label=Star)
      [[code](https://github.com/ModernRelay/omnigraph)]
      _Object-storage-native graph engine for agent memory with git-style branch/merge workflows._

26. **[Puppyone](https://www.puppyone.ai)** 
      ![Star](https://img.shields.io/github/stars/puppyone-ai/puppyone.svg?style=social&label=Star)
      [[code](https://github.com/puppyone-ai/puppyone)]
      [[docs](https://www.puppyone.ai/doc)]
      _Filesystem-shaped agent memory with auto-versioning, per-agent ACLs, and data connectors; accessible via MCP/REST/CLI._

27. **[PowerMem](https://www.powermem.ai)**
      ![Star](https://img.shields.io/github/stars/oceanbase/powermem.svg?style=social&label=Star)
      [[code](https://github.com/oceanbase/powermem)]
      _Persistent, self-evolving memory for AI agents — hybrid vector/full-text/graph retrieval with LLM-driven extraction, Ebbinghaus-style decay, and two-layer Experience + Skill distillation; from the OceanBase team._

28. **[Vestige](https://github.com/samvallad33/vestige)**
      ![Star](https://img.shields.io/github/stars/samvallad33/vestige.svg?style=social&label=Star)
      [[code](https://github.com/samvallad33/vestige)]
      [[release](https://github.com/samvallad33/vestige/releases/tag/v2.1.23)]
      _Local-first cognitive memory MCP server for coding agents, with FSRS-6 decay, spreading activation, active suppression, Receipt Lock, and an inspectable dashboard._

29. **[CodeAlmanac](https://github.com/AlmanacCode/codealmanac)**
      ![Star](https://img.shields.io/github/stars/AlmanacCode/codealmanac.svg?style=social&label=Star)
      [[code](https://github.com/AlmanacCode/codealmanac)]
      _Repo-local Markdown wiki for AI coding agents that preserves project conversations, decisions, and implementation context._

30. **[MemClaw (Caura)](https://memclaw.net/)**
      ![Star](https://img.shields.io/github/stars/caura-ai/caura-memclaw.svg?style=social&label=Star)
      [[code](https://github.com/caura-ai/caura-memclaw)]
      [[blog](https://memclaw.net/blog)]
      _Governed shared memory for AI agent fleets — cross-agent knowledge sharing with permissions, audit trails, and self-learning._

31. **[MisakaNet](https://github.com/Ikalus1988/MisakaNet)**
      ![Star](https://img.shields.io/github/stars/Ikalus1988/MisakaNet.svg?style=social&label=Star)
      [[code](https://github.com/Ikalus1988/MisakaNet)]
      [[wiki](https://github.com/Ikalus1988/MisakaNet/wiki)]
      _Git-based distributed swarm memory; agents share lessons across nodes via GitHub Issues._

32. **[Statewave](https://statewave.ai/)**
      ![Star](https://img.shields.io/github/stars/smaramwbc/statewave.svg?style=social&label=Star)
      [[code](https://github.com/smaramwbc/statewave)]
      [[docs](https://github.com/smaramwbc/statewave-docs)]
      [[blog](https://www.statewave.ai/blog)]
      _Open-source memory runtime for AI agents serving reproducible, provenance-tagged context bundles instead of query-time retrieval; self-hosted on Postgres + pgvector with Python/TypeScript SDKs._

33. **[Memov](https://www.memov.ai/)** 
      ![Star](https://img.shields.io/github/stars/memovai/memov.svg?style=social&label=Star)
      [[code](https://github.com/memovai/memov)]
      _Git-based, traceable memory layer for Claude Code._

34. **[Mnemory](https://github.com/fpytloun/mnemory)** ![Star](https://img.shields.io/github/stars/fpytloun/mnemory.svg?style=social&label=Star)
      [[code](https://github.com/fpytloun/mnemory)]
      _Multi-type agent memory (facts, preferences, episodic) with TTLs, user/agent scoping, and an MCP server._

35. **[OMEGA](https://omegamax.co)** ![Star](https://img.shields.io/github/stars/omega-memory/omega-memory.svg?style=social&label=Star)
      [[code](https://github.com/omega-memory/omega-memory)]
      [[blog](https://omegamax.co/blog)]
      _MCP server exposing 25 memory tools for AI coding agents._

36. **[projectmem](https://projectmem.dev)**
      ![Star](https://img.shields.io/github/stars/riponcm/projectmem.svg?style=social&label=Star)
      [[code](https://github.com/riponcm/projectmem)]
      [[docs](https://projectmem.dev/guide)]
      [[paper](https://arxiv.org/abs/2606.12329)]
      _Local-first, event-sourced memory and judgment layer for AI coding agents: an append-only event log served via MCP, plus a pre-commit gate that warns before repeating a failed fix._

37. **[CommonGround Kernel](https://github.com/Intelligent-Internet/CommonGround)** 
      ![Star](https://img.shields.io/github/stars/Intelligent-Internet/CommonGround.svg?style=social&label=Star)
      [[code](https://github.com/Intelligent-Internet/CommonGround)]
      _PostgreSQL-backed shared work-record substrate for human-agent and multi-agent systems, with durable handoff facts, causal lineage, and pull-first recovery across runtimes._

<details>
  <summary>🌱 <b>Emerging projects</b> — open-source products with fewer than 100 GitHub stars, same format and ordering (click to expand)</summary>

38. **[taOSmd](https://github.com/jaylfc/taosmd)**
      ![Star](https://img.shields.io/github/stars/jaylfc/taosmd.svg?style=social&label=Star)
      [[code](https://github.com/jaylfc/taosmd)]
      [[benchmarks](https://github.com/jaylfc/taosmd/blob/master/docs/benchmarks.md)]
      _Local-first, offline agent memory: an append-only transcript yields a typed temporal knowledge graph with source-grounded, verifier-checked facts and hybrid retrieval, tuned for small local models._

39. **[widemem-ai](https://widemem.ai)**
      ![Star](https://img.shields.io/github/stars/remete618/widemem-ai.svg?style=social&label=Star)
      [[code](https://github.com/remete618/widemem-ai)]
      _Lightweight memory layer with importance scoring, temporal decay, and 3-tier hierarchy._

40. **[Origin](https://useorigin.app/)**
      ![Star](https://img.shields.io/github/stars/7xuanlu/origin.svg?style=social&label=Star)
      [[code](https://github.com/7xuanlu/origin)]
      [[docs](https://useorigin.app/docs)]
      _Local-first AI work memory for coding agents and MCP clients: session handoffs, source-backed wiki pages, graph context, and hybrid retrieval via one local daemon._

41. **[Synap](https://maximem.ai)** 
      ![Star](https://img.shields.io/github/stars/maximem-ai/maximem_synap_sdk.svg?style=social&label=Star)
      [[code](https://github.com/maximem-ai/maximem_synap_sdk)]
      [[docs](https://docs.maximem.ai)]
      _Long-term memory layer that extracts facts, preferences, episodes, and temporal events from conversations; integrates with most major agent frameworks._

42. **[memclaw (Felo)](https://memclaw.me)**
      ![Star](https://img.shields.io/github/stars/Felo-Inc/memclaw.svg?style=social&label=Star)
      [[code](https://github.com/Felo-Inc/memclaw)]
      _Persistent project memory for AI coding agents — isolated per-project workspaces, a web dashboard to review what the agent remembers, and team collaboration._

43. **[Mimir](https://github.com/Perseus-Computing-LLC/mimir)** 
      ![Star](https://img.shields.io/github/stars/Perseus-Computing-LLC/mimir.svg?style=social&label=Star)
      [[code](https://github.com/Perseus-Computing-LLC/mimir)]
      _MCP-native persistent memory for agents as a single Rust binary — embedded SQLite with FTS5 + vector hybrid search, AES-256-GCM encryption at rest, fully local._

44. **[Data Olympus](https://github.com/knaisoma/data-olympus)**
      ![Star](https://img.shields.io/github/stars/knaisoma/data-olympus.svg?style=social&label=Star)
      [[code](https://github.com/knaisoma/data-olympus)]
      _Governed project memory for AI coding agents: agents propose learnings, humans promote them, and MCP retrieval serves only in-force knowledge after validity and supersession checks._

45. **[A3M Router](https://github.com/Das-rebel/a3m-router)**
      ![Star](https://img.shields.io/github/stars/Das-rebel/a3m-router.svg?style=social&label=Star)
      [[code](https://github.com/Das-rebel/a3m-router)]
      _Multi-model LLM router with persistent memory (MemoryTree), cross-session context-window management, conversation memory with semantic recall, and ObsidianVault integration._

46. **[GoodMemory](https://github.com/hjqcan/GoodMemory)**
      ![Star](https://img.shields.io/github/stars/hjqcan/GoodMemory.svg?style=social&label=Star)
      [[code](https://github.com/hjqcan/GoodMemory)]
      [[docs](https://github.com/hjqcan/GoodMemory#quickstart-codex-or-claude-code-memory)]
      _Local-first, auditable memory layer for AI agents and coding hosts, with durable SQLite, embedding-free recall, MCP access, and opt-in governed writeback._

47. **[Agentic Task System](https://github.com/renezander030/agentic-task-system)**
      ![Star](https://img.shields.io/github/stars/renezander030/agentic-task-system.svg?style=social&label=Star)
      [[code](https://github.com/renezander030/agentic-task-system)]
      [[npm](https://www.npmjs.com/package/@reneza/ats-cli)]
      _Agent-native context layer over your existing task app (TickTick; Notion/Obsidian planned), exposing hybrid retrieval over tasks/notes to agents via a CLI with pluggable storage adapters._

48. **[archon-memory-core](https://github.com/atw4757-byte/archon-memory-core)**
      ![Star](https://img.shields.io/github/stars/atw4757-byte/archon-memory-core.svg?style=social&label=Star)
      [[code](https://github.com/atw4757-byte/archon-memory-core)]
      _Local-first agent memory with nightly consolidation, active forgetting, and salience scoring._

49. **[FluctlightDB](https://github.com/voxmastery/FluctlightDB)**
      ![Star](https://img.shields.io/github/stars/voxmastery/FluctlightDB.svg?style=social&label=Star)
      [[code](https://github.com/voxmastery/FluctlightDB)]
      [[paper](https://doi.org/10.5281/zenodo.20949890)]
      _Embedded database engine for AI agents with `experience()`/`activate()` API and reproducible LoCoMo evaluation._

50. **[Tree Ring Memory](https://terminallylazy.github.io/Tree-Ring-Memory/)**
      ![Star](https://img.shields.io/github/stars/TerminallyLazy/Tree-Ring-Memory.svg?style=social&label=Star)
      [[code](https://github.com/TerminallyLazy/Tree-Ring-Memory)]
      _Local-first memory lifecycle for AI agents with a Rust CLI, SQLite/FTS recall, audit, forgetting, consolidation, and Ratatui TUI._

51. **[Agent Knowledge Cycle](https://github.com/shimo4228/agent-knowledge-cycle)**
      ![Star](https://img.shields.io/github/stars/shimo4228/agent-knowledge-cycle.svg?style=social&label=Star)
      [[code](https://github.com/shimo4228/agent-knowledge-cycle)]
      [[paper](https://doi.org/10.5281/zenodo.20578272)]
      _Six-phase knowledge cycle specification (ADRs, JSON schemas, reference implementation) that turns coding-agent sessions into persistent skills, rules, and memory._

52. **[PackRat](https://github.com/kevdogg102396-afk/packrat)**
      ![Star](https://img.shields.io/github/stars/kevdogg102396-afk/packrat.svg?style=social&label=Star)
      [[code](https://github.com/kevdogg102396-afk/packrat)]
      _Auto-learning codebook compression that shrinks agent context files while keeping them LLM-readable._

53. **[Akephalos](https://github.com/sunnja69/akephalos)**
      ![Star](https://img.shields.io/github/stars/sunnja69/akephalos.svg?style=social&label=Star)
      [[code](https://github.com/sunnja69/akephalos)]
      _Local-first, markdown-based portable agent profile (preferences, rules, durable memories) synced across agents via plain files and Git._

54. **[溯忆 (Suyi)](https://github.com/xiaofanliu525-ctrl/suyi-memory)**
      ![Star](https://img.shields.io/github/stars/xiaofanliu525-ctrl/suyi-memory.svg?style=social&label=Star)
      [[code](https://github.com/xiaofanliu525-ctrl/suyi-memory)]
      _Dual-temporal memory engine for AI agents — SQLite-backed, zero-dependency, Ebbinghaus-decayed fact storage with skill crystallization._

</details>

### Closed-Source

-  [MemoryLake](https://www.memorylake.ai/en)
   [[blog](https://www.memorylake.ai/en/blogs)]

-  [Supermemory](https://supermemory.ai/)
   [[partial-code](https://github.com/supermemoryai/supermemory)]
   [[blog](https://supermemory.ai/blog)]

-  [Memories.ai](https://memories.ai/)
   [[research](https://memories.ai/research)]
   [[paper](https://memories.ai/research/Camera)]
   [[blog](https://memories.ai/blogs)]

-  [Macaron Mind Lab](https://macaron.im/mindlab)
   [[blog](https://macaron.im/mindlab/research)]
   [[paper](https://macaron.im/mindlab/publications)]
   
-  [Mem 2.0](https://get.mem.ai/)
   [[blog](https://get.mem.ai/blog)]

-  [M-Flow](https://m-flow.ai/)

-  [TwinMind](https://twinmind.com/)
   [[blog](https://twinmind.com/blogs)]

-  [Penfield](https://www.penfield.app/)
   [[blog](https://penfieldlabs.substack.com/)]

-  [Sonzai](https://sonz.ai/)

-  [Threadline](https://threadline.to)
   [[partial-code](https://github.com/vidursharma202-del/threadline-mcp)]
   [[schema](https://github.com/vidursharma202-del/context-schema)]
   [[docs](https://threadline.to/docs)]

-  [Remio](https://remio.ai/)
   _Local-first personal knowledge base that indexes files, webpages, recordings, notes, emails, and messages for agent retrieval via search and RAG._

-  [AccInt](https://accint.xyz)
   [[partial-code](https://github.com/maxbaluev/accreted-intelligence)]
   _Local-first MCP Work Model for coding agents that retrieves scored memory, records actions, and credits real outcomes; engine is a closed-source binary._

-  [Agentage Memory](https://memory.agentage.io)
   _Remote MCP memory server (OAuth 2.1 + PKCE + DCR) giving Claude, Cursor, and ChatGPT one shared markdown memory mirrored locally as files you own._

-  [screenpipe](https://screenpipe.com)
   [[source-available](https://github.com/screenpipe/screenpipe)]
   [[license](https://github.com/screenpipe/screenpipe/blob/main/LICENSE.md)]
   [[docs](https://docs.screenpi.pe)]
   _Local-first work memory that captures screen, audio, input, browser, and meeting context for search and agent retrieval._

### Archival

_Projects that are inactive or whose claims have been disputed by third parties. Status labels link to the evidence and note when the status was last checked._

-  [MemPalace](https://github.com/MemPalace/mempalace) ⚠️ Disputed (third-party critiques challenge the project's core claims; last checked 2026-07)
   [[code](https://github.com/milla-jovovich/mempalace)]
   [[critique1](https://www.youtube.com/watch?v=WlxNNvDHJkE), [critique2](https://penfieldlabs.substack.com/p/milla-jovovich-just-released-an-ai)]
   _Developed by actress [Milla Jovovich](https://en.wikipedia.org/wiki/Milla_Jovovich) and her friends_

-  [Memvid](https://www.memvid.com/) ⚠️ Disputed (technical critique raised in GitHub issues, since deleted but archived; last checked 2026-07)
   [[code](https://github.com/Olow304/memvid)]
   [[critique (archived)](https://web.archive.org/web/20250807093442/https://github.com/Olow304/memvid/issues/49)]

-  [Memary](https://kingjulio8238.github.io/memarydocs/) ❄️ Inactive (no significant development activity; last checked 2026-07)
   [[code](https://github.com/kingjulio8238/memary)]

---

## 📖 Tutorials

#### 🗓️ 2026

 - **[Agent Memory Techniques](https://github.com/NirDiamant/Agent_Memory_Techniques)** (NirDiamant): 30 runnable Jupyter notebooks covering conversation buffers, vector stores, knowledge graphs, episodic and semantic memory, Mem0, MemGPT/Letta, Zep, Graphiti, and LoCoMo benchmarks
     [[code](https://github.com/NirDiamant/Agent_Memory_Techniques)]

- **[Memory, Context, and Retrieval](https://books.bloo-mind.ai/masact/ch-07-memory-context-retrieval)** †: Chapter 7 of the book _[Multi-Agent Systems: A Contemporary Treatment](https://books.bloo-mind.ai/masact/)_.
  
#### 🗓️ 2025

 - **[ACM SIGIR-AP 2025](https://www.sigir-ap.org/sigir-ap-2025/) Tutorial: [Conversational Agents: From RAG to LTM](https://sites.google.com/view/ltm-tutorial)** †
     [[paper](https://dl.acm.org/doi/10.1145/3767695.3769671)]
     [[code](https://github.com/TeleAI-UAGI/Awesome-Agent-Memory)]
 
 - Daily Dose of DS: A Practical Deep Dive Into Memory Optimization for Agentic Systems
     [[Part-A](https://www.dailydoseofds.com/ai-agents-crash-course-part-15-with-implementation/)]
     [[Part-B](https://www.dailydoseofds.com/ai-agents-crash-course-part-16-with-implementation/)]
     [[Part-C](https://www.dailydoseofds.com/ai-agents-crash-course-part-17-with-implementation/)]

---

## 📚 Surveys

#### 🗓️ 2026

- **[Memory in the LLM Era: Modular Architectures and Strategies within a Unified Framework](https://arxiv.org/abs/2604.01707)**
    [[code](https://github.com/Yanchen398/Memory-in-the-LLM-Era)]

- **[From Storage to Experience: A Survey on the Evolution of LLM Agent Memory Mechanisms](https://arxiv.org/abs/2605.06716)**
    [[code](https://github.com/FeishuLuo/Evolving-LLM-Agent-Memory-Survey)]

- **[Rethinking Memory Mechanisms of Foundation Agents in the Second Half: A Survey](https://arxiv.org/abs/2602.06052)**
    [[code](https://github.com/AgentMemoryWorld/Awesome-Agent-Memory)]

- **[Toward Efficient Agents: Memory, Tool learning, and Planning](https://arxiv.org/abs/2601.14192)**
    [[code](https://github.com/yxf203/Awesome-Efficient-Agents)]

- [LLM Agent Memory: A Survey from a Unified Representation–Management Perspective](https://www.preprints.org/manuscript/202603.0359)

- [Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Emerging Frontiers](https://arxiv.org/abs/2603.07670)

- [Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering](https://arxiv.org/abs/2604.08224)

- [Survey on AI Memory: Theories, Taxonomies, Evaluations, and Emerging Trends](https://github.com/BAI-LAB/Survey-on-AI-Memory/blob/main/Survey%20on%20AI%20Memory.pdf)

- [The AI Hippocampus: How Far are We From Human Memory?](https://arxiv.org/abs/2601.09113)

#### 🗓️ 2025

- **[AI Meets Brain: Memory Systems from Cognitive Neuroscience to Autonomous Agents](https://arxiv.org/abs/2512.23343)**
    [[code](https://github.com/AgentMemory/Huaman-Agent-Memory)]

- **[Memory in the Age of AI Agents](https://arxiv.org/abs/2512.13564)**
    [[code](https://github.com/Shichun-Liu/Agent-Memory-Paper-List)]

- **[Rethinking Memory in AI: Taxonomy, Operations, Topics, and Future Directions](https://arxiv.org/abs/2505.00675)**
    [[code](https://github.com/Elvin-Yiming-Du/Survey_Memory_in_AI)]
  
- [From Human Memory to AI Memory: A Survey on Memory Mechanisms in the Era of LLMs](https://arxiv.org/abs/2504.15965)

- [Cognitive Memory in Large Language Models](https://arxiv.org/abs/2504.02441)

- [Advances and Challenges in Foundation Agents: From Brain-Inspired Intelligence to Evolutionary, Collaborative, and Safe Systems (Chapter 3)](https://arxiv.org/abs/2504.01990)

- [Human-inspired Perspectives: A Survey on AI Long-term Memory](https://arxiv.org/abs/2411.00489)
   
#### 🗓️ 2024

- **[A Survey on the Memory Mechanism of Large Language Model based Agents](https://arxiv.org/abs/2404.13501)**
    [[code](https://github.com/nuster1128/LLM_Agent_Memory_Survey)]

---

## 📏 Benchmarks

### 💬 Plain-Text Benchmarks

#### 🗓️ 2026

- **OmniMemEval**
    [[code](https://github.com/MemTensor/OmniMemEval)]

- **[Are We Ready For An Agent-Native Memory System?](https://arxiv.org/abs/2606.24775)**
    (The MemoryData Paper)
   [[code](https://github.com/OpenDataBox/MemoryData)]
 
- **[Locomo-Plus: Beyond-Factual Cognitive Memory Evaluation Framework for LLM Agents](https://arxiv.org/abs/2602.10715)**
    [[code](https://github.com/xjtuleeyf/Locomo-Plus)]

- **LoCoMo Refined: Recalibrating LoCoMo with Stricter LLM Judging and A Cleaned Dataset**
    [[code](https://github.com/mem-eval-suite/LoCoMo_refined)]

#### 🗓️ 2025

- **[Beyond a Million Tokens: Benchmarking and Enhancing Long-Term Memory in LLMs](https://arxiv.org/abs/2510.27246)** 
    (The BEAM Paper)
    [[code](https://github.com/mohammadtavakoli78/BEAM)]
    [[data](https://huggingface.co/datasets/Mohammadta/BEAM)]
  
- **[MOOM: Maintenance, Organization and Optimization of Memory in Ultra-Long Role-Playing Dialogues](https://arxiv.org/abs/2509.11860)** 
    (The ZH-4O Paper)
    [[code](https://github.com/cows21/MOOM-Roleplay-Dialogue)]
    [[data](https://github.com/cows21/MOOM-Roleplay-Dialogue/tree/main/data)]

- **[Know Me, Respond to Me: Benchmarking LLMs for Dynamic User Profiling and Personalized Responses at Scale](https://arxiv.org/abs/2504.14225)** 
    (The PersonaMem and ImplicitPersona Paper)
    [[code](https://github.com/bowen-upenn/PersonaMem)]
    [[data11](https://huggingface.co/datasets/bowen-upenn/PersonaMem)]
    [[data2](https://huggingface.co/datasets/bowen-upenn/ImplicitPersona)]

- **[Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions](https://arxiv.org/abs/2507.05257)** 
    (The MemoryAgentBench Paper)
    [[code](https://github.com/HUST-AI-HYZ/MemoryAgentBench)]
    [[data](https://huggingface.co/datasets/ai-hyz/MemoryAgentBench)]

- **[LifelongAgentBench: Evaluating LLM Agents as Lifelong Learners](https://arxiv.org/abs/2505.11942)**
    [[code](https://github.com/caixd-220529/LifelongAgentBench)]
    [[data](https://huggingface.co/datasets/csyq/LifelongAgentBench)]

- **[NoLiMa: Long-Context Evaluation Beyond Literal Matching](https://arxiv.org/abs/2502.05167)**
    [[code](https://github.com/adobe-research/NoLiMa)]
    [[data](https://github.com/adobe-research/NoLiMa/tree/main/data)]

- **[HaluMem: Evaluating Hallucinations in Memory Systems of Agents](http://arxiv.org/abs/2511.03506)**
    [[code](https://github.com/MemTensor/HaluMem)]
    [[data](https://huggingface.co/datasets/IAAR-Shanghai/HaluMem)]

- **[LongBench v2: Towards Deeper Understanding and Reasoning on Realistic Long-context Multitasks](https://arxiv.org/abs/2412.15204)**
    [[code](https://github.com/THUDM/LongBench)]

- **[Minerva: A Programmable Memory Test Benchmark for Language Models](https://arxiv.org/abs/2502.03358)**
    [[code](https://github.com/microsoft/minerva_memory_test)]

- **[MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents](https://arxiv.org/abs/2506.21605)**
    [[code](https://github.com/import-myself/Membench)]

- [Evo-Memory: Benchmarking LLM Agent Test-time Learning with Self-Evolving Memory](https://arxiv.org/abs/2511.20857)

- [OdysseyBench: Evaluating LLM Agents on Long-Horizon Complex Office Application Workflows](https://arxiv.org/abs/2508.09124)
   
#### 🗓️ 2024

- **[LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](https://arxiv.org/abs/2410.10813)**
   [[data](https://github.com/xiaowu0162/LongMemEval)]
   
- **[Evaluating Very Long-Term Conversational Memory of LLM Agents](https://arxiv.org/abs/2402.17753)** 
    (The LoCoMo Paper)
    [[code](https://github.com/snap-research/LoCoMo)]
    [[data](https://github.com/snap-research/locomo/tree/main/data)]

- **[∞Bench: Extending Long Context Evaluation Beyond 100K Tokens](https://arxiv.org/abs/2402.13718v3)**
    [[code](https://github.com/OpenBMB/InfiniteBench)]

- **[LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding](https://arxiv.org/abs/2308.14508)**
    [[code](https://github.com/THUDM/LongBench)]

#### 🗓️ 2023

- **[StoryBench: A Multifaceted Benchmark for Continuous Story Visualization](https://proceedings.neurips.cc/paper_files/paper/2023/hash/f63f5fbed1a4ef08c857c5f377b5d33a-Abstract-Datasets_and_Benchmarks.html)**
    [[code](https://github.com/google/storybench)]

### 🎬 Multimodal Benchmarks

#### 🗓️ 2026

- **[MBench: A Comprehensive Benchmark on Memory Capability for Video World Models](https://arxiv.org/abs/2606.00793)**
    [[code](https://github.com/study-overflow/MBench)]
    [[proj](https://peanutup.github.io/MBench-project/)]
    [[leaderboard](https://huggingface.co/spaces/study-overflow/MBench_Leaderboard)]

- **[RoboMemArena: A Comprehensive and Challenging Robotic Memory Benchmark](https://arxiv.org/abs/2605.10921)**
    [[code](https://github.com/OpenHelix-Team/RoboMemArena)]
    [[data](https://huggingface.co/datasets/RoboMemArenaBenchmark/RoboMemArena)]
    [[proj](https://robomemarena.github.io/)]
    [[leaderboard](https://robomemarena.github.io/leaderboard.html)]

- **[DeepImageSearch: Benchmarking Multimodal Agents for Context-Aware Image Retrieval in Visual Histories](https://arxiv.org/abs/2602.10809)**
    [[code](https://github.com/RUC-NLPIR/DeepImageSearch)]
    [[data](https://huggingface.co/datasets/RUC-NLPIR/DISBench)]
    [[leaderboard](https://huggingface.co/spaces/RUC-NLPIR/DISBench-Leaderboard)]

- **[Persona-MME: A Benchmark for Long-Term Personalized Multimodal LLMs](https://arxiv.org/abs/2604.13074)**
    [[code](https://github.com/MiG-NJU/PersonaVLM)]
    [[data](https://huggingface.co/datasets/ClareNie/Persona-MME)]

#### 🗓️ 2025

-  **[TeleEgo: Benchmarking Egocentric AI Assistants in the Wild](https://arxiv.org/abs/2510.23981)** †
     [[code](https://github.com/TeleAI-UAGI/TeleEgo)]
     [[data](https://huggingface.co/datasets/David0219/TeleEgo)]
     [[proj](https://programmergg.github.io/jrliu.github.io/)]
     [[leaderboard](https://programmergg.github.io/jrliu.github.io/#leaderboard)]

-  **[LVBench: An Extreme Long Video Understanding Benchmark](https://arxiv.org/abs/2406.08035)**
     [[code](https://github.com/zai-org/LVBench)]

- **[Video-MME: The First-Ever Comprehensive Evaluation Benchmark of Multi-modal LLMs in Video Analysis](https://arxiv.org/abs/2405.21075v3)**
    [[code](https://github.com/MME-Benchmarks/Video-MME)]

#### 🗓️ 2024

-  **[MovieChat+: Question-aware Sparse Memory for Long Video Question Answering](https://arxiv.org/abs/2404.17176)**
     [[code](https://github.com/rese1f/MovieChat)]

-  **[CinePile: A Long Video Question Answering Dataset and Benchmark](https://arxiv.org/abs/2405.08813)**
     [[code](https://huggingface.co/datasets/tomg-group-umd/cinepile)]

-  **[LongVideoBench: A Benchmark for Long-Context Interleaved Video-Language Understanding](https://arxiv.org/abs/2407.15754)**
     [[code](https://github.com/longvideobench/LongVideoBench)]

#### 🗓️ 2023

- **[EgoSchema: A Diagnostic Benchmark for Very Long-form Video Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2023/file/90ce332aff156b910b002ce4e6880dec-Paper-Datasets_and_Benchmarks.pdf)**
    [[code](https://github.com/egoschema/egoschema)]

- [LvBench: A Benchmark for Long-form Video Understanding with Versatile Multi-modal Question Answering](https://arxiv.org/abs/2312.04817)

### 🎮 Dynamic Benchmarks & Simulation Environments

#### 🗓️ 2026

- **[Beyond Static Dialogues: Benchmarking Realistic, Heterogeneous, and Evolving Long-Term Memory](https://arxiv.org/abs/2605.31086)**
    [[code](https://github.com/microsoft/RHELM)]
    [[data](https://huggingface.co/datasets/microsoft/RHELM)]
    [[proj](https://microsoft.github.io/RHELM/)]

- **[AMemGym: Interactive Memory Benchmarking for Assistants in Long-Horizon Conversations](https://arxiv.org/abs/2603.01966)**
    [[code](https://github.com/AGI-Eval-Official/amemgym)]
    [[proj](https://agi-eval-official.github.io/amemgym/)]

- [StreamMemBench: Streaming Evaluation of Agent Memory for Future-Oriented Assistance](https://arxiv.org/abs/2606.14571)

#### 🗓️ 2025

- **[MemoryBench: A Benchmark for Memory and Continual Learning in LLM Systems](https://arxiv.org/abs/2510.17281)**
    [[code](https://github.com/LittleDinoC/MemoryBench)]
    [[data](https://huggingface.co/datasets/THUIR/MemoryBench)]

- **[ARE: Scaling Up Agent Environments and Evaluations](https://arxiv.org/abs/2509.17158)** 
    (The Gaia2 Paper)
    [[code](https://github.com/facebookresearch/meta-agents-research-environments)]

#### 🗓️ 2024

- **[AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents](https://arxiv.org/abs/2407.18901)**
    [[code](https://github.com/StonyBrookNLP/appworld)]

---

## 🔤 Papers - Nonparametric Memory

### 📝 Text Memory

#### 🗓️ 2026

- **[Memory Efficiency and Resource-Rational Encoding in Sentence Processing](https://aclanthology.org/2026.acl-long.1550/)**
    [[code](https://github.com/weijiexu-charlie/resource-rational-encoding)]

- **[AutoMem: Automated Learning of Memory as a Cognitive Skill](https://arxiv.org/abs/2607.01224)**
    [[code](https://github.com/autoLearnMem/AutoMem)]
    [[proj](https://autolearnmem.github.io/)]

- **[Mandol: An Agglomerative Agent Memory System for Long-Term Conversations](https://arxiv.org/abs/2606.29778)**
    [[code](https://github.com/AgentCombo/Mandol)]

- **[RecMem: Recurrence-based Memory Consolidation for Efficient and Effective Long-Running LLM Agents](https://arxiv.org/abs/2605.16045)**
    [[code](https://github.com/CaiusDai/RecMem)]

- **[Evoking User Memory: Personalizing LLM via Recollection-Familiarity Adaptive Retrieval](https://arxiv.org/abs/2603.09250)** (RF-Mem)
    [[code](https://github.com/Applied-Machine-Learning-Lab/ICLR2026_RF-Mem)]

- **[MemPrivacy: Privacy-Preserving Personalized Memory Management for Edge-Cloud Agents](https://arxiv.org/abs/2605.09530)**
    [[code](https://github.com/MemTensor/MemPrivacy)]

- **[Beyond RAG for Agent Memory: Retrieval by Decoupling and Aggregation](https://arxiv.org/abs/2602.02007)**
    [[code](https://github.com/HU-xiaobai/xMemory)]

- **[MemSearch-o1: Empowering Large Language Models with Reasoning-Aligned Memory Growth in Agentic Search](https://arxiv.org/abs/2604.17265)**
    [[code](https://github.com/Applied-Machine-Learning-Lab/ACL2026_MemSearch-o1)]

- **[SimpleMem: Efficient Lifelong Memory for LLM Agents](https://arxiv.org/abs/2601.02553)**
    [[code](https://github.com/aiming-lab/SimpleMem)]

- **[Beyond Similarity Search: Tenure and the Case for Structured Belief State in LLM Memory](https://arxiv.org/abs/2605.11325)**
    [[code](https://github.com/jeffreyflynt/tenure)]

- [MemCompiler: Compile, Don't Inject -- State-Conditioned Memory for Embodied Agents](https://arxiv.org/abs/2605.07594)

#### 🗓️ 2025

- **[LightMem: Lightweight and Efficient Memory-Augmented Generation](https://arxiv.org/abs/2510.18866)**
   [[code](https://github.com/zjunlp/LightMem)]

- **[What Deserves Memory: Adaptive Memory Distillation for LLM Agents](https://arxiv.org/abs/2508.03341)**
    [[code](https://github.com/nemori-ai/nemori)]

- **[Human-inspired Episodic Memory for Infinite Context LLMs](https://arxiv.org/abs/2407.09450)**
    [[code](https://github.com/em-llm/EM-LLM-model)]

- **[MemWeaver: A Hierarchical Memory from Textual Interactive Behaviors for Personalized Generation](https://arxiv.org/abs/2510.07713)**
    [[code](https://github.com/fishsure/MemWeaver)]

- [Evaluating Long-Term Memory for Long-Context Question Answering](https://arxiv.org/abs/2510.23730)

- [Text2Mem: A Unified Memory Operation Language for Memory Operating System](https://arxiv.org/abs/2509.11145)

- [O-Mem: Omni Memory System for Personalized, Long Horizon, Self-Evolving Agents](https://arxiv.org/abs/2511.13593)

- [Omne-R1: Learning to Reason with Memory for Multi-hop Question Answering](https://arxiv.org/abs/2508.17330)

- [In Prospect and Retrospect: Reflective Memory Management for Long-term Personalized Dialogue Agents](https://aclanthology.org/2025.acl-long.413/)

- [SEDM: Scalable Self-Evolving Distributed Memory for Agents](https://arxiv.org/abs/2509.09498)

- [MemoRAG: Boosting Long Context Processing with Global Memory-Enhanced Retrieval Augmentation](https://arxiv.org/abs/2409.05591)

- [Towards LifeSpan Cognitive Systems](https://arxiv.org/abs/2409.13265)

#### 🗓️ 2024

- **[Compress to Impress: Unleashing the Potential of Compressive Memory in Real-World Long-Term Conversations](https://arxiv.org/abs/2402.11975)**
    [[code](https://github.com/nuochenpku/COMEDY)]

- **[Agent Workflow Memory](https://arxiv.org/abs/2409.07429)**
    [[code](https://github.com/zorazrw/agent-workflow-memory)]

- **[MemoryBank: Enhancing Large Language Models with Long-Term Memory](https://arxiv.org/abs/2305.10250)**
    (AAAI 2024)
    [[code](https://github.com/zhongwanjun/MemoryBank-SiliconFriend)]

- **[Toward Conversational Agents with Context and Time Sensitive Long-term Memory](https://arxiv.org/abs/2406.00057)**
    [[data](https://github.com/Zyphra/TemporalMemoryDataset)]

- [InfLLM: Training-Free Long-Context Extrapolation for LLMs with an Efficient Context Memory](https://arxiv.org/abs/2402.04617)

#### 🗓️ 2023

- [RET-LLM: Towards a General Read-Write Memory for Large Language Models](https://arxiv.org/abs/2305.14322)

### 🌐 Graph Memory

#### 🗓️ 2026

- **[GraphPlanner: Graph Memory-Augmented Agentic Routing for Multi-Agent LLMs](https://arxiv.org/abs/2604.23626)**
    [[code](https://github.com/ulab-uiuc/GraphPlanner)]

- **[HyperMem: Hypergraph Memory for Long-Term Conversations](https://arxiv.org/abs/2604.08256)**
    [[code](https://github.com/EverMind-AI/EverOS)]

- **[Mnemis: Dual-Route Retrieval on Hierarchical Graphs for Long-Term LLM Memory](https://arxiv.org/abs/2602.15313)**
    [[code](https://github.com/microsoft/Mnemis)]

- **[MAGMA: A Multi-Graph based Agentic Memory Architecture for AI Agents](https://arxiv.org/abs/2601.03236)**
    [[code](https://github.com/FredJiang0324/MAMGA)]

- **[TraceMem: Weaving Narrative Memory Schemata from User Conversational Traces](https://arxiv.org/abs/2602.09712)**
    [[code](https://github.com/YimingShu-teay/TraceMem)]
  
- **[PlugMem: A Task-Agnostic Plugin Memory Module for LLM Agents](https://arxiv.org/abs/2603.03296)**
    [[code](https://github.com/TIMAN-group/PlugMem)]

- [SAGE: A Self-Evolving Agentic Graph-Memory Engine for Structure-Aware Associative Memory](https://arxiv.org/abs/2605.12061)

#### 🗓️ 2025

- **[From RAG to Memory: Non-Parametric Continual Learning for Large Language Models](https://arxiv.org/abs/2502.14802)**
    [[code](https://github.com/OSU-NLP-Group/HippoRAG)]

- **[MIRIX: Multi-Agent Memory System for LLM-Based Agents](https://arxiv.org/abs/2507.07957)**
    [[code](https://github.com/Mirix-AI/MIRIX)]

- **[From Single to Multi-Granularity: Toward Long-Term Memory Association and Selection of Conversational Agents](https://arxiv.org/abs/2505.19549)** (MemGAS)
    [[code](https://github.com/quqxui/MemGAS)]

- **[Hierarchical Memory Organization for Wikipedia Generation](https://aclanthology.org/2025.acl-long.1423/)**
    [[code](https://github.com/eugeneyujunhao/mog)]

- [From Experience to Strategy: Empowering LLM Agents with Trainable Graph Memory](https://www.arxiv.org/abs/2511.07800)

- [Bridging Intuitive Associations and Deliberate Recall: Empowering LLM Personal Assistant with Graph-Structured Long-term Memory](https://aclanthology.org/2025.findings-acl.901/)

- [HiAgent: Hierarchical Working Memory Management for Solving Long-Horizon Agent Tasks with Large Language Model](https://aclanthology.org/2025.acl-long.1575/)

- [Optimizing the Interface Between Knowledge Graphs and LLMs for Complex Reasoning](https://arxiv.org/abs/2505.24478)

#### 🗓️ 2024

- **[HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models](https://arxiv.org/abs/2405.14831)**
    [[code](https://github.com/OSU-NLP-Group/HippoRAG)]

- **[AriGraph: Learning Knowledge Graph World Models with Episodic Memory for LLM Agents](https://arxiv.org/abs/2407.04363)**
    [[code](https://github.com/AIRI-Institute/AriGraph)]

### 🎥 Multimodal Memory (for Understanding)

#### 🗓️ 2026

- **[MemGUI-Agent: An End-to-End Long-Horizon Mobile GUI Agent with Proactive Context Management](https://arxiv.org/abs/2606.19926)**
    [[code](https://github.com/kwai/MemGUI-Agent)]
    [[proj](https://memgui-agent.github.io/)]

- **[FluxMem: Adaptive Hierarchical Memory for Streaming Video Understanding](https://arxiv.org/abs/2603.02096)**
    [[code](https://github.com/YiwengXie/FluxMem)]
    [[proj](https://yiwengxie.com/FluxMem/)]

- **[SE-GA: Memory-Augmented Self-Evolution for GUI Agents](https://arxiv.org/abs/2605.16883)**
    [[code](https://github.com/jinshilong-dev/SE-GA)]

- **[Visual Agentic Memory: Enabling Online Long Video Understanding via Online Indexing, Hierarchical Memory, and Agentic Retrieval](https://arxiv.org/abs/2605.16481)**
    [[code](https://github.com/yiliu-li/Visual-Agentic-Memory)]

- **[PersonaVLM: Long-Term Personalized Multimodal LLMs](https://arxiv.org/abs/2604.13074)**
    [[code](https://github.com/MiG-NJU/PersonaVLM)]
    [[proj](https://PersonaVLM.github.io)]

- **[Omni-SimpleMem: Autoresearch-Guided Discovery of Lifelong Multimodal Agent Memory](https://arxiv.org/abs/2604.01007)**
    [[code](https://github.com/aiming-lab/SimpleMem)]

- **[HERMES: KV Cache as Hierarchical Memory for Efficient Streaming Video Understanding](https://arxiv.org/abs/2601.14724)**
    [[code](https://github.com/haowei-freesky/HERMES)]

- **[EventMemAgent: Hierarchical Event-Centric Memory for Online Video Understanding with Adaptive Tool Use](https://arxiv.org/abs/2602.15329)**
    [[code](https://github.com/lingcco/EventMemAgent)]

- **[M2A: Multimodal Memory Agent with Dual-Layer Hybrid Memory for Long-Term Personalized Interactions](https://arxiv.org/abs/2602.07624)**
    [[code](https://github.com/Little-Fridge/M2A)]

#### 🗓️ 2025

- **[WorldMM: Dynamic Multimodal Memory Agent for Long Video Reasoning](https://arxiv.org/abs/2512.02425)**
    [[code](https://github.com/wgcyeo/WorldMM)]

- **[MemVerse: Multimodal Memory for Lifelong Learning Agents](https://arxiv.org/abs/2512.03627)**
    [[code](https://github.com/KnowledgeXLab/MemVerse)]

- **[MGA: Memory-Driven GUI Agent for Observation-Centric Interaction](https://arxiv.org/abs/2510.24168)**
    [[code](https://github.com/MintyCo0kie/MGA4OSWorld)]

- **[Seeing, Listening, Remembering, and Reasoning: A Multimodal Agent with Long-Term Memory](https://arxiv.org/abs/2508.09736)**
    [[code](https://github.com/bytedance-seed/m3-agent)]

- **[HippoMM: Hippocampal-inspired Multimodal Memory for Long Audiovisual Event Understanding](https://arxiv.org/abs/2504.10739)**
    [[code](https://github.com/linyueqian/HippoMM)]

- [Infinite Video Understanding](https://www.arxiv.org/abs/2507.09068)

- [Episodic Memory Representation for Long-form Video Understanding](https://arxiv.org/abs/2508.09486)

- [Multi-RAG: A Multimodal Retrieval-Augmented Generation System for Adaptive Video Understanding](https://arxiv.org/abs/2505.23990)

- [Contextual Experience Replay for Self-Improvement of Language Agents](https://arxiv.org/abs/2506.06698)

#### 🗓️ 2024

- **[VideoAgent: Long-form Video Understanding with Large Language Model as Agent](https://arxiv.org/abs/2403.10517)**
    [[code](https://github.com/HKUDS/VideoAgent)]

- **[VideoChat-Flash: Hierarchical Compression for Long-Context Video Modeling](https://arxiv.org/abs/2501.00574)**
    [[code](https://github.com/OpenGVLab/VideoChat-Flash)]

- **[LongVLM: Efficient Long Video Understanding via Large Language Models](https://arxiv.org/abs/2404.03384)**
    [[code](https://github.com/ziplab/LongVLM)]

- **[KARMA: Augmenting Embodied AI Agents with Long-and-short Term Memory Systems](https://arxiv.org/abs/2409.14908)**
    [[code](https://github.com/WZX0Swarm0Robotics/KARMA/tree/master)]

### 🎥 Multimodal Memory (for Generation)

#### 🗓️ 2026

- **[MemSlides: A Hierarchical Memory Driven Agent Framework for Personalized Slide Generation with Multi-turn Local Revision](https://arxiv.org/abs/2606.17162)**
    [[code](https://github.com/huohua325/Memslides)]
    [[proj](https://memslides.github.io/)]

- **[LoGeR: Long-Context Geometric Reconstruction with Hybrid Memory](https://arxiv.org/abs/2603.03269)**
    [[code](https://github.com/Junyi42/LoGeR)]

- [OneStory: Coherent Multi-Shot Video Generation with Adaptive Memory](https://arxiv.org/abs/2512.07802)

#### 🗓️ 2025

- **[MagicWorld: Towards Long-Horizon Stability for Interactive Video World Exploration](https://arxiv.org/abs/2511.18886)**
    [[code](https://github.com/vivoCameraResearch/Magic-World)]

- **[Yume-1.5: A Text-Controlled Interactive World Generation Model](https://arxiv.org/abs/2512.22096)**
    [[code](https://github.com/stdstu12/YUME)]

- **[StoryMem: Multi-shot Long Video Storytelling with Memory](https://arxiv.org/abs/2512.19539)**
    [[code](https://github.com/Kevin-thu/StoryMem)]
  
- **[MemFlow: Flowing Adaptive Memory for Consistent and Efficient Long Video Narratives](https://arxiv.org/abs/2512.14699)**
    [[code](https://github.com/KlingTeam/MemFlow)]

- **[MotionRAG: Motion Retrieval-Augmented Image-to-Video Generation](http://arxiv.org/abs/2509.26391)**
    [[code](https://github.com/MCG-NJU/MotionRAG)]

- **[VideoRAG: Retrieval-Augmented Generation over Video Corpus](http://arxiv.org/abs/2501.05874)**
    [[code](https://github.com/starsuzi/VideoRAG)]
  
- [Pretraining Frame Preservation in Autoregressive Video Memory Compression](https://arxiv.org/abs/2512.23851)

- [EgoLCD: Egocentric Video Generation with Long Context Diffusion](https://arxiv.org/abs/2512.04515)

- [Pack and Force Your Memory: Long-form and Consistent Video Generation](http://arxiv.org/abs/2510.01784)

- [Video World Models with Long-term Spatial Memory](http://arxiv.org/abs/2506.05284)

- [Mixture of Contexts for Long Video Generation](http://arxiv.org/abs/2508.21058)

- [Context as Memory: Scene-Consistent Interactive Long Video Generation with Memory Retrieval](http://arxiv.org/abs/2506.03141)

## 🔢 Papers - Parametric Memory

#### 🗓️ 2026

- **[Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models](https://arxiv.org/abs/2601.07372)** 
    (The DeepSeek **Engram** Paper)
    [[code](https://github.com/deepseek-ai/Engram/)]
    + **[Beyond Conditional Computation: Retrieval-Augmented Genomic Foundation Models with Gengram](https://arxiv.org/abs/2601.22203)**
        [[code](https://github.com/zhejianglab/Gengram/)]
    + [Pooling Engram Conditional Memory in Large Language Models using CXL](https://arxiv.org/abs/2603.10087)
    + [A Collision-Free Hot-Tier Extension for Engram-Style Conditional Memory: A Controlled Study of Training Dynamics](https://arxiv.org/abs/2601.16531)

- **[δ-mem: Efficient Online Memory for Large Language Models](https://arxiv.org/abs/2605.12357)**
    [[code](https://github.com/MindLab-Research/delta-Mem)]

- **[Language Model Memory and Memory Models for Language](https://arxiv.org/abs/2602.13466)**
    [[code](https://github.com/blbadger/memorymodels)]

- **[MSA: Memory Sparse Attention for Efficient End-to-End Memory Model Scaling to 100M Tokens](https://github.com/EverMind-AI/MSA/blob/main/paper/MSA__Memory_Sparse_Attention_for_Efficient_End_to_End_Memory_Model_Scaling_to_100M_Tokens.pdf)**
    [[code](https://github.com/EverMind-AI/MSA)]
    
- **[GradMem: Learning to Write Context into Memory with Test-Time Gradient Descent](https://arxiv.org/abs/2603.13875)**
    [[code](https://github.com/yurakuratov/gradmem)]

- **[MeKi: Memory-based Expert Knowledge Injection for Efficient LLM Scaling](https://arxiv.org/abs/2602.03359)**
    [[code](https://github.com/ningding-o/MeKi)]

- **[STEM: Scaling Transformers with Embedding Modules](https://arxiv.org/abs/2601.10639)**
    [[code](https://github.com/Infini-AI-Lab/STEM)]

- **[MeMo: Memory as a Model](https://arxiv.org/abs/2605.15156)**
    [[code](https://github.com/arunv3rma/MeMo)]

- [Language Models Need Sleep: Learning to Self-Modify and Consolidate Memories](https://arxiv.org/abs/2606.03979)

- [Do Language Models Need Sleep? Offline Recurrence for Improved Online Inference](https://arxiv.org/abs/2605.26099)

- [Training Transformers for KV Cache Compressibility](https://arxiv.org/abs/2605.05971)

- [Contextual Agentic Memory is a Memo, Not True Memory](https://arxiv.org/abs/2604.27707)

- [Memory Caching: RNNs with Growing Memory](https://arxiv.org/abs/2602.24281)

- [Fast-weight Product Key Memory](https://arxiv.org/abs/2601.00671)

#### 🗓️ 2025

- **[MoM: Linear Sequence Modeling with Mixture-of-Memories](https://arxiv.org/abs/2502.13685)**
    [[code](https://github.com/OpenSparseLLMs/MoM)]

- **[MLP Memory: Language Modeling with Retriever-pretrained External Memory](https://arxiv.org/abs/2508.01832)**
    [[code](https://github.com/Rubin-Wei/MLPMemory)]

- **[Memory Decoder: A Pretrained, Plug-and-Play Memory for Large Language Models](https://www.arxiv.org/abs/2508.09874)**
    [[code](https://github.com/LUMIA-Group/MemoryDecoder)]

- [How Much Do Language Models Memorize?](https://arxiv.org/abs/2505.24832)

- [Memory Retrieval and Consolidation in Large Language Models through Function Tokens](https://arxiv.org/abs/2510.08203)

- [Nested Learning: The Illusion of Deep Learning Architectures](https://openreview.net/forum?id=nbMeRvNb7A)

- [Improving Factuality with Explicit Working Memory](https://arxiv.org/abs/2412.18069)
  
- [R<sup>3</sup>Mem: Bridging Memory Retention and Retrieval via Reversible Compression](https://arxiv.org/abs/2502.15957)

- [May the Memory Be With You: Efficient and Infinitely Updatable State for Large Language Models](https://dl.acm.org/doi/abs/10.1145/3721146.3721951)

- [MeMo: Towards Language Models with Associative Memory Mechanisms](https://aclanthology.org/2025.findings-acl.785/)

- [REFRAG: Rethinking RAG based Decoding](https://arxiv.org/abs/2509.01092)

- [EpMAN: Episodic Memory AttentioN for Generalizing to Longer Contexts](https://aclanthology.org/2025.acl-long.574/)

- [Disentangling Memory and Reasoning Ability in Large Language Models](https://aclanthology.org/2025.acl-long.84/)

#### 🗓️ 2024

- **[InfLLM: Training-Free Long-Context Extrapolation for LLMs with an Efficient Context Memory](https://arxiv.org/abs/2402.04617)**
    [[code](https://github.com/thunlp/InfLLM)]

- **[MA-LMM: Memory-Augmented Large Multimodal Model for Long-Term Video Understanding](https://arxiv.org/abs/2404.05726)**
    (CVPR 2024)
    [[code](https://github.com/boheumd/MA-LMM)]

- **[MemoryLLM: Towards Self-Updatable Large Language Models](https://arxiv.org/abs/2402.04624)**
    [[code](https://github.com/wangyu-ustc/MemoryLLM)]

- **[WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models](https://arxiv.org/abs/2405.14768)**
    [[code](https://github.com/zjunlp/EasyEdit)]

- [Titans: Learning to Memorize at Test Time](https://arxiv.org/abs/2501.00663)

- [Memory<sup>3</sup>: Language Modeling with Explicit Memory](https://arxiv.org/abs/2407.01178v1)
  
- [Infinite-LLM: Efficient LLM Service for Long Context with DistAttention and Distributed KVCache](https://arxiv.org/abs/2401.02669)

- [MemServe: Context Caching for Disaggregated LLM Serving with Elastic Memory Pool](https://arxiv.org/abs/2406.17565)

- [WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models](https://arxiv.org/abs/2405.14768/)

- [Ultra-Sparse Memory Network](https://arxiv.org/abs/2411.12364)

#### 🗓️ 2023

- **[Augmenting Language Models with Long-Term Memory](https://arxiv.org/abs/2306.07174)**
    [[code](https://github.com/Victorwz/LongMem)]

- **[Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180)**
    [[code](https://github.com/vllm-project/vllm)]

## 📈 Papers - Memory for Agent Evolution

### 🧭 Reinforcement Learning & Continual Learning 

#### 🗓️ 2026

- **[MLEvolve: A Self-Evolving Framework for Automated Machine Learning Algorithm Discovery](https://arxiv.org/abs/2606.06473)**
    [[code](https://github.com/InternScience/MLEvolve)]

- **[SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://arxiv.org/abs/2605.23904)**
    [[code](https://github.com/microsoft/SkillOpt)]

- **[Learning, Fast and Slow: Towards LLMs That Adapt Continually](https://arxiv.org/abs/2605.12484)**
    [[code](https://rishabhtiwari.ai/projects/fst/code/)]
    [[blog](https://gepa-ai.github.io/gepa/blog/2026/05/11/learning-fast-and-slow/)]

- **[CASCADE: Case-Based Continual Adaptation for Large Language Models During Deployment](https://arxiv.org/abs/2605.06702)**
    (The DTLBench Paper)
    [[code](https://github.com/guosyjlu/CASCADE)]

- **[Memory Intelligence Agent](https://arxiv.org/abs/2604.04503)**
    [[code](https://github.com/ECNU-SII/MIA)]

- **[PASK: Toward Intent-Aware Proactive Agents with Long-Term Memory](https://arxiv.org/abs/2604.08000)**
    [[code](https://github.com/xzf-thu/Pask)]

- **[Toward Autonomous Long-Horizon Engineering for ML Research](https://arxiv.org/abs/2604.13018)**
    [[code](https://github.com/AweAI-Team/AiScientist)]

- **[OpenClaw-RL: Train Any Agent Simply by Talking](https://arxiv.org/abs/2603.10165)**
    [[code](https://github.com/Gen-Verse/OpenClaw-RL)]

- **[Memento-Skills: Let Agents Design Agents](https://arxiv.org/abs/2603.18743)**
    [[code](https://github.com/Memento-Teams/Memento-Skills)]

- **[Memento 2: Learning by Stateful Reflective Memory](https://arxiv.org/abs/2512.22716)**
    [[code](https://github.com/Agent-on-the-Fly/Memento)]

- **[MemSkill: Learning and Evolving Memory Skills for Self-Evolving Agents](https://arxiv.org/abs/2602.02474)**
    [[code](https://github.com/ViktorAxelsen/MemSkill)]

- **[ProcMEM: Learning Reusable Procedural Memory from Experience via Non-Parametric PPO for LLM Agents](https://arxiv.org/abs/2602.01869)**
    [[code](https://github.com/Miracle1207/ProcMEM)]

- **[MemRL: Self-Evolving Agents via Runtime Reinforcement Learning on Episodic Memory](https://arxiv.org/abs/2601.03192)**
    [[code](https://github.com/MemTensor/MemRL)]

- [Self-Evolving Multi-Agent Systems via Decentralized Memory](https://arxiv.org/abs/2605.22721)

- [Meta-Cognitive Memory Policy Optimization for Long-Horizon LLM Agents](https://arxiv.org/abs/2605.30159)

- [MEMTIER: Tiered Memory Architecture and Retrieval Bottleneck Analysis for Long-Running Autonomous AI Agents](https://arxiv.org/abs/2605.03675)

- [Neural Garbage Collection: Learning to Forget while Learning to Reason](https://arxiv.org/abs/2604.18002)

- [Why the Brain Consolidates: Predictive Forgetting for Optimal Generalisation](https://arxiv.org/abs/2603.04688)

- [Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents](https://arxiv.org/abs/2601.01885)

#### 🗓️ 2025

- **[End-to-End Test-Time Training for Long Context](https://arxiv.org/abs/2512.23675)**
    [[code](https://github.com/test-time-training/e2e)]

- **[ML-Master: Towards AI-for-AI via Integration of Exploration and Reasoning](https://arxiv.org/abs/2506.16499)**
    [[code](https://github.com/sjtu-sai-agents/ML-Master)]
  
- **[MemEvolve: Meta-Evolution of Agent Memory Systems](https://arxiv.org/abs/2512.18746)**
    [[code](https://github.com/bingreeky/MemEvolve)]
  
- **[Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution](https://arxiv.org/abs/2512.10696)**
    [[code](https://github.com/agentscope-ai/ReMe)]

- **[EvolveR: Self-Evolving LLM Agents through an Experience-Driven Lifecycle](https://arxiv.org/abs/2510.16079)**
    [[code](https://github.com/KnowledgeXLab/EvolveR)]

- **[Learning on the Job: An Experience-Driven, Self-Evolving Agent for Long-Horizon Tasks](https://arxiv.org/abs/2510.08002)**
    [[code](https://github.com/KnowledgeXLab/MUSE)]

- **[Mem-α: Learning Memory Construction via Reinforcement Learning](https://arxiv.org/abs/2509.25911)**
    [[code](https://github.com/wangyu-ustc/Mem-alpha)]

- **[Memento: Fine-tuning LLM Agents without Fine-tuning LLMs](https://arxiv.org/abs/2508.16153)**
    [[code](https://github.com/Agent-on-the-Fly/Memento)]

- **[Goal-Directed Search Outperforms Goal-Agnostic Memory Compression in Long-Context Memory Tasks](https://arxiv.org/abs/2511.21726)**
    [[code](https://arxiv.org/abs/2511.21726)]

- **[General Agentic Memory via Deep Research](https://arxiv.org/abs/2511.18423)**
    [[code](https://github.com/VectorSpaceLab/general-agentic-memory/)]

- **[AgentEvolver: Towards Efficient Self-Evolving Agent System](https://arxiv.org/abs/2511.10395)**
    [[code](https://github.com/modelscope/AgentEvolver)]

- **[FLEX: Continuous Agent Evolution via Forward Learning from Experience](https://arxiv.org/abs/2511.06449)**
    [[code](https://github.com/GenSI-THUAIR/FLEX)]

- **[MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent](https://arxiv.org/abs/2507.02259)**
    [[code](https://github.com/BytedTsinghua-SIA/MemAgent)]

- [Beyond Heuristics: A Decision-Theoretic Framework for Agent Memory Management](https://arxiv.org/abs/2512.21567)

- [Nested Learning: The Illusion of Deep Learning Architecture](https://abehrouz.github.io/files/NL.pdf)
  [[blog](https://research.google/blog/introducing-nested-learning-a-new-ml-paradigm-for-continual-learning/)]
  
- [LightSearcher: Efficient DeepSearch via Experiential Memory](https://www.arxiv.org/abs/2512.06653)

- [Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning](https://arxiv.org/abs/2508.19828)
   
- [Latent Learning: Episodic Memory Complements Parametric Learning by Enabling Flexible Reuse of Experiences](https://arxiv.org/abs/2509.16189)

- [Evo-Memory: Benchmarking LLM Agent Test-time Learning with Self-Evolving Memory](https://arxiv.org/abs/2511.20857)

- [ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory](https://arxiv.org/abs/2509.25140)

- [Long Term Memory: The Foundation of AI Self-Evolution](https://arxiv.org/abs/2410.15665)

- [REFRAG: Rethinking RAG based Decoding](https://arxiv.org/abs/2509.01092)

- [MemGen: Weaving Generative Latent Memory for Self-Evolving Agents](https://arxiv.org/abs/2509.24704)

- [ReSum: Unlocking Long-Horizon Search Intelligence via Context Summarization](https://arxiv.org/abs/2509.13313)

- [MARC: Memory-Augmented RL Token Compression for Efficient Video Understanding](https://arxiv.org/pdf/2510.07915)

- [Continual Learning via Sparse Memory Finetuning](https://arxiv.org/abs/2510.15103)
  
- [Task-Core Memory Management and Consolidation for Long-term Continual Learning](https://arxiv.org/abs/2505.09952)

### 🧩 Context Engineering & Harness Engineering 

#### 🗓️ 2026

- **[Code as Agent Harness](https://arxiv.org/abs/2605.18747)**
    [[code](https://github.com/YennNing/Awesome-Code-as-Agent-Harness-Papers)]

- **[SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents](https://arxiv.org/abs/2601.16746)**
    [[code](https://github.com/Ayanami1314/swe-pruner)]

- **[LCM: Lossless Context Management](https://papers.voltropy.com/LCM)**
    [[code](https://github.com/Martian-Engineering/lossless-claw)]

- **[CL-bench: A Benchmark for Context Learning](https://arxiv.org/abs/2602.03587)**
    [[code](https://github.com/Tencent-Hunyuan/CL-bench)]

- [Is Grep All You Need? How Agent Harnesses Reshape Agentic Search](https://arxiv.org/abs/2605.15184)

- [M\*: Every Task Deserves Its Own Memory Harness](https://arxiv.org/abs/2604.11811)

#### 🗓️ 2025

- **[Everything is Context: Agentic File System Abstraction for Context Engineering](https://arxiv.org/abs/2512.05470)**
    [[code](https://github.com/AIGNE-io/aigne-framework)]

- **[AgentFold: Long-Horizon Web Agents with Proactive Context Management](https://arxiv.org/abs/2510.24699)**
    [[code](https://github.com/Alibaba-NLP/DeepResearch)]

- **[ACON: Optimizing Context Compression for Long-horizon LLM Agents](https://arxiv.org/abs/2510.00615)**
    [[code](https://github.com/microsoft/acon)]

- [Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models](https://arxiv.org/abs/2510.04618)

## 🔬 Papers - Memory in Cognitive Science

#### 🗓️ 2026

- [Subspace Communication in the Hippocampal–Retrosplenial Axis](https://www.nature.com/articles/s41586-026-10481-z)

- [A Neural State Space for Episodic Memories](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(25)00284-0)

- [Dopaminergic Processes Predict Temporal Distortions in Event Memory](https://www.nature.com/articles/s41467-026-69950-8)

- [Awareness as the Heart of Working Memory](https://www.sciencedirect.com/science/article/pii/S1364661326000756)

- [Neural Activations and Representations during Episodic versus Semantic Memory Retrieval](https://www.nature.com/articles/s41562-025-02390-4)

- [Distinct Neuronal Populations in the Human Brain Combine Content and Context](https://www.nature.com/articles/s41586-025-09910-2)

#### 🗓️ 2025

- [Neural Population Activity for Memory: Properties, Computations, and Codes](https://www.cell.com/neuron/fulltext/S0896-6273(25)00854-2)

- [How Prediction Error Drives Memory Updating: Role of Locus Coeruleus–Hippocampal Interactions](https://www.cell.com/trends/neurosciences/abstract/S0166-2236(25)00189-4)

- [Towards Large Language Models with Human-Like Episodic Memory](https://www.cell.com/trends/cognitive-sciences/abstract/S1364-6613(25)00179-2)

---

## 🔒 Memory Security & Defense

- **[Agent Memory Guard](https://owasp.org/www-project-agent-memory-guard/)**
    [[code](https://github.com/OWASP/www-project-agent-memory-guard)]
    [[pypi](https://pypi.org/project/agent-memory-guard/)]
    _OWASP runtime defense layer that screens agent memory writes for poisoning before they reach the agent — multi-layer validation with semantic anomaly detection, entropy scoring, provenance verification, and cross-reference and temporal checks._

- [From Untrusted Input to Trusted Memory: A Systematic Study of Memory Poisoning Attacks in LLM Agents](https://arxiv.org/abs/2606.04329)
    (The MPBench Paper)

- **[mnemo poisoning probes](https://github.com/DanceNitra/agora/tree/main/mnemo/probes)**
    [[attack](https://github.com/DanceNitra/agora/blob/main/mnemo/probes/memory_defense_layer_probe.py)]
    [[defense](https://github.com/DanceNitra/agora/blob/main/mnemo/probes/memory_gate_defense_probe.py)]
    _Runnable probe scripts demonstrating that provenance written into a memory record is forgeable, and that a retrieval-time corroboration gate raises the cost of memory-poisoning attacks._

---

## 📰 Articles

#### 🗓️ 2026

- [Why Character.AI Forgets You — And What Persistent Memory Actually Requires](https://blog.kinthai.ai/why-character-ai-forgets-you-persistent-memory-architecture)

- [221 Agents: Multi-Agent Coordination Lessons](https://blog.kinthai.ai/221-agents-multi-agent-coordination-lessons)

- [OpenClaw Multi-Tenancy: Why VM-Per-User Does Not Scale](https://blog.kinthai.ai/openclaw-multi-tenancy-why-vm-per-user-doesnt-scale)

#### 🗓️ 2025

- [Survey of AI Agent Memory Frameworks](https://www.graphlit.com/blog/survey-of-ai-agent-memory-frameworks)

#### 🗓️ 2024

- [Memory in Language Model-Enabled Agents](https://yuweisunn.github.io/blog-1-06-24.html)

- [Mastering LLM Memory: A Comprehensive Guide](https://www.strongly.ai/blog/mastering-llm-memory-a-comprehensive-guide.html)

#### 🗓️ 2023

- [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/)

---

## 👥 Workshops

#### 🗓️ 2026

- [ICLR 2026](https://iclr.cc/Conferences/2026): [Workshop on Memory for LLM-Based Agentic Systems (MemAgents)](https://sites.google.com/view/memagent-iclr26/)
  [[schedule](https://sites.google.com/view/memagent-iclr26/schedule)]

#### 🗓️ 2025

- [ACL 2025](https://2025.aclweb.org/): [The First Workshop on Large Language Model Memorization (L2M2)](https://sites.google.com/view/memorization-workshop)
  [[proceedings](https://aclanthology.org/volumes/2025.l2m2-1/)]

---

## 📑 Citation

To cite this collection itself, use the metadata in [`CITATION.cff`](CITATION.cff) (GitHub's "Cite this repository" button), or:

```bibtex
@misc{zhang2025awesomeagentmemory,
        author = {Zhang, Dell and Sun, Changzhi and Luo, Jixiang and Chen, Xiangyu and Li, Xuelong},
        title = {Awesome Agent Memory: Curated Systems, Benchmarks, and Papers on Memory for {LLMs}/{MLLMs}},
        year = {2025},
        howpublished = {\url{https://github.com/TeleAI-UAGI/Awesome-Agent-Memory}}
}
```

This list grew out of the maintainers' SIGIR-AP 2025 tutorial, which you can cite as the related publication:

```bibtex
@inproceedings{zhangConversationalAgentsRAG2025,
        author = {Zhang, Dell and Feng, Yue and Liu, Haiming and Sun, Changzhi and Luo, Jixiang and Chen, Xiangyu and Li, Xuelong},
        title = {Conversational Agents: From {RAG} to {LTM}},
        year = {2025},
        isbn = {9798400722189},
        doi = {10.1145/3767695.3769671},
        booktitle = {Proceedings of the 2025 Annual International ACM SIGIR Conference on Research and Development in Information Retrieval in the Asia Pacific Region (SIGIR-AP)},
        pages = {447–452},
        location = {China}
}
```

---

## Star History

[![Star History Chart](https://api.star-history.com/chart?repos=TeleAI-UAGI/Awesome-Agent-Memory&type=date&legend=bottom-right&sealed_token=HndhpfcgmQQTZzykPTJnhTRiM7VTBcvQ8x1cmjkLDjqmPAXnhQlj8KJCwGZQDy3FL90JNnLOlvRMZ0S2RmzOE1p-Q-mot3_dvaxkvM_7mznGaYL9KoDkVYPs5gWv8Ga8Qw9-7USKNYYp_VHvjPloysMz_0Q9DZiL0UGs0d2LK26AaMRfGygbYU9nG85O)](https://www.star-history.com/?repos=TeleAI-UAGI%2FAwesome-Agent-Memory&type=date&legend=bottom-right)

---

<div align="center">

**If you find this page helpful, please give it a ⭐️ — starring also keeps updates in your GitHub feed.**

Made with ❤️ by [Bloo-Mind AI Ltd](https://www.bloo-mind.ai/) and the Ubiquitous AGI team at TeleAI.

</div>

<div align="center" style="margin-top: 10px;">
    <a href="https://www.bloo-mind.ai/"><img src="assets/bloo-mind.png" alt="Bloo-Mind Logo" width="120px" /></a>
    &nbsp;&nbsp;&nbsp;
    <img src="assets/TeleAI.png" alt="TeleAI Logo" width="120px" />
</div> 
