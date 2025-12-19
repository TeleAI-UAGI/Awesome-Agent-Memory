<a name="readme-top"></a>

<h1 align="center">🧠 Awesome Agent Memory</h1>

<p align="center">
    A curated collection of systems, benchmarks, and papers et. on memory mechanisms for Large Language Models (LLMs) and Multimodal Large Language Models (MLLMs), exploring how different approaches enable long-term context, retrieval, and efficient reasoning.
</p>

<p align="center">
   👀 <b>Open-source</b> resources (e.g. papers with reproducible code publicly available on Github) are marked in bold font and ranked higher.
</p>

<details open>
  <summary>🗂️ Table of Contents</summary>
  <ul>
    <li><a href="#-products">💿 Products</a></li>
    <li><a href="#-tutorials">📖 Tutorials</a></li>
    <li><a href="#-surveys">📚 Surveys</a></li>
    <li><a href="#-benchmarks">📏 Benchmarks</a></li>
    <ul>
        <li><a href="#-plain-text-benchmarks">💬 Plain-Text Benchmarks</a></li>
        <li><a href="#-multimodal-benchmarks">🎬 Multimodal Benchmarks</a></li>
    </ul>
    <li><a href="#-papers---nonparametric-memory">🔤 Papers - Nonparameteric Memory</a></li>
    <ul>
        <li><a href="#-text-memory">📝 Text Memory</a></li>
        <li><a href="#-graph-memory">🌐 Graph Memory</a></li>
        <li><a href="#-multimodal-memory-for-understanding">🎥 Multimodal Memory (for Understanding)</a></li>
        <li><a href="#-multimodal-memory-for-generation">🎥 Multimodal Memory (for Generation)</a></li>
    </ul>
    <li><a href="#-papers---parameteric-memory">🔢 Papers - Parameteric Memory</a></li>
    <li><a href="#-papers---memory-for-agent-evolution">📈 Papers - Memory for Agent Evolution</a></li>
    <ul>
        <li><a href="#-reinforcement-learning--continual-learning">🧭 Reinforcement Learning & Continual Learning</a></li>
        <li><a href="#-context-engineering">🧩 Context Engineering</a></li>
    </ul>
    <li><a href="#-papers---memory-in-cognitive-science">🔬 Papers - Memory in Cognitive Science</a></li>      
    <li><a href="#-articles">📰 Articles</a></li>
    <li><a href="#-workshops">👥 Workshops</a></li>
  </ul>
</details>

<div align="left">
    
**If you find this project helpful, please give us a ⭐️ on GitHub for the latest update.**

</div>

---

## 💿 Products

### Open-Source

_Ordered by the number of Github stars._

