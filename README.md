<a name="readme-top"></a>

<h1 align="center">🧠 Awesome Agent Memory</h1>

<p align="center">
    <b> A curated collection of papers, projects, and resources on memory mechanisms for Large Language Models (LLMs) and Multimodal Large Language Models (MLLMs), exploring how different approaches enable long-term context, retrieval, and efficient reasoning </b>
</p>

<details open>
  <summary>🗂️ Table of Contents</summary>
  <ol>
    <li><a href="#systems">🧩 Systems</a></li>
    <li><a href="#tutorials">🧑‍🏫 Tutorials</a></li>
    <li><a href="#surveys">📚 Surveys</a></li>
    <li><a href="#benchmarks">📏 Benchmarks</a></li>
    <li><a href="#text-memory">📝 Papers - Text Memory</a></li>
    <li><a href="#parameter-memory">⚙️ Papers - Parameter Memory</a></li>
    <li><a href="#multimodal-memory">🎥 Papers - Multimodal Memory</a></li>
    <li><a href="#memory-retrieval">🔍 Papers - Memory Retrieval</a></li>
    <li><a href="#articles">📰 Articles</a></li>
    <li><a href="#workshops">💬 Workshops</a></li>
  </ol>
</details>

<h2 id="systems">🧩 Systems</h2>

#### Open-Source

Ordered by current Github stars.

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

