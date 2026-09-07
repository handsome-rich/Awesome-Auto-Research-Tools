# 🔬 Awesome Auto Research [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[English](README.md) | [中文](README_CN.md)

<p align="center">
  <img src="fig/banner_cn.jpg" alt="开源科研自动化项目精选" width="800">
</p>

> 🤖 精选的自动化科研开源项目列表 —— 覆盖文献综述、想法生成、实验执行、论文撰写与同行评审全流程。

**📅 Star 数据最后验证时间：2026-07-25**

---

## 📑 目录

- [🧪 自主研究系统](#-自主研究系统)
- [📚 深度调研与文献综合](#-深度调研与文献综合)
- [⚙️ 研究实现与实验](#️-研究实现与实验)
- [✍️ 学术写作与传播](#️-学术写作与传播)
- [🔧 研究 Skills 与插件合集](#-研究-skills-与插件合集)
- [📋 Awesome Lists 与综述](#-awesome-lists-与综述)
- [💡 本列表与通用 AI Agent 列表的区别](#-本列表与通用-ai-agent-列表的区别)
- [🤝 贡献指南](#-贡献指南)

---

## 🧪 自主研究系统

> 自主完成科研闭环中多个阶段的系统，例如假设生成、实验、分析和论文准备。

| 项目 | Stars | 框架 / 工具 | 支持的 LLM API | 简介 |
|------|-------|-------------|----------------|------|
| [autoresearch](https://github.com/karpathy/autoresearch) | <img src="https://img.shields.io/github/stars/karpathy/autoresearch?style=for-the-badge" height="36"> | 自研（PyTorch, nanochat） | Anthropic Claude Code、OpenAI Codex 等外部编码 agent | Andrej Karpathy 出品的极简单 GPU 研究框架：外部编码 agent 按 `program.md` 指令反复修改 `train.py`，并运行固定五分钟的 nanochat 实验。 |
| [AI-Scientist](https://github.com/SakanaAI/AI-Scientist) | <img src="https://img.shields.io/github/stars/SakanaAI/AI-Scientist?style=for-the-badge" height="36"> | 自研（模板系统, LaTeX 流水线） | OpenAI, Anthropic Claude, DeepSeek, Gemini, OpenRouter, 开源模型 | 首个全自动开放式科学发现系统。自动完成想法生成、编码、实验运行和完整论文撰写。 |
| [RD-Agent](https://github.com/microsoft/RD-Agent) | <img src="https://img.shields.io/github/stars/microsoft/RD-Agent?style=for-the-badge" height="36"> | 自研 + **LiteLLM**, Docker, Streamlit, Qlib | OpenAI (GPT-4o/o1/o3), Azure OpenAI, DeepSeek；任何 LiteLLM 支持的提供商 | 微软出品。自动化 R&D 流程 —— 量化因子/模型演化、Kaggle 自动化、论文到代码实现。MLE-bench 顶尖 agent。 |
| [AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | <img src="https://img.shields.io/github/stars/aiming-lab/AutoResearchClaw?style=for-the-badge" height="36"> | **OpenClaw** + Docker, LaTeX (NeurIPS/ICML/ICLR), OpenAlex, Semantic Scholar | OpenAI (GPT-4o), OpenRouter, DeepSeek, MiniMax；Claude/Gemini/Kimi 经 ACP 协议 | 自主或人在回路研究：idea → 文献检索 → 沙箱实验 → 多 agent 同行评审 → LaTeX 论文输出，支持六种可配置干预模式。 |
| [ARIS](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | <img src="https://img.shields.io/github/stars/wanshuiyin/Auto-claude-code-research-in-sleep?style=for-the-badge" height="36"> | **Claude Code** + MCP（Codex, llm-chat, Zotero, Obsidian） | Anthropic Claude, OpenAI GPT, GLM-5, MiniMax, Kimi, Qwen, DeepSeek, LongCat；任何 OpenAI 兼容 API | Claude Code skills 套件，用于自主 ML 研究：跨模型评审循环、想法发现流水线、实验自动化与论文撰写。 |
| [AI-Scientist-v2](https://github.com/SakanaAI/AI-Scientist-v2) | <img src="https://img.shields.io/github/stars/SakanaAI/AI-Scientist-v2?style=for-the-badge" height="36"> | 自研（BFTS 智能体树搜索, AIDE） | OpenAI (o1/o3/GPT-4o), Anthropic (Bedrock), Gemini | AI-Scientist 升级版。首篇完全由 AI 撰写并通过同行评审被接收的 Workshop 论文。 |
| [Agent Laboratory](https://github.com/SamuelSchmidgall/AgentLaboratory) | <img src="https://img.shields.io/github/stars/SamuelSchmidgall/AgentLaboratory?style=for-the-badge" height="36"> | 自研多智能体（arXiv, HuggingFace, LaTeX） | OpenAI (o1/o3/GPT-4o), DeepSeek | 端到端自主研究工作流，包含文献综述、实验和报告撰写的专用智能体。 |
| [AI-Researcher](https://github.com/HKUDS/AI-Researcher) | <img src="https://img.shields.io/github/stars/HKUDS/AI-Researcher?style=for-the-badge" height="36"> | 自研 + **LiteLLM**, Docker, Gradio | Anthropic, OpenAI, Gemini, DeepSeek, OpenRouter, GitHub AI（经 LiteLLM） | NeurIPS 2025 Spotlight。完全自主系统，覆盖文献综述、假设生成、算法实现和可投稿论文准备。 |
| [claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | <img src="https://img.shields.io/github/stars/Galaxy-Dawn/claude-scholar?style=for-the-badge" height="36"> | **Claude Code** / Codex CLI / OpenCode, Zotero MCP, Obsidian, LaTeX | Anthropic Claude, OpenAI（经 Codex） | 半自动学术研究助手，覆盖 idea → 编码 → 实验 → 写作 → 投稿。 |
| [EvoScientist](https://github.com/EvoScientist/EvoScientist) | <img src="https://img.shields.io/github/stars/EvoScientist/EvoScientist?style=for-the-badge" height="36"> | **LangChain** + DeepAgents, Docker（Python 3.11 + Node.js 24） | Anthropic Claude, OpenAI, Google Gemini, MiniMax, NVIDIA NIM | 自我进化的 AI Scientist。6 个专门 agent 协作，带持久化记忆，可自主探索并迭代改进。内置消息通道（Slack/Discord/Telegram/飞书/微信）。 |
| [Biomni](https://github.com/snap-stanford/Biomni) | <img src="https://img.shields.io/github/stars/snap-stanford/Biomni?style=for-the-badge" height="36"> | 生物医学自研智能体 + 代码执行、数据湖、know-how 知识库 | Anthropic Claude, OpenAI, Azure OpenAI, Gemini, Groq, AWS Bedrock, 自定义 OpenAI 兼容 API | 斯坦福出品。通用生物医学 AI 智能体，可在生物与医学研究中自主执行任务，结合 LLM 推理、检索增强与工具/代码调用。 |
| [DeepScientist](https://github.com/ResearAI/DeepScientist) | <img src="https://img.shields.io/github/stars/ResearAI/DeepScientist?style=for-the-badge" height="36"> | 自研（贝叶斯优化、Findings Memory、Research Map），Git worktrees, LaTeX | OpenAI (Codex CLI), Anthropic Claude, Moonshot Kimi, OpenCode；本地模型后端 | Local-first 自主研究 studio。Findings Memory 与贝叶斯优化编排基线复现 → 分支实验 → LaTeX 论文草稿。 |
| [DATAGEN](https://github.com/starpig1129/DATAGEN) | <img src="https://img.shields.io/github/stars/starpig1129/DATAGEN?style=for-the-badge" height="36"> | **LangChain** + **LangGraph**, MCP servers, Firecrawl | OpenAI, Anthropic Claude, Gemini, Ollama, Groq | AI 驱动的多智能体研究助手，自动完成假设生成、数据分析、可视化和报告撰写。 |
| [AutoSci](https://github.com/skyllwt/AutoSci) | <img src="https://img.shields.io/github/stars/skyllwt/AutoSci?style=for-the-badge" height="36"> | 记忆中心式 agent 框架、持久化知识图谱、Web 仪表盘 | Claude Code；预览支持 Codex 和 OpenCode | 具有跨阶段持久记忆的全生命周期研究系统，覆盖文献综述、构思、实验、分析与论文写作。 |
| [NanoResearch](https://github.com/OpenRaiser/NanoResearch) | <img src="https://img.shields.io/github/stars/OpenRaiser/NanoResearch?style=for-the-badge" height="36"> | 九阶段流水线、本地/SLURM 执行、LaTeX | OpenAI 兼容 API；Claude Code 和 Codex | 从 idea 到论文的端到端研究流水线，可在本地机器或 SLURM 集群上执行真实实验。 |
| [InternAgent](https://github.com/InternScience/InternAgent) | <img src="https://img.shields.io/github/stars/InternScience/InternAgent?style=for-the-badge" height="36"> | 自研（Aider 代码生成、持久化记忆），Conda；Google Search, Semantic Scholar | OpenAI（含 OpenAI 兼容接口）, Anthropic Claude | 上海 AI Lab 出品。长周期自主科学发现的统一 agentic 框架，覆盖物理、生物、地球与生命科学 —— 反应产率预测、分子动力学、蛋白质工程、气候诊断。 |
| [Idea2Paper](https://github.com/AgentAlphaAGI/Idea2Paper) | <img src="https://img.shields.io/github/stars/AgentAlphaAGI/Idea2Paper?style=for-the-badge" height="36"> | 自研 AgentAlpha 框架（多智能体协作），向量数据库，知识图谱 | DeepSeek V3/R1, Claude 3.5, GPT-4o；Semantic Scholar, ArXiv API | 科研灵感探索引擎：多 Agent 协同进行深度文献挖掘与知识图谱对齐，将朴素 idea 包装为结构化课题方案。 |
| [K-Dense BYOK](https://github.com/K-Dense-AI/k-dense-byok) | <img src="https://img.shields.io/github/stars/K-Dense-AI/k-dense-byok?style=for-the-badge" height="36"> | 本地优先桌面工作区、科学 skills、专家 agent、MCP、Ollama | OpenRouter, OpenAI Codex, Anthropic Claude, GitHub Copilot, xAI, Ollama | 本地 AI 科研协作者，可检索文献、分析真实数据、运行代码、生成图表与报告，并记录可检查的动态实验日志。 |
| [data-to-paper](https://github.com/Technion-Kishony-lab/data-to-paper) | <img src="https://img.shields.io/github/stars/Technion-Kishony-lab/data-to-paper?style=for-the-badge" height="36"> | 多智能体流水线、代码执行、LaTeX、Semantic Scholar | OpenAI API；可选 DeepInfra | 将科研数据集转化为透明、可追溯、可验证的论文，由多个 agent 分工完成分析、解释、文献检索与写作。 |
| [Robin](https://github.com/Future-House/robin) | <img src="https://img.shields.io/github/stars/Future-House/robin?style=for-the-badge" height="36"> | 多智能体科学发现系统、**LiteLLM**、Edison 平台 | LiteLLM 支持的模型；需要 Edison 访问权限 | FutureHouse 的多智能体科学发现系统，协同完成文献调研、数据分析与实验规划。 |

## 📚 深度调研与文献综合

> 聚焦于自动信息收集、文献综述和报告生成。

| 项目 | Stars | 框架 / 工具 | 支持的 LLM API | 简介 |
|------|-------|-------------|----------------|------|
| [DeerFlow](https://github.com/bytedance/deer-flow) | <img src="https://img.shields.io/github/stars/bytedance/deer-flow?style=for-the-badge" height="36"> | **LangChain** + **LangGraph**, InfoQuest | 任何 OpenAI 兼容 API（GPT-4, Gemini via OpenRouter 等） | 字节跳动出品。开源 SuperAgent 框架，编排子智能体、记忆和沙箱，用于深度调研、代码生成和报告撰写。 |
| [STORM](https://github.com/stanford-oval/storm) | <img src="https://img.shields.io/github/stars/stanford-oval/storm?style=for-the-badge" height="36"> | **DSPy** + **LiteLLM**, Streamlit | 全部 LiteLLM 支持的模型（OpenAI, Azure 等）；搜索：You.com, Bing, Google, Brave, Tavily, SearXNG | 斯坦福出品。LLM 驱动的知识管理系统，生成带引用的完整维基百科风格文章。支持 Co-STORM 人机协作。 |
| [GPT Researcher](https://github.com/assafelovic/gpt-researcher) | <img src="https://img.shields.io/github/stars/assafelovic/gpt-researcher?style=for-the-badge" height="36"> | **LangGraph**, MCP, FastAPI, NextJS | OpenAI, Anthropic Claude, Gemini；任何 OpenAI 兼容 API | 自主深度调研智能体。生成 5-6 页带引用的事实性报告，支持 PDF/Docx/Markdown 和多智能体工作流。 |
| [通义深度研究](https://github.com/Alibaba-NLP/DeepResearch) | <img src="https://img.shields.io/github/stars/Alibaba-NLP/DeepResearch?style=for-the-badge" height="36"> | 自研（ReAct, IterResearch, GRPO RL）；Serper, Jina, SandboxFusion | OpenAI 兼容, OpenRouter；通义-30B-A3B, Dashscope/百炼 | 阿里巴巴出品。Agentic LLM（305 亿参数，33 亿激活），专为长周期深度信息检索设计。多项基准 SOTA。 |
| [Open Deep Research](https://github.com/langchain-ai/open_deep_research) | <img src="https://img.shields.io/github/stars/langchain-ai/open_deep_research?style=for-the-badge" height="36"> | **LangChain** + **LangGraph**, MCP, LangSmith | OpenAI (GPT-5/4.1), Anthropic (Sonnet 4), OpenRouter, Ollama（本地） | LangChain 出品。开源深度调研框架，可配置 MCP 工具和搜索 API。 |
| [PaperQA2](https://github.com/Future-House/paper-qa) | <img src="https://img.shields.io/github/stars/Future-House/paper-qa?style=for-the-badge" height="36"> | 自研 + **LiteLLM**, Pydantic, tantivy | OpenAI, Anthropic, Gemini, Ollama, llama.cpp；任何 LiteLLM 支持的提供商 | 面向科学文献的高精度 RAG 系统。动态检索全文论文并迭代优化回答。发表于 ICLR。 |
| [local-deep-research](https://github.com/LearningCircuit/local-deep-research) | <img src="https://img.shields.io/github/stars/LearningCircuit/local-deep-research?style=for-the-badge" height="36"> | **LangChain** + **LangGraph**, FastAPI, FAISS, SQLCipher, SearXNG | Ollama, LM Studio, llama.cpp（本地）; OpenAI, Anthropic, Gemini, OpenRouter | 本地优先 deep research agent，使用本地 LLM 在 SimpleQA 达 ~95%。集成 arXiv/PubMed/Semantic Scholar/Wikipedia 等 10+ 搜索源，加密存储。 |
| [DeepResearchAgent](https://github.com/SkyworkAI/DeepResearchAgent) | <img src="https://img.shields.io/github/stars/SkyworkAI/DeepResearchAgent?style=for-the-badge" height="36"> | 自研（Autogenesis 自演化协议），MMEngine 配置 | OpenRouter（多模型访问） | 昆仑万维出品。层级多智能体系统，顶层规划智能体协调多个专业化底层智能体。 |
| [Auto-Deep-Research](https://github.com/HKUDS/Auto-Deep-Research) | <img src="https://img.shields.io/github/stars/HKUDS/Auto-Deep-Research?style=for-the-badge" height="36"> | AutoAgent 框架 + **LiteLLM**, Docker | Anthropic, OpenAI, Gemini, Mistral, Groq, OpenRouter, DeepSeek；任何 OpenAI 兼容 | OpenAI Deep Research 的开源替代。通用 LLM 兼容，零配置启动。GAIA Benchmark 表现优异。 |
| [OpenScholar](https://github.com/AkariAsai/OpenScholar) | <img src="https://img.shields.io/github/stars/AkariAsai/OpenScholar?style=for-the-badge" height="36"> | 自研 RAG（PyTorch, HuggingFace, Contriever） | OpenAI (GPT-4o), Llama 3.1 8B（自部署）；Semantic Scholar API, You.com | 检索增强语言模型，搜索 4500 万篇论文。发表于 Nature。超越 PaperQA2 和 Perplexity Pro。 |
| [OpenResearcher](https://github.com/TIGER-AI-Lab/OpenResearcher) | <img src="https://img.shields.io/github/stars/TIGER-AI-Lab/OpenResearcher?style=for-the-badge" height="36"> | Megatron-LM（训练）, vLLM（部署）, HuggingFace, Tevatron, BM25 + Qwen3-Embedding, Serper | OpenResearcher-30B-A3B（开源权重）; OpenAI API（评分） | 完全开源的长周期 deep research 训练 + 推理 pipeline，发布 30B-A3B 开源模型，在 BrowseComp-Plus 上超越 GPT-4.1 和 Claude Opus 4。 |

## ⚙️ 研究实现与实验

> 用于实现研究想法、编排实验并进行迭代优化的编码、调度与实验系统。

| 项目 | Stars | 框架 / 工具 | 支持的 LLM API | 简介 |
|------|-------|-------------|----------------|------|
| [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | <img src="https://img.shields.io/github/stars/Significant-Gravitas/AutoGPT?style=for-the-badge" height="36"> | 自研（Agent Builder, 工作流模块），Docker | OpenAI, Anthropic, Groq, Llama, AI/ML API（300+ 模型） | 最早的自主 AI 智能体框架之一。包含 Forge（智能体创建）、基准测试套件和用户界面。 |
| [OpenHands](https://github.com/OpenHands/OpenHands) | <img src="https://img.shields.io/github/stars/OpenHands/OpenHands?style=for-the-badge" height="36"> | 自研智能体框架，可组合 Python 库 | Anthropic Claude, OpenAI GPT, MiniMax；任何 LLM | AI 驱动的软件开发平台。自主编码智能体可编辑文件、运行命令、浏览网页。SWE-Bench Verified 达 72%。 |
| [Aider](https://github.com/Aider-AI/aider) | <img src="https://img.shields.io/github/stars/Aider-AI/aider?style=for-the-badge" height="36"> | 自研（AI 结对编程 CLI），Git 集成 | Anthropic Claude, OpenAI, DeepSeek, OpenRouter, Ollama；几乎任何 LLM | 终端中的 AI 结对编程。支持多文件编辑、Git 集成。广泛用作研究流水线中的编码基础设施。 |
| [SWE-agent](https://github.com/SWE-agent/SWE-agent) | <img src="https://img.shields.io/github/stars/SWE-agent/SWE-agent?style=for-the-badge" height="36"> | 自研（YAML 配置驱动），面向研究场景 | OpenAI (GPT-4o), Anthropic (Sonnet 4, Claude 3.7)；可配置 | 普林斯顿出品。将 LLM 转化为修复真实 GitHub Issue 的软件工程智能体。开创 SWE-Bench 基准。 |
| [DeepCode](https://github.com/HKUDS/DeepCode) | <img src="https://img.shields.io/github/stars/HKUDS/DeepCode?style=for-the-badge" height="36"> | 多智能体代码生成、MCP、沙箱执行 | OpenAI, Anthropic, Gemini, OpenRouter；OpenAI 兼容 API | 面向科研与软件任务的 agentic 编码平台，其中 Paper2Code 工作流可将技术论文转化为可执行实现。 |
| [ClawTeam](https://github.com/HKUDS/ClawTeam) | <img src="https://img.shields.io/github/stars/HKUDS/ClawTeam?style=for-the-badge" height="36"> | 多智能体集群、Git worktrees、共享任务状态、隔离沙箱 | Claude Code, Codex, OpenClaw, Cursor, Gemini CLI 等编码 agent | 面向并行科研实验的集群编排基础设施；其 autoresearch 工作流可协调大量隔离 agent 和 GPU 实验。 |
| [Paper2Code](https://github.com/going-doer/Paper2Code) | <img src="https://img.shields.io/github/stars/going-doer/Paper2Code?style=for-the-badge" height="36"> | 多智能体规划、分析与代码生成；vLLM | OpenAI (o3-mini)；经 vLLM 使用开源权重模型 | ICLR 2026。通过规划、分析与生成 agent，将机器学习论文转化为可运行代码库。 |
| [Paper2Agent](https://github.com/jmiao24/Paper2Agent) | <img src="https://img.shields.io/github/stars/jmiao24/Paper2Agent?style=for-the-badge" height="36"> | Claude Code, MCP, 论文/代码库分析 | Anthropic Claude | 将研究论文及其代码库转化为交互式 MCP agent，把方法、数据和工作流暴露为可调用工具。 |
| [MLE-agent](https://github.com/MLSysOps/MLE-agent) | <img src="https://img.shields.io/github/stars/MLSysOps/MLE-agent?style=for-the-badge" height="36"> | Python, Kaggle 集成, arXiv, Papers with Code | OpenAI, Anthropic Claude, Ollama (Llama3), Mistral | ML 工程与研究的智能伴侣。集成 arXiv 和 Papers with Code，提供更好的代码/研究计划。自动调试。 |
| [AIDE](https://github.com/WecoAI/aideml) | <img src="https://img.shields.io/github/stars/WecoAI/aideml?style=for-the-badge" height="36"> | Python, Streamlit, Docker | OpenAI (GPT-4-turbo/4o), Anthropic Claude, Gemini, Ollama（本地） | AI 驱动的代码空间探索。LLM agent 通过树搜索编写、评估和改进 ML 代码。[[论文]](https://arxiv.org/abs/2502.13138) Kaggle 奖牌数是最佳线性 agent 的 4 倍。托管平台：[Weco AI](https://weco.ai)。 |
| [Kapso](https://github.com/Leeroo-AI/kapso) | <img src="https://img.shields.io/github/stars/Leeroo-AI/kapso?style=for-the-badge" height="36"> | Python, Claude Code / Codex CLI, git worktrees, MCP | Claude（通过 Claude Code）、OpenAI（通过 Codex CLI） | 自我改进的 AI 软件工厂（面向可量化目标）。开源系统中 MLE-Bench 第一；ALE-Bench；RelBench。 [文档](https://docs.leeroo.com/docs) |
| [CORAL](https://github.com/Human-Agent-Society/CORAL) | <img src="https://img.shields.io/github/stars/Human-Agent-Society/CORAL?style=for-the-badge" height="36"> | 多智能体 worktrees、评分器、共享状态、可选 **LiteLLM** | Claude Code, Codex, Cursor；LiteLLM 支持的模型 | 自我进化研究 agent 基础设施：并行 worktrees、自动评分、发现共享和 autoresearch 风格实验循环。 |

## ✍️ 学术写作与传播

> 聚焦于科学成果阅读、润色、配图、展示与审稿回复的工具。

| 项目 | Stars | 框架 / 工具 | 支持的 LLM API | 简介 |
|------|-------|-------------|----------------|------|
| [ChatPaper](https://github.com/kaixindelele/ChatPaper) | <img src="https://img.shields.io/github/stars/kaixindelele/ChatPaper?style=for-the-badge" height="36"> | PyMuPDF, arxiv.py, Flask, Docker | OpenAI (GPT-3.5/4) | 用 ChatGPT 总结 arXiv 论文、专业翻译、润色论文、分析审稿意见并起草回复。 |
| [PaperBanana](https://github.com/dwzhu-pku/PaperBanana) | <img src="https://img.shields.io/github/stars/dwzhu-pku/PaperBanana?style=for-the-badge" height="36"> | Streamlit, OpenRouter | OpenAI, Anthropic, Gemini（经 OpenRouter） | 参考驱动的多智能体学术插图生成框架，由五个专用 agent 生成出版级图表。 |
| [Paper2Poster](https://github.com/Paper2Poster/Paper2Poster) | <img src="https://img.shields.io/github/stars/Paper2Poster/Paper2Poster?style=for-the-badge" height="36"> | 多智能体流水线、可编辑 PowerPoint 输出、vLLM | GPT-4o；经 vLLM 使用开源权重模型 | NeurIPS 2025。将论文 PDF 转换为可编辑学术海报（`.pptx`），同时提供完整流水线和轻量编码 agent skill。 |
| [ChatReviewer](https://github.com/nishiwen1214/ChatReviewer) | <img src="https://img.shields.io/github/stars/nishiwen1214/ChatReviewer?style=for-the-badge" height="36"> | Python, tiktoken, Docker, HuggingFace Spaces | OpenAI (GPT-3.5/4) | 用 ChatGPT 分析论文优缺点、提供改进建议并起草审稿人回复。ChatPaper 姊妹项目。 |

## 🔧 研究 Skills 与插件合集

> 可复用的 skill 集合和插件生态，集成到编码 agent（Claude Code、Codex、Gemini CLI 等）中以实现研究工作流。

| 项目 | Stars | 框架 / 工具 | 支持的 LLM API | 简介 |
|------|-------|-------------|----------------|------|
| [scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | <img src="https://img.shields.io/github/stars/K-Dense-AI/scientific-agent-skills?style=for-the-badge" height="36"> | PyTorch Lightning, scikit-learn, BioPython, RDKit, DeepChem, Scanpy, OpenMM | Agent 无关（Claude Code, Cursor, Codex, Gemini CLI） | 150 个即用型科学 skills，覆盖生物信息学、药物发现、临床研究、医学影像和材料科学。 |
| [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-research-SKILLs) | <img src="https://img.shields.io/github/stars/Orchestra-Research/AI-research-SKILLs?style=for-the-badge" height="36"> | DeepSpeed, vLLM, LangChain, W&B, MLflow 等 80+ 框架 | Agent 无关（Claude Code, Codex, Gemini CLI, Qwen Code） | 98 个 skills，覆盖 23 个类别，贯穿 AI 研究全生命周期：文献综述、想法生成、实验和论文撰写。 |
| [OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills) | <img src="https://img.shields.io/github/stars/FreedomIntelligence/OpenClaw-Medical-Skills?style=for-the-badge" height="36"> | BioPython, GATK, Scanpy, RDKit, DeepChem, OpenMM, AlphaFold, pysam, MDAnalysis | 基于 Claude 的 agent（经 **OpenClaw** / **NanoClaw** 框架） | 869 个医学 AI skills，覆盖临床报告、基因组学、药物发现、生信、结构生物学和生医数据库。 |

## 📋 Awesome Lists 与综述

> 自动化科研领域的精选集合和综述论文。

| 项目 | Stars | 简介 |
|------|-------|------|
| [awesome-autoresearch](https://github.com/webfuse-com/awesome-autoresearch) | <img src="https://img.shields.io/github/stars/webfuse-com/awesome-autoresearch?style=for-the-badge" height="36"> | Karpathy autoresearch 风格的自主改进循环、研究 agent 与衍生系统精选索引，50+ 条目。 |
| [awesome-ai-for-science](https://github.com/ai4s-research/awesome-ai-for-science) | <img src="https://img.shields.io/github/stars/ai4s-research/awesome-ai-for-science?style=for-the-badge" height="36"> | AI for Science 工具、库、论文、数据集和框架的精选列表，覆盖物理、化学、生物和材料科学等领域。 |
| [Autonomous-Agents](https://github.com/tmgthb/Autonomous-Agents) | <img src="https://img.shields.io/github/stars/tmgthb/Autonomous-Agents?style=for-the-badge" height="36"> | 每日更新的自主 LLM Agent 研究论文合集，覆盖多智能体系统、科学计算、机器人等领域。 |
| [Awesome-Deep-Research](https://github.com/DavidZWZ/Awesome-Deep-Research) | <img src="https://img.shields.io/github/stars/DavidZWZ/Awesome-Deep-Research?style=for-the-badge" height="36"> | Deep research agent 精选合集 —— 涵盖产业界产品、开源实现、70+ 最新论文、评测基准和 2026 年 agent 系统。 |

---

## 💡 本列表与通用 AI Agent 列表的区别

本列表专注于**自动化科研流程**，而非通用 AI 智能体。我们收录的项目覆盖研究生命周期的一个或多个阶段：

```
📖 文献综述 → 💡 想法生成 → 🔍 新颖性检验 → 📐 实验设计 →
💻 代码实现 → 🚀 实验执行 → 📊 结果分析 → ✍️ 论文撰写 → 📝 同行评审
```

通用编码智能体（OpenHands、Aider、SWE-agent）被收录是因为它们是实验执行阶段的关键基础设施。

---

## 🤝 贡献指南

欢迎提交 PR！请确保项目：
- 拥有 **500+ GitHub stars**
- 与自动化科研直接相关
- 开源且仓库活跃

请按每个分类中的 star 数降序排列。

---

## 📈 Star 趋势

[![Star History Chart](https://api.star-history.com/svg?repos=karpathy/autoresearch,SakanaAI/AI-Scientist,microsoft/RD-Agent,aiming-lab/AutoResearchClaw,kaixindelele/ChatPaper,snap-stanford/Biomni,EvoScientist/EvoScientist,ResearAI/DeepScientist,InternScience/InternAgent,bytedance/deer-flow,stanford-oval/storm,assafelovic/gpt-researcher,Alibaba-NLP/DeepResearch,LearningCircuit/local-deep-research,skyllwt/AutoSci,OpenRaiser/NanoResearch,going-doer/Paper2Code,Future-House/robin&type=Date)](https://star-history.com/#karpathy/autoresearch&SakanaAI/AI-Scientist&microsoft/RD-Agent&aiming-lab/AutoResearchClaw&kaixindelele/ChatPaper&snap-stanford/Biomni&EvoScientist/EvoScientist&ResearAI/DeepScientist&InternScience/InternAgent&bytedance/deer-flow&stanford-oval/storm&assafelovic/gpt-researcher&Alibaba-NLP/DeepResearch&LearningCircuit/local-deep-research&skyllwt/AutoSci&OpenRaiser/NanoResearch&going-doer/Paper2Code&Future-House/robin&Date)

---

## 📄 许可证

[CC0 1.0 Universal](LICENSE)