1. **[Mem0](https://mem0.ai/)**
   [[code](https://github.com/mem0ai/mem0)]
   [[paper](https://arxiv.org/abs/2504.19413)]
   [[blog](https://get.mem.ai/blog)]

2. **[Zep (powered by Graphiti)](https://www.getzep.com/)**
   [[code](https://github.com/getzep/graphiti)]
   [[paper](https://arxiv.org/abs/2501.13956)]
   [[blog](https://blog.getzep.com/)]

3. **[Letta (formerly MemGPT)](https://www.letta.com/)**
   [[code](https://github.com/letta-ai/letta)]
   [[paper](https://arxiv.org/abs/2310.08560)]
   [[research](https://www.letta.com/research)]
   [[blog](https://www.letta.com/blog)]

4. **[Second Me](https://home.second.me/)**
   [[code](https://github.com/mindverse/Second-Me)]
   [[paper](https://arxiv.org/abs/2503.08102)]

5. **[Congee](https://www.cognee.ai/)**
   [[code](https://github.com/topoteretes/cognee)]
   [[paper](https://arxiv.org/abs/2505.24478)]
   [[blog](https://www.cognee.ai/blog)]

6. **[Claude-Mem (A Plug-in for Claude-Code)](https://claude-mem.ai/)**
   [[code](https://github.com/thedotmack/claude-mem)]

7. **[MIRIX](https://mirix.io/)**
   [[code](https://github.com/Mirix-AI/MIRIX)]
   [[paper](https://arxiv.org/abs/2507.07957)]
   [[blog](https://mirix.io/blog)]

8. **[MemOS](https://memos.openmem.net/)** 
   [[code](https://github.com/MemTensor/MemOS)]
   [[paper](https://arxiv.org/abs/2507.03724)]
   [[blog](https://supermemory.ai/blog)]
   
9. **[MemU](https://memu.pro/)**
   [[code](https://github.com/NevaMind-AI/memU)]
   [[blog](https://memu.pro/blog)]

10. **[OpenMemory](https://openmemory.cavira.app/)**
    [[code](https://github.com/caviraoss/openmemory)]

11. **[MemMachine](https://memmachine.ai/)**
    [[code](https://github.com/MemMachine/MemMachine)]
    [[blog](https://memmachine.ai/blog/)]

12. **[Memobase](https://memobase.io/)**
   [[code](https://github.com/memodb-io/memobase)]
   [[blog](https://www.memobase.io/blog)]

13. **[EverMemOS (part of EverMind)](https://evermind-ai.com/)**
    [[code](https://github.com/EverMind-AI/EverMemOS/)]
    [[blog](https://evermind-ai.com/blog/)]

14. **[LangMem (part of LangChain-LangGraph)](https://langchain-ai.github.io/langmem/)**
    [[code](https://github.com/langchain-ai/langmem)]
    [[blog](https://blog.langchain.com/)]

15. **[Hindsight](https://hindsight.vectorize.io/)**
    [[code](https://github.com/vectorize-io/hindsight)]
    [[paper](https://arxiv.org/abs/2512.12818)]

16. **[TeleMem](https://github.com/TeleAI-UAGI/TeleMem)**
      [[code](https://github.com/TeleAI-UAGI/TeleMem)] 
      🆕 _Newly released. Rising star. Tech-Report will be on arXiv soon. Stay tuned!_ 😜

### Closed-Source

1. [Supermemory](https://supermemory.ai/)
   [[partial-code](https://github.com/supermemoryai/supermemory)]
   [[blog](https://supermemory.ai/blog)]

2. [Memories.ai](https://memories.ai/)
   [[research](https://memories.ai/research)]
   [[paper](https://memories.ai/research/Camera)]
   [[blog](https://memories.ai/blogs)]

3. [Mem 2.0](https://get.mem.ai/)
   [[blog](https://get.mem.ai/blog)]

4. [Macaron Mind Lab](https://macaron.im/mindlab)
   [[blog](https://macaron.im/mindlab/research)]
   
5. [TwinMind](https://twinmind.com/)

6. [Readbear AI](https://www.redbearai.com/memoryScience)

### Archival (Inactive)

1. [Memvid](https://www.memvid.com/)
   [[code](https://github.com/Olow304/memvid)]
   [[critique1](https://github.com/Olow304/memvid/issues/63),[critique2](https://github.com/Olow304/memvid/issues/49)]

2. [Memary](https://kingjulio8238.github.io/memarydocs/)
   [[code](https://github.com/kingjulio8238/memary)]

## 📖 Tutorials

#### 🗓️ 2025

 - **[ACM SIGIR-AP 2025](https://www.sigir-ap.org/sigir-ap-2025/) Tutorial: [Conversational Agents: From RAG to LTM](https://sites.google.com/view/ltm-tutorial)**
     [[paper](https://dl.acm.org/doi/10.1145/3767695.3769671)]
     [[code](https://github.com/TeleAI-UAGI/Awesome-Agent-Memory)]
 
 - Daily Dose of DS: A Practical Deep Dive Into Memory Optimization for Agentic Systems
     [[Part-A](https://www.dailydoseofds.com/ai-agents-crash-course-part-15-with-implementation/)]
     [[Part-B](https://www.dailydoseofds.com/ai-agents-crash-course-part-16-with-implementation/)]
     [[Part-C](https://www.dailydoseofds.com/ai-agents-crash-course-part-17-with-implementation/)]

## 📚 Surveys

#### 🗓️ 2025

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

## 📏 Benchmarks

### 💬 Plain-Text Benchmarks

#### 🗓️ 2025

- **[Beyond a Million Tokens: Benchmarking and Enhancing Long-Term Memory in LLMs](https://arxiv.org/abs/2510.27246)** (The BEAM Paper)
    [[code](https://github.com/mohammadtavakoli78/BEAM)]
    [[data](https://huggingface.co/datasets/Mohammadta/BEAM)]
  
- **[MOOM: Maintenance, Organization and Optimization of Memory in Ultra-Long Role-Playing Dialogues](https://arxiv.org/abs/2509.11860)** (The ZH-4O Paper)
    [[code](https://github.com/cows21/MOOM-Roleplay-Dialogue)]
    [[data](https://github.com/cows21/MOOM-Roleplay-Dialogue/tree/main/data)]

- **[Know Me, Respond to Me: Benchmarking LLMs for Dynamic User Profiling and Personalized Responses at Scale](https://arxiv.org/abs/2504.14225)** (The PersonaMem and ImplicitPersona Paper)
    [[code](https://github.com/bowen-upenn/PersonaMem)]
    [[data11](https://huggingface.co/datasets/bowen-upenn/PersonaMem)]
    [[data2](https://huggingface.co/datasets/bowen-upenn/ImplicitPersona)]
  
- **[NoLiMa: Long-Context Evaluation Beyond Literal Matching](https://arxiv.org/abs/2502.05167)**
    [[code](https://github.com/adobe-research/NoLiMa)]
    [[data](https://github.com/adobe-research/NoLiMa/tree/main/data)]

- **[MemoryBench: A Benchmark for Memory and Continual Learning in LLM Systems](https://arxiv.org/abs/2510.17281)**
   [[code](https://github.com/LittleDinoC/MemoryBench)]
   [[data](https://huggingface.co/datasets/THUIR/MemoryBench)]

- **[HaluMem: Evaluating Hallucinations in Memory Systems of Agents](http://arxiv.org/abs/2511.03506)**
   [[code](https://github.com/MemTensor/HaluMem)]
   [[data](https://huggingface.co/datasets/IAAR-Shanghai/HaluMem)]

- **[LongBench v2: Towards Deeper Understanding and Reasoning on Realistic Long-context Multitasks](https://arxiv.org/abs/2412.15204)**
   [[data](https://github.com/THUDM/LongBench)]

- **[Minerva: A Programmable Memory Test Benchmark for Language Models](https://arxiv.org/abs/2502.03358)**
    [[code](https://github.com/microsoft/minerva_memory_test)]

- **[MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents](https://arxiv.org/abs/2506.21605)**
   [[code](https://github.com/import-myself/Membench)]

- [Evo-Memory: Benchmarking LLM Agent Test-time Learning with Self-Evolving Memory](https://arxiv.org/abs/2511.20857)

- [OdysseyBench: Evaluating LLM Agents on Long-Horizon Complex Office Application Workflows](https://arxiv.org/abs/2508.09124)
   
#### 🗓️ 2024

- **[LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](https://arxiv.org/abs/2410.10813)**
   [[data](https://github.com/xiaowu0162/LongMemEval)]
   
- **[Evaluating Very Long-Term Conversational Memory of LLM Agents](https://arxiv.org/abs/2402.17753)** (The LoCoMo Paper)
    [[code](https://github.com/snap-research/LoCoMo)]
    [[data](https://github.com/snap-research/locomo/tree/main/data)]

- **[∞Bench: Extending Long Context Evaluation Beyond 100K Tokens](https://arxiv.org/abs/2402.13718v3)**
    [[code](https://github.com/OpenBMB/InfiniteBench)]

- **[LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding](https://arxiv.org/abs/2308.14508)**
    [[code](https://github.com/THUDM/LongBench/blob/main/LongBench/README.md)]

#### 🗓️ 2023
-  **[Storybench: A multifaceted benchmark for continuous story visualization ](https://proceedings.neurips.cc/paper_files/paper/2023/hash/f63f5fbed1a4ef08c857c5f377b5d33a-Abstract-Datasets_and_Benchmarks.html)**
   [[code](https://github.com/google/storybench)]

### 🎬 Multimodal Benchmarks

#### 🗓️ 2025

-  **[TeleEgo: Benchmarking Egocentric AI Assistants in the Wild](https://arxiv.org/abs/2510.23981)**
    [[code](https://github.com/TeleAI-UAGI/TeleEgo)] [[proj](https://programmergg.github.io/jrliu.github.io/)]

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

## 🔤 Papers - Nonparametric Memory

### 📝 Text Memory

#### 🗓️ 2025

- **[LightMem: Lightweight and Efficient Memory-Augmented Generation](https://arxiv.org/abs/2510.18866)**
   [[code](https://github.com/zjunlp/LightMem)]

- **[Nemori: Self-Organizing Agent Memory Inspired by Cognitive Science](https://arxiv.org/abs/2508.03341)**
    [[code](https://github.com/nemori-ai/nemori)]

- [O-Mem: Omni Memory System for Personalized, Long Horizon, Self-Evolving Agents](https://arxiv.org/abs/2511.13593)

- [Omne-R1: Learning to Reason with Memory for Multi-hop Question Answering](https://arxiv.org/abs/2508.17330)

- [In Prospect and Retrospect: Reflective Memory Management for Long-term Personalized Dialogue Agents](https://aclanthology.org/2025.acl-long.413/)

- [SEDM: Scalable Self-Evolving Distributed Memory for Agents](https://arxiv.org/abs/2509.09498)

- [MemoRAG: Boosting Long Context Processing with Global Memory-Enhanced Retrieval Augmentation](https://arxiv.org/abs/2409.05591)

- [Human-inspired Episodic Memory for Infinite Context LLMs](https://arxiv.org/abs/2407.09450)

- [Towards LifeSpan Cognitive Systems](https://arxiv.org/abs/2409.13265)

#### 🗓️ 2024

- **[Compress to Impress: Unleashing the Potential of Compressive Memory in Real-World Long-Term Conversations](https://arxiv.org/abs/2402.11975)**
    [[code](https://github.com/nuochenpku/COMEDY)]

- **[Agent Workflow Memory](https://arxiv.org/abs/2409.07429)**
    [[code](https://github.com/zorazrw/agent-workflow-memory)]

- **[MemoryBank: Enhancing Large Language Models with Long-Term Memory](https://ojs.aaai.org/index.php/AAAI/article/view/29946)**
    [[code](https://github.com/zhongwanjun/MemoryBank-SiliconFriend)]

- **[Toward Conversational Agents with Context and Time Sensitive Long-term Memory](https://arxiv.org/abs/2406.00057)**
    [[data](https://github.com/Zyphra/TemporalMemoryDataset)]

- [InfLLM: Training-Free Long-Context Extrapolation for LLMs with an Efficient Context Memory](https://arxiv.org/abs/2402.04617)

#### 🗓️ 2023

- [RET-LLM: Towards a General Read-Write Memory for Large Language Models](https://arxiv.org/abs/2305.14322)

### 🌐 Graph Memory

#### 🗓️ 2025

- **[From RAG to Memory: Non-Parametric Continual Learning for Large Language Models](https://arxiv.org/abs/2502.14802)**
    [[code](https://github.com/OSU-NLP-Group/HippoRAG)]

- **[MIRIX: Multi-Agent Memory System for LLM-Based Agents](https://arxiv.org/abs/2507.07957)**
    [[code](https://github.com/Mirix-AI/MIRIX)]

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

#### 🗓️ 2025

- **[MemVerse: Multimodal Memory for Lifelong Learning Agents](https://arxiv.org/abs/2512.03627)**
    [[code](https://github.com/KnowledgeXLab/MemVerse)]
    [[blog](https://dw2283.github.io/memverse.ai/research)]

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

#### 🗓️ 2025

- **[MotionRAG: Motion Retrieval-Augmented Image-to-Video Generation](http://arxiv.org/abs/2509.26391)**
  [[code](https://github.com/MCG-NJU/MotionRAG)]

- **[VideoRAG: Retrieval-Augmented Generation over Video Corpus](http://arxiv.org/abs/2501.05874)**
  [[code](https://github.com/starsuzi/VideoRAG)]
  
- [Pack and Force Your Memory: Long-form and Consistent Video Generation](http://arxiv.org/abs/2510.01784)

- [Video World Models with Long-term Spatial Memory](http://arxiv.org/abs/2506.05284)

- [Mixture of Contexts for Long Video Generation](http://arxiv.org/abs/2508.21058)

- [Context as Memory: Scene-Consistent Interactive Long Video Generation with Memory Retrieval](http://arxiv.org/abs/2506.03141)


## 🔢 Papers - Parameteric Memory

#### 🗓️ 2025

- **[MLP Memory: Language Modeling with Retriever-pretrained External Memory](https://arxiv.org/abs/2508.01832)**
    [[code](https://github.com/Rubin-Wei/MLPMemory)]

- **[Memory Decoder: A Pretrained, Plug-and-Play Memory for Large Language Models](https://www.arxiv.org/abs/2508.09874)**
    [[code](https://github.com/LUMIA-Group/MemoryDecoder)]

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

- **[MA-LMM: Memory-Augmented Large Multimodal Model for Long-Term Video Understanding](https://openaccess.thecvf.com/content/CVPR2024/papers/He_MA-LMM_Memory-Augmented_Large_Multimodal_Model_for_Long-Term_Video_Understanding_CVPR_2024_paper.pdf)**
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

#### 🗓️ 2023

- **[Augmenting Language Models with Long-Term Memory](https://arxiv.org/abs/2306.07174)**
    [[code](https://github.com/Victorwz/LongMem)]

- **[Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180)**
    [[code](https://github.com/vllm-project/vllm)]

## 📈 Papers - Memory for Agent Evolution

### 🧭 Reinforcement Learning & Continual Learning 

#### 🗓️ 2025

- **[Remember Me, Refine Me: A Dynamic Procedural Memory Framework for Experience-Driven Agent Evolution](https://arxiv.org/abs/2512.10696)**
    [[code](https://github.com/agentscope-ai/ReMe)]

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

- [LightSearcher: Efficient DeepSearch via Experiential Memory](https://www.arxiv.org/abs/2512.06653)

- [Nested Learning: The Illusion of Deep Learning Architecture](https://abehrouz.github.io/files/NL.pdf)
  
- [Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning](https://arxiv.org/abs/2508.19828)
   
- [Latent Learning: Episodic Memory Complements Parametric Learning by Enabling Flexible Reuse of Experiences](https://arxiv.org/abs/2509.16189)

- [Evo-Memory: Benchmarking LLM Agent Test-time Learning with Self-Evolving Memory](https://arxiv.org/abs/2511.20857)

- [ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory](https://arxiv.org/abs/2509.25140)

- [Long Term Memory: The Foundation of AI Self-Evolution](https://arxiv.org/abs/2410.15665)

- [REFRAG: Rethinking RAG based Decoding](https://arxiv.org/abs/2509.01092)

- [MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent](https://arxiv.org/abs/2507.02259)

- [MemGen: Weaving Generative Latent Memory for Self-Evolving Agents](https://arxiv.org/abs/2509.24704)

- [ReSum: Unlocking Long-Horizon Search Intelligence via Context Summarization](https://arxiv.org/abs/2509.13313)

- [MARC: Memory-Augmented RL Token Compression for Efficient Video Understanding](https://arxiv.org/pdf/2510.07915)

- [Continual Learning via Sparse Memory Finetuning](https://arxiv.org/abs/2510.15103)
  
- [Task-Core Memory Management and Consolidation for Long-term Continual Learning](https://arxiv.org/abs/2505.09952)

### 🧩 Context Engineering 

#### 🗓️ 2025

- **[Everything is Context: Agentic File System Abstraction for Context Engineering](https://arxiv.org/abs/2512.05470)**
  [[code](https://github.com/AIGNE-io/aigne-framework)]

- [Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models](https://arxiv.org/abs/2510.04618)

## 🔬 Papers - Memory in Cognitive Science

#### 🗓️ 2025

- [How Prediction Error Drives Memory Updating: Role of Locus Coeruleus–Hippocampal Interactions](https://www.cell.com/trends/neurosciences/fulltext/S0166-2236(25)00189-4)

- [Towards Large Language Models with Human-Like Episodic Memory](https://www.cell.com/trends/cognitive-sciences/abstract/S1364-6613(25)00179-2)

## 📰 Articles

#### 🗓️ 2025

- [Survey of AI Agent Memory Frameworks](https://www.graphlit.com/blog/survey-of-ai-agent-memory-frameworks)

#### 🗓️ 2024

- [Memory in Language Model-Enabled Agents](https://yuweisunn.github.io/blog-1-06-24.html)

- [Mastering LLM Memory: A Comprehensive Guide](https://www.strongly.ai/blog/mastering-llm-memory-a-comprehensive-guide.html)

#### 🗓️ 2023

- [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/)

## 👥 Workshops

#### 🗓️ 2025

- [ACL 2025](https://2025.aclweb.org/) Workshop: [The First Workshop on Large Language Model Memorization (L2M2)](https://sites.google.com/view/memorization-workshop)
  [[proceedings](https://aclanthology.org/volumes/2025.l2m2-1/)]

---

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=TeleAI-UAGI/Awesome-Agent-Memory&type=date&legend=top-left)](https://www.star-history.com/#TeleAI-UAGI/Awesome-Agent-Memory&type=date&legend=top-left)

---

<div align="center">

**If you find this project helpful, please give us a ⭐️.**

Made with ❤️ by the Ubiquitous AGI team at TeleAI.

</div>

<div align="center" style="margin-top: 10px;">
    <img src="https://github.com/TeleAI-UAGI/TeleEgo/blob/main/assets/TeleAI.jpg" alt="TeleAI Logo" width="120px" />
</div>