4. **[Congee](https://www.cognee.ai/)**
   [[code](https://github.com/topoteretes/cognee)]
   [[paper](https://arxiv.org/abs/2505.24478)]
   [[blog](https://www.cognee.ai/blog)]

5. **[MemOS](https://memos.openmem.net/)** 
   [[code](https://github.com/MemTensor/MemOS)]
   [[paper](https://arxiv.org/abs/2507.03724)]
   [[blog](https://supermemory.ai/blog)]
   
6. **[MemU](https://memu.pro/)**
   [[code](https://github.com/NevaMind-AI/memU)]
   [[blog](https://memu.pro/blog)]

7. **[MIRIX](https://mirix.io/)**
   [[code](https://github.com/Mirix-AI/MIRIX)]
   [[paper](https://arxiv.org/abs/2507.07957)]
   [[blog](https://mirix.io/blog)]

8. **[Memobase](https://memobase.io/)**
   [[code](https://github.com/memodb-io/memobase)]
   [[blog](https://www.memobase.io/blog)]

9. **[TeleMem (under construction)]()**
   [[code](https://github.com/TeleAI-UAGI/TeleMem)]


#### Closed-Source

1. **[Supermemory](https://supermemory.ai/)**
   [[partial-code](https://github.com/supermemoryai/supermemory)]
   [[blog](https://supermemory.ai/blog)]

2. **[Memories.ai](https://memories.ai/)**
   [[research](https://memories.ai/research)]
   [[paper](https://memories.ai/research/Camera)]
   [[blog](memories.ai/blogs)]

4. **[Mem 2.0](https://get.mem.ai/)**
   [[blog](https://get.mem.ai/blog)]

5. **[TwinMind](https://twinmind.com/)**

#### Archival (Inactive)

1. [Memvid](https://www.memvid.com/)
   [[code](https://github.com/Olow304/memvid)]
   [[critique1](https://github.com/Olow304/memvid/issues/63),[critique2](https://github.com/Olow304/memvid/issues/49)]

2. [Memary](https://kingjulio8238.github.io/memarydocs/)
   [[code](https://github.com/kingjulio8238/memary)]

<h2 id="tutorials">🧑‍🏫 Tutorials</h2>

TBA

<h2 id="surveys">📚 Surveys</h2>

#### 🗓️ 2025

1. **[From Human Memory to AI Memory: A Survey on Memory Mechanisms in the Era of LLMs](https://arxiv.org/abs/2504.15965)**

    *Yaxiong Wu, Sheng Liang, Chen Zhang, Yichao Wang, Yongyue Zhang, Huifeng Guo, Ruiming Tang, Yong Liu.* Preprint, 2025

2. **[A Survey on the Memory Mechanism of Large
Language Model based Agents](https://dl.acm.org/doi/10.1145/3748302)** [[code](https://github.com/nuster1128/LLM_Agent_Memory_Survey)]

    *Zeyu Zhang, Quanyu Dai, Xiaohe Bo, Chen Ma, Rui Li, Xu Chen, Jieming Zhu, Zhenhua Dong, Ji-Rong Wen.* ACM Transactions on Information Systems, 2025

3. **[Cognitive Memory in Large Language Models](https://arxiv.org/abs/2504.02441)**

    *Lianlei Shan, Shixian Luo, Zezhou Zhu, Yu Yuan, Yong Wu.* Preprint, 2025

4. **[Advances and Challenges in Foundation Agents: From Brain-Inspired Intelligence to Evolutionary, Collaborative, and Safe Systems (Chapter 3)](https://arxiv.org/abs/2504.01990)**

    *Bang Liu, Xinfeng Li, Jiayi Zhang, Jinlin Wang, Tanjin He, Sirui Hong, Hongzhang Liu, Shaokun Zhang, Kaitao Song, Kunlun Zhu, Yuheng Cheng, Suyuchen Wang, Xiaoqiang Wang, Yuyu Luo, Haibo Jin, Peiyan Zhang, Ollie Liu, Jiaqi Chen, Huan Zhang, Zhaoyang Yu, Haochen Shi, Boyan Li, Dekun Wu, Fengwei Teng, Xiaojun Jia, Jiawei Xu, Jinyu Xiang, Yizhang Lin, Tianming Liu, Tongliang Liu, Yu Su, Huan Sun, Glen Berseth, Jianyun Nie, Ian Foster, Logan Ward, Qingyun Wu, Yu Gu, Mingchen Zhuge, Xinbing Liang, Xiangru Tang, Haohan Wang, Jiaxuan You, Chi Wang, Jian Pei, Qiang Yang, Xiaoliang Qi, Chenglin Wu.* Preprint, 2025

5. **[Rethinking Memory in AI: Taxonomy, Operations, Topics, and Future Directions](https://arxiv.org/abs/2505.00675)**

    _Yiming Du, Wenyu Huang, Danna Zheng, Zhaowei Wang, Sebastien Montella, Mirella Lapata, Kam-Fai Wong, Jeff Z. Pan._ Preprint, 2025
6. **[Human-inspired Perspectives: A Survey on AI Long-term Memory](https://arxiv.org/abs/2411.00489)**
   
    _Zihong He, Weizhe Lin, Hao Zheng, Fan Zhang, Matt W. Jones, Laurence Aitchison, Xuhai Xu, Miao Liu, Per Ola Kristensson, Junxiao Shen._ Preprint, 2025

<h2 id="benchmarks">📏 Benchmarks</h2>

### 💬 Text-only Benchmarks

#### 🗓️ 2025

1. **[HaluMem: Evaluating Hallucinations in Memory Systems of Agents](http://arxiv.org/abs/2511.03506)**
   [[code](https://github.com/MemTensor/HaluMem)]
   [[dataset](https://huggingface.co/datasets/IAAR-Shanghai/HaluMem)]

   _Ding Chen, Simin Niu, Kehang Li, Peng Liu, Xiangping Zheng, Bo Tang, Xinchi Li, Feiyu Xiong, Zhiyu Li._ Preprint, 2025 

2. **[MemoryBench: A Benchmark for Memory and Continual Learning in LLM Systems](https://arxiv.org/abs/2510.17281)**
   [[code](https://github.com/LittleDinoC/MemoryBench)]
   [[dataset](https://huggingface.co/datasets/THUIR/MemoryBench)]

   _Qingyao Ai, Yichen Tang, Changyue Wang, Jianming Long, Weihang Su, Yiqun Liu._ Preprint, 2025
   
3. **[OdysseyBench: Evaluating LLM Agents on Long-Horizon Complex Office Application Workflows](https://arxiv.org/abs/2508.09124)**
    
    *Weixuan Wang, Dongge Han, Daniel Madrigal Diaz, Jin Xu, Victor Rühle, Saravan Rajmohan.* Preprint, 2025

4. **[LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](https://arxiv.org/abs/2410.10813)**
   [[dataset](https://github.com/xiaowu0162/LongMemEval)]
    
    *Di Wu, Hongwei Wang, Wenhao Yu, Yuwei Zhang, Kai-Wei Chang, Dong Yu.* ICLR, 2025

5. **[LongBench v2: Towards Deeper Understanding and Reasoning on Realistic Long-context Multitasks](https://arxiv.org/abs/2412.15204)**
   [[dataset](https://github.com/THUDM/LongBench)]

   *Yushi Bai, Shangqing Tu, Jiajie Zhang, Hao Peng, Xiaozhi Wang, Xin Lv, Shulin Cao, Jiazheng Xu, Lei Hou, Yuxiao Dong, Jie Tang, Juanzi Li*. ACL 2025

6. **[Minerva: A Programmable Memory Test Benchmark for Language Models](https://arxiv.org/abs/2502.03358)**

   *Menglin Xia, Victor Ruehle, Saravan Rajmohan, Reza Shokri.* ICML, 2025

#### 🗓️ 2024
1. **[∞Bench: Extending Long Context Evaluation Beyond 100K Tokens](https://arxiv.org/abs/2402.13718v3)
[[code](https://github.com/OpenBMB/InfiniteBench)]**

    *Xinrong Zhang, Yingfa Chen, Shengding Hu, Zihang Xu, Junhao Chen, Moo Khai Hao, Xu Han, Zhen Leng Thai, Shuo Wang, Zhiyuan Liu, Maosong Sun.* Preprint, 2024

2. **[Evaluating Very Long-Term Conversational Memory of LLM Agents](https://arxiv.org/abs/2402.17753)
[[code](https://github.com/snap-research/LoCoMo)]**

    *Adyasha Maharana, Dong-Ho Lee, Sergey Tulyakov, Mohit Bansal, Francesco Barbieri, Yuwei Fang.* Preprint, 2024

3. **[LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding](https://arxiv.org/abs/2308.14508)
   [[code](https://github.com/THUDM/LongBench/blob/main/LongBench/README.md)]**

    *Yushi Bai, Xin Lv, Jiajie Zhang, Hongchang Lyu, Jiankai Tang, Zhidian Huang, Zhengxiao Du, Xiao Liu, Aohan Zeng, Lei Hou, Yuxiao Dong, Jie Tang, Juanzi Li.* ACL, 2024

#### 🗓️ 2023
1.  **[Storybench: A multifaceted benchmark for continuous story visualization ](https://proceedings.neurips.cc/paper_files/paper/2023/hash/f63f5fbed1a4ef08c857c5f377b5d33a-Abstract-Datasets_and_Benchmarks.html)** [[code](https://github.com/google/storybench)]

    *Emanuele Bugliarello, H. Hernan Moraldo, Ruben Villegas, Mohammad Babaeizadeh, Mohammad Taghi Saffar, Han Zhang, Dumitru Erhan, Vittorio Ferrari, Pieter-Jan Kindermans, Paul Voigtlaender.* NeurIPS, 2023

### 🎬 Multimodal Benchmarks

#### 🗓️ 2025
1.  **[TeleEgo: Benchmarking Egocentric AI Assistants in the Wild](https://arxiv.org/abs/2510.23981)** [[code](https://github.com/TeleAI-UAGI/TeleEgo)] [[project](https://programmergg.github.io/jrliu.github.io/)]

    *Jiaqi Yan, Ruilong Ren, Jingren Liu, Shuning Xu, Ling Wang, Yiheng Wang, Yun Wang, Long Zhang, Xiangyu Chen, Changzhi Sun, Jixiang Luo, Dell Zhang, Hao Sun, Chi Zhang, Xuelong Li*. Preprint, 2025

2.  **[LVBench: An Extreme Long Video Understanding Benchmark](https://arxiv.org/abs/2406.08035)** [[code](https://github.com/zai-org/LVBench)]

    *Weihan Wang, Zehai He, Wenyi Hong, Yean Cheng, Xiaohan Zhang, Ji Qi, Xiaotao Gu, Shiyu Huang, Bin Xu, Yuxiao Dong, Ming Ding, Jie Tang*. Preprint, 2025

3. **[Video-MME: The First-Ever Comprehensive Evaluation Benchmark of Multi-modal LLMs in Video Analysis](https://arxiv.org/abs/2405.21075v3)** [[code](https://github.com/MME-Benchmarks/Video-MME)]

    *Chaoyou Fu, Yuhan Dai, Yongdong Luo, Lei Li, Shuhuai Ren, Renrui Zhang, Zihan Wang, Chenyu Zhou, Yunhang Shen, Mengdan Zhang, Peixian Chen, Yanwei Li, Shaohui Lin, Sirui Zhao, Ke Li, Tong Xu, Xiawu Zheng, Enhong Chen, Caifeng Shan, Ran He, Xing Sun*. CVPR, 2025
    
4. **[Task-Core Memory Management and Consolidation for Long-term Continual Learning](https://arxiv.org/abs/2505.09952)**

    *Tianyu Huai, Jie Zhou, Yuxuan Cai, Qin Chen, Wen Wu, Xingjiao Wu, Xipeng Qiu, Liang He*. Neurips, 2025

#### 🗓️ 2024

1.  **[MovieChat+: Question-aware Sparse Memory for Long Video Question Answering](https://arxiv.org/abs/2404.17176)** [[code](https://github.com/rese1f/MovieChat)]

    *Enxin Song, Wenhao Chai, Tian Ye, Jenq-Neng Hwang, Xi Li, Gaoang Wang*. Preprint, 2024

2.  **[CinePile: A Long Video Question Answering Dataset and Benchmark](https://arxiv.org/abs/2405.08813)** [[code](https://huggingface.co/datasets/tomg-group-umd/cinepile)]

    *Ruchit Rawal, Khalid Saifullah, Miquel Farré, Ronen Basri, David Jacobs, Gowthami Somepalli, Tom Goldstein*. CVPR, 2024

3.  **[LongVideoBench: A Benchmark for Long-context
    Interleaved Video-Language Understanding](https://arxiv.org/abs/2407.15754)** [[code](https://github.com/longvideobench/LongVideoBench)]

    *Haoning Wu Dongxu Li Bei Chen Junnan Li*. NeurIPS, 2024

#### 🗓️ 2023

1. **[LvBench: A Benchmark for Long-form Video Understanding with Versatile Multi-modal Question Answering](https://arxiv.org/abs/2312.04817)**

    *Hongjie Zhang, Lu Dong, Yi Liu, Yifei Huang, Yali Wang, Limin Wang, Yu Qiao*. Preprint, 2023

2. **[EgoSchema: A Diagnostic Benchmark for Very Long-form Video Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2023/file/90ce332aff156b910b002ce4e6880dec-Paper-Datasets_and_Benchmarks.pdf)** [[code](https://github.com/egoschema/egoschema)]

    *Karttikeya Mangalam, Raiymbek Akshulakov, Jitendra Malik*. Preprint, 2023

<h2 id="text-memory">📝 Papers - Text Memory</h2>

### 📖 Plain-Text based Memory

#### 🗓️ 2025
1. **[In Prospect and Retrospect: Reflective Memory Management for Long-term Personalized Dialogue Agents](https://aclanthology.org/2025.acl-long.413/)**

    *Zhen Tan, Jun Yan, I-Hung Hsu, Rujun Han, Zifeng Wang, Long Le, Yiwen Song, Yanfei Chen, Hamid Palangi, George Lee, Anand Rajan Iyer, Tianlong Chen, Huan Liu, Chen-Yu Lee, Tomas Pfister*. ACL, 2025
    
2. **[SEDM: Scalable Self-Evolving Distributed Memory for Agents](https://arxiv.org/abs/2509.09498)**

    *Haoran Xu, Jiacong Hu, Ke Zhang, Lei Yu, Yuxin Tang, Xinyuan Song, Yiqun Duan, Lynn Ai, Bill Shi*. Preprint, 2025

5. **[MemoRAG: Boosting Long Context Processing with Global Memory-Enhanced Retrieval Augmentation](https://arxiv.org/abs/2409.05591)**

   *Hongjin Qian, Zheng Liu, Peitian Zhang, Kelong Mao, Defu Lian, Zhicheng Dou, Tiejun Huang*. theWebConf, 2025

6. **[Human-inspired Episodic Memory for Infinite Context LLMs](https://arxiv.org/abs/2407.09450)**

    *Zafeirios Fountas, Martin A Benfeghoul, Adnan Oomerjee, Fenia Christopoulou, Gerasimos Lampouras, Haitham Bou-Ammar, Jun Wang*. ICLR, 2025

8. **[Towards LifeSpan Cognitive Systems](https://arxiv.org/abs/2409.13265)**

    *Yu Wang, Chi Han, Tongtong Wu, Xiaoxin He, Wangchunshu Zhou, Nafis Sadeq, Xiusi Chen, Zexue He, Wei Wang, Gholamreza Haffari, Heng Ji, Julian McAuley*. TMLR, 2025


#### 🗓️ 2024

1. **[Compress to Impress: Unleashing the Potential of Compressive Memory in Real-World Long-Term Conversations](https://arxiv.org/abs/2402.11975)** [[code](https://github.com/nuochenpku/COMEDY)]

    *Nuo Chen, Hongguang Li, Juhua Huang, Baoyuan Wang, Jia Li*. Preprint, 2024

2. **[Agent Workflow Memory](https://arxiv.org/abs/2409.07429)** [[code](https://github.com/zorazrw/agent-workflow-memory)]

    *Zora Zhiruo Wang, Jiayuan Mao, Daniel Fried, Graham Neubig*. Preprint, 2024

3. **[MemoryBank: Enhancing Large Language Models with Long-Term Memory](https://ojs.aaai.org/index.php/AAAI/article/view/29946)** [[code](https://github.com/zhongwanjun/MemoryBank-SiliconFriend)]

    *Wanjun Zhong, Lianghong Guo, Qiqi Gao, He Ye, Yanlin Wang*. AAAI, 2024
    
4. **[InfLLM: Training-Free Long-Context Extrapolation for LLMs with an Efficient Context Memory](https://arxiv.org/abs/2402.04617)**

    *Chaojun Xiao, Pengle Zhang, Xu Han, Guangxuan Xiao, Yankai Lin, Zhengyan Zhang, Zhiyuan Liu, Maosong Sun*. Preprint, 2024


#### 🗓️ 2023

1. **[RET-LLM: Towards a General Read-Write Memory for Large Language Models](https://arxiv.org/abs/2305.14322)**

    *Ali Modarressi, Ayyoob Imani, Mohsen Fayyaz, Hinrich Schütze*. Preprint, 2023

### 🧠 Graph based Memory


#### 🗓️ 2025

1. **[From RAG to Memory: Non-Parametric Continual Learning for Large Language Models](https://arxiv.org/abs/2502.14802)** [[code](https://github.com/OSU-NLP-Group/HippoRAG)]

    *Bernal Jiménez Gutiérrez, Yiheng Shu, Weijian Qi, Sizhe Zhou, Yu Su*. ICML, 2025

2. **[Zep](https://github.com/getzep/zep)**

3. **[MIRIX: Multi-Agent Memory System for LLM-Based Agents](https://arxiv.org/abs/2507.07957)** [[code](https://github.com/Mirix-AI/MIRIX)]

    *Yu Wang, Xi Chen*. Preprint, 2025

4. **[Hierarchical Memory Organization for Wikipedia Generation](https://aclanthology.org/2025.acl-long.1423/)** [[code](https://github.com/eugeneyujunhao/mog)]

    *Eugene J. Yu, Dawei Zhu, Yifan Song, Xiangyu Wong, Jiebin Zhang, Wenxuan Shi, Xiaoguang Li, Qun Liu, Sujian Li*. ACL, 2025

5. **[Bridging Intuitive Associations and Deliberate Recall: Empowering LLM Personal Assistant with Graph-Structured Long-term Memory](https://aclanthology.org/2025.findings-acl.901/)**

    *Yujie Zhang, Weikang Yuan, Zhuoren Jiang*. Findings of ACL, 2025

6. **[HiAgent: Hierarchical Working Memory Management for Solving Long-Horizon Agent Tasks with Large Language Model](https://aclanthology.org/2025.acl-long.1575/)**

    *Mengkang Hu, Tianxing Chen, Qiguang Chen, Yao Mu, Wenqi Shao, Ping Luo*. ACL, 2025

#### 🗓️ 2024

1. **[HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models](https://arxiv.org/abs/2405.14831)** [[code](https://github.com/OSU-NLP-Group/HippoRAG)]

    *Bernal Jiménez Gutiérrez, Yiheng Shu, Yu Gu, Michihiro Yasunaga, Yu Su*. NeurIPS, 2024

2. **[AriGraph: Learning Knowledge Graph World Models with Episodic Memory for LLM Agents](https://arxiv.org/abs/2407.04363)** [[code](https://github.com/AIRI-Institute/AriGraph)]

    *Petr Anokhin, Nikita Semenov, Artyom Sorokin, Dmitry Evseev, Andrey Kravchenko, Mikhail Burtsev, Evgeny Burnaev*. Preprint, 2024


<h2 id="parameter-memory">⚙️ Papers - Parameter Memory</h2>


#### 🗓️ 2025
1. **[R<sup>3</sup>Mem: Bridging Memory Retention and Retrieval via Reversible Compression](https://arxiv.org/abs/2502.15957)**

    *Xiaoqiang Wang, Suyuchen Wang, Yun Zhu, Bang Liu*. Preprint, 2025

2. **[May the Memory Be With You: Efficient and Infinitely Updatable State for Large Language Models](https://dl.acm.org/doi/abs/10.1145/3721146.3721951)**

    *Excel Chukwu, Laurent Bindschaedler*. Preprint, 2025

3. **[MLP Memory: Language Modeling with Retriever-pretrained External Memory](https://arxiv.org/abs/2508.01832)**

    *Rubin Wei, Jiaqi Cao, Jiarui Wang, Jushi Kai, Qipeng Guo, Bowen Zhou, Zhouhan Lin*. Preprint, 2025

4. **[Memory Decoder: A Pretrained, Plug-and-Play Memory for Large Language Models](https://www.arxiv.org/abs/2508.09874)**

    *Jiaqi Cao, Jiarui Wang, Rubin Wei, Qipeng Guo, Kai Chen, Bowen Zhou, Zhouhan Lin*. Preprint, 2025

5. **[MeMo: Towards Language Models with Associative Memory Mechanisms](https://aclanthology.org/2025.findings-acl.785/)**

    *Fabio Massimo Zanzotto, Elena Sofia Ruzzetti, Giancarlo A. Xompero, Leonardo Ranaldi, Davide Venditti, Federico Ranaldi, Cristina Giannone, Andrea Favalli, Raniero Romagnoli*. Findings of ACL, 2025

6. **[REFRAG: Rethinking RAG based Decoding](https://arxiv.org/abs/2509.01092)**

    *Xiaoqiang Lin, Aritra Ghosh, Bryan Kian Hsiang Low, Anshumali Shrivastava, Vijai Mohan*. Preprint, 2025

7. **[EpMAN: Episodic Memory AttentioN for Generalizing to Longer Contexts](https://aclanthology.org/2025.acl-long.574/)**

    *Subhajit Chaudhury, Payel Das, Sarathkrishna Swaminathan, Georgios Kollias, Elliot Nelson, Khushbu Pahwa, Tejaswini Pedapati, Igor Melnyk, Matthew Riemer*. ACL, 2025

8. **[Disentangling Memory and Reasoning Ability in Large Language Models](https://aclanthology.org/2025.acl-long.84/)**

    *Mingyu Jin, Weidi Luo, Sitao Cheng, Xinyi Wang, Wenyue Hua, Ruixiang Tang, William Yang Wang, Yongfeng Zhang*. ACL, 2025


#### 🗓️ 2024
1. **[InfLLM: Training-Free Long-Context Extrapolation for LLMs with an Efficient Context Memory](https://arxiv.org/abs/2402.04617)** [[code](https://github.com/thunlp/InfLLM)]

    *Chaojun Xiao, Pengle Zhang, Xu Han, Guangxuan Xiao, Yankai Lin, Zhengyan Zhang, Zhiyuan Liu, Maosong Sun*. Preprint, 2024

2. **[Memory<sup>3</sup>: Language Modeling with Explicit Memory](https://arxiv.org/abs/2407.01178v1)**

    *Hongkang Yang, Zehao Lin, Wenjin Wang, Hao Wu, Zhiyu Li, Bo Tang, Wenqiang Wei, Jinbo Wang, Zeyun Tang, Shichao Song, Chenyang Xi, Yu Yu, Kai Chen, Feiyu Xiong, Linpeng Tang, Weinan E*. Preprint, 2024

3. **[MA-LMM: Memory-Augmented Large Multimodal Model for Long-Term Video Understanding](https://openaccess.thecvf.com/content/CVPR2024/papers/He_MA-LMM_Memory-Augmented_Large_Multimodal_Model_for_Long-Term_Video_Understanding_CVPR_2024_paper.pdf)** [[code](https://github.com/boheumd/MA-LMM)]

    *Bo He, Hengduo Li, Young Kyun Jang, Menglin Jia, Xuefei Cao, Ashish Shah, Abhinav Shrivastava, Ser-Nam Lim*. CVPR, 2024

4. **[MemoryLLM: Towards Self-Updatable Large Language Models](https://arxiv.org/abs/2402.04624)** [[code](https://github.com/wangyu-ustc/MemoryLLM)]

    *Yu Wang, Yifan Gao, Xiusi Chen, Haoming Jiang, Shiyang Li, Jingfeng Yang, Qingyu Yin, Zheng Li, Xian Li, Bing Yin, Jingbo Shang, Julian McAuley*. Preprint, 2024

5. **[WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models](https://arxiv.org/abs/2405.14768)** [[code](https://github.com/zjunlp/EasyEdit)]

    *Peng Wang, Zexi Li, Ningyu Zhang, Ziwen Xu, Yunzhi Yao, Yong Jiang, Pengjun Xie, Fei Huang, Huajun Chen*. NeurIPS, 2024

6. **[Infinite-LLM: Efficient LLM Service for Long Context with DistAttention and Distributed KVCache](https://arxiv.org/abs/2401.02669)**

    *Bin Lin, Chen Zhang, Tao Peng, Hanyu Zhao, Wencong Xiao, Minmin Sun, Anmin Liu, Zhipeng Zhang, Lanbo Li, Xiafei Qiu, Shen Li, Zhigang Ji, Tao Xie, Yong Li, Wei Lin*. Preprint, 2024

7. **[MemServe: Context Caching for Disaggregated LLM Serving with Elastic Memory Pool](https://arxiv.org/abs/2406.17565)**
    *Cunchen Hu, Heyang Huang, Junhao Hu, Jiang Xu, Xusheng Chen, Tao Xie, Chenxi Wang, Sa Wang, Yungang Bao, Ninghui Sun, Yizhou Shan*. Preprint, 2024

8. **[WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models](https://arxiv.org/abs/2405.14768/)**
    *Peng Wang, Zexi Li, Ningyu Zhang, Ziwen Xu, Yunzhi Yao, Yong Jiang, Pengjun Xie, Fei Huang, Huajun Chen*. NeurIPS,2024


#### 🗓️ 2023

1. **[Augmenting Language Models with Long-Term Memory](https://arxiv.org/abs/2306.07174)** [[code](https://github.com/Victorwz/LongMem)]

    *Weizhi Wang, Li Dong, Hao Cheng, Xiaodong Liu, Xifeng Yan, Jianfeng Gao, Furu Wei*. Preprint, 2023

2. **[Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180)** [[code](https://github.com/vllm-project/vllm)]

    *Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Hao Yu, Joseph E. Gonzalez, Hao Zhang, Ion Stoica*. Preprint, 2023

<h2 id="multimodal-memory">🎥 Papers - Multimodal Memory</h2>

#### 🗓️ 2025

1. **[Infinite Video Understanding](https://www.arxiv.org/abs/2507.09068)** 

    *Dell Zhang, Xiangyu Chen, Jixiang Luo, Mengxi Jia, Changzhi Sun, Ruilong Ren, Jingren Liu, Hao Sun, Xuelong Li*. Preprint, 2025

2. **[Seeing, Listening, Remembering, and Reasoning: A Multimodal Agent with Long-Term Memory](https://arxiv.org/abs/2508.09736)** [[code](https://github.com/bytedance-seed/m3-agent)]

    *Lin Long, Yichen He, Wentao Ye, Yiyuan Pan, Yuan Lin, Hang Li, Junbo Zhao, Wei Li*. Preprint, 2025

3. **[HippoMM: Hippocampal-inspired Multimodal Memory for Long Audiovisual Event Understanding](https://arxiv.org/abs/2504.10739)** [[code](https://github.com/linyueqian/HippoMM)]

    *Yueqian Lin, Qinsi Wang, Hancheng Ye, Yuzhe Fu, Hai "Helen" Li, Yiran Chen*. Preprint, 2025

4. **[Episodic Memory Representation for Long-form Video Understanding](https://arxiv.org/abs/2508.09486)**

    *Yun Wang, Long Zhang, Jingren Liu, Jiaqi Yan, Zhanjie Zhang, Jiahao Zheng, Xun Yang, Dapeng Wu, Xiangyu Chen, Xuelong Li*. Preprint, 2025

5. **[Multi-RAG: A Multimodal Retrieval-Augmented Generation System for Adaptive Video Understanding](https://arxiv.org/abs/2505.23990)**

    *Mingyang Mao, Mariela M. Perez-Cabarcas, Utteja Kallakuri, Nicholas R. Waytowich, Xiaomin Lin, Tinoosh Mohsenin*.  Preprint, 2025
    
5. **[Contextual Experience Replay for Self-Improvement of Language Agents](https://arxiv.org/abs/2506.06698)**

    *Yitao Liu, Chenglei Si, Karthik Narasimhan, Shunyu Yao*.  Preprint, 2025


#### 🗓️ 2024
1. **[VideoAgent: Long-form Video Understanding with Large Language Model as Agent](https://arxiv.org/abs/2403.10517)** [[code](https://github.com/HKUDS/VideoAgent)]

    *Xiaohan Wang, Yuhui Zhang, Orr Zohar, Serena Yeung-Levy*. Preprint, 2024

2. **[VideoChat-Flash: Hierarchical Compression for Long-Context Video Modeling](https://arxiv.org/abs/2501.00574)** [[code](https://github.com/OpenGVLab/VideoChat-Flash)]

    *Xinhao Li, Yi Wang, Jiashuo Yu, Xiangyu Zeng, Yuhan Zhu, Haian Huang, Jianfei Gao, Kunchang Li, Yinan He, Chenting Wang, Yu Qiao, Yali Wang, Limin Wang*. Preprint, 2024

3. **[LongVLM: Efficient Long Video Understanding via Large Language Models](https://arxiv.org/abs/2404.03384)** [[code](https://github.com/ziplab/LongVLM)]

    *Yuetian Weng, Mingfei Han, Haoyu He, Xiaojun Chang, Bohan Zhuang*. ECCV, 2024


<h2 id="memory-retrieval">🔍 Papers - Memory Retrieval</h2>

### 🧭 Reinforcement Learning

#### 🗓️ 2025

1. **[Memento: Fine-tuning LLM Agents without Fine-tuning LLMs](https://arxiv.org/abs/2508.16153)**

    *Huichi Zhou, Yihang Chen, Siyuan Guo, Xue Yan, Kin Hei Lee, Zihan Wang, Ka Yiu Lee, Guchun Zhang, Kun Shao, Linyi Yang, Jun Wang*. Preprint, 2025

2. **[REFRAG: Rethinking RAG based Decoding](https://arxiv.org/abs/2509.01092)**

    *Xiaoqiang Lin, Aritra Ghosh, Bryan Kian Hsiang Low, Anshumali Shrivastava, Vijai Mohan*. Preprint, 2025

3. **[Seeing, Listening, Remembering, and Reasoning: A Multimodal Agent with Long-Term Memory](https://arxiv.org/abs/2508.09736)** [[code](https://github.com/bytedance-seed/m3-agent)]

    *Lin Long, Yichen He, Wentao Ye, Yiyuan Pan, Yuan Lin, Hang Li, Junbo Zhao, Wei Li*. Preprint, 2025

4. **[MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent](https://arxiv.org/abs/2507.02259)**

    *Hongli Yu, Tinghong Chen, Jiangtao Feng, Jiangjie Chen, Weinan Dai, Qiying Yu, Ya-Qin Zhang, Wei-Ying Ma, Jingjing Liu, Mingxuan Wang, Hao Zhou*. Preprint, 2025
    
5. **[MemGen: Weaving Generative Latent Memory for Self-Evolving Agents](https://arxiv.org/abs/2509.24704)**

    *Guibin Zhang, Muxin Fu, Shuicheng Yan*. Preprint, 2025

6. **[ReSum: Unlocking Long-Horizon Search Intelligence via Context Summarization](https://arxiv.org/abs/2509.13313)**

    *Xixi Wu, Kuan Li, Yida Zhao, Liwen Zhang, Litu Ou, Huifeng Yin, Zhongwang Zhang, Xinmiao Yu, Dingchu Zhang, Yong Jiang, Pengjun Xie, Fei Huang, Minhao Cheng, Shuai Wang, Hong Cheng, Jingren Zhou*. Preprint, 2025
    
7. **[MARC: Memory-Augmented RL Token Compression for Efficient Video Understanding](https://arxiv.org/pdf/2510.07915)**

    *Xixi Wu, Kuan Li, Yida Zhao, Liwen Zhang, Litu Ou, Huifeng Yin, Zhongwang Zhang, Xinmiao Yu, Dingchu Zhang, Yong Jiang, Pengjun Xie, Fei Huang, Minhao Cheng, Shuai Wang, Hong Cheng, Jingren Zhou*. Preprint, 2025


<h2 id="articles">📰 Articles</h2>

#### 🗓️ 2025
1. **[Survey of AI Agent Memory Frameworks](https://www.graphlit.com/blog/survey-of-ai-agent-memory-frameworks)**

    *Kirk Marple*, 2025
#### 🗓️ 2024
1. **[Memory in Language Model-Enabled Agents](https://yuweisunn.github.io/blog-1-06-24.html)**

    *Yuwei Sun*, 2024

2. **[Mastering LLM Memory: A Comprehensive Guide](https://www.strongly.ai/blog/mastering-llm-memory-a-comprehensive-guide.html)**

    *Strongly.AI*, 2024

#### 🗓️ 2023
1. **[LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/)**

    *Lilian Weng*, 2023

<h2 id="workshops">💬 Workshops</h2>

#### 🗓️ 2025
1. **[Proceedings of the First Workshop on Large Language Model Memorization (L2M2)](https://aclanthology.org/volumes/2025.l2m2-1/)**

    *Robin Jia, Eric Wallace, Yangsibo Huang, Tiago Pimentel, Pratyush Maini, Verna Dankers, Johnny Wei, Pietro Lesci (Editors)*. 2025

