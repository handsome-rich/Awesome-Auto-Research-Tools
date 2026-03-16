# 🔬 Awesome Auto Research [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[English](README.md) | [中文](README_CN.md)

<p align="center">
  <img src="fig/banner_cn.jpg" alt="开源科研自动化项目精选" width="800">
</p>

> 🤖 精选的自动化科研开源项目列表 —— 覆盖文献综述、想法生成、实验执行、论文撰写与同行评审全流程。

**📅 Star 数据最后验证时间：2026-03-16**

---

## 📑 目录

- [🧪 端到端自主研究系统](#-端到端自主研究系统)
- [📚 深度调研与文献综合](#-深度调研与文献综合)
- [⚙️ 自动化实验与代码智能体](#️-自动化实验与代码智能体)
- [📋 Awesome Lists 与综述](#-awesome-lists-与综述)
- [💡 本列表与通用 AI Agent 列表的区别](#-本列表与通用-ai-agent-列表的区别)
- [🤝 贡献指南](#-贡献指南)

---

## 🧪 端到端自主研究系统

> 自动化完整研究生命周期：想法 → 实验 → 论文。

| 项目 | Stars | 框架 / 工具 | 支持的 LLM API | 简介 |
|------|-------|-------------|----------------|------|
| [autoresearch](https://github.com/karpathy/autoresearch) | <img src="https://img.shields.io/github/stars/karpathy/autoresearch?style=for-the-badge" height="36"> | 自研（PyTorch, nanochat） | Anthropic Claude, OpenAI Codex | Andrej Karpathy 出品。630 行 AI 智能体，自主阅读训练脚本、提出假设、修改代码、运行实验并评估结果 —— 一夜跑数百个实验。 |
| [AI-Scientist](https://github.com/SakanaAI/AI-Scientist) | <img src="https://img.shields.io/github/stars/SakanaAI/AI-Scientist?style=for-the-badge" height="36"> | 自研（模板系统, LaTeX 流水线） | OpenAI, Anthropic Claude, DeepSeek, Gemini, OpenRouter, 开源模型 | 首个全自动开放式科学发现系统。自动完成想法生成、编码、实验运行和完整论文撰写。 |
| [Agent Laboratory](https://github.com/SamuelSchmidgall/AgentLaboratory) | <img src="https://img.shields.io/github/stars/SamuelSchmidgall/AgentLaboratory?style=for-the-badge" height="36"> | 自研多智能体（arXiv, HuggingFace, LaTeX） | OpenAI (o1/o3/GPT-4o), DeepSeek | 端到端自主研究工作流，包含文献综述、实验和报告撰写的专用智能体。 |
| [AI-Researcher](https://github.com/HKUDS/AI-Researcher) | <img src="https://img.shields.io/github/stars/HKUDS/AI-Researcher?style=for-the-badge" height="36"> | 自研 + **LiteLLM**, Docker, Gradio | Anthropic, OpenAI, Gemini, DeepSeek, OpenRouter, GitHub AI（经 LiteLLM） | NeurIPS 2025 Spotlight。完全自主系统，覆盖文献综述、假设生成、算法实现和可投稿论文准备。 |
| [Biomni](https://github.com/snap-stanford/Biomni) | <img src="https://img.shields.io/github/stars/snap-stanford/Biomni?style=for-the-badge" height="36"> | 生物医学自研智能体 + 代码执行、数据湖、know-how 知识库 | Anthropic Claude, OpenAI, Azure OpenAI, Gemini, Groq, AWS Bedrock, 自定义 OpenAI 兼容 API | 斯坦福出品。通用生物医学 AI 智能体，可在生物与医学研究中自主执行任务，结合 LLM 推理、检索增强与工具/代码调用。 |
| [AI-Scientist-v2](https://github.com/SakanaAI/AI-Scientist-v2) | <img src="https://img.shields.io/github/stars/SakanaAI/AI-Scientist-v2?style=for-the-badge" height="36"> | 自研（BFTS 智能体树搜索, AIDE） | OpenAI (o1/o3/GPT-4o), Anthropic (Bedrock), Gemini | AI-Scientist 升级版。首篇完全由 AI 撰写并通过同行评审被接收的 Workshop 论文。 |
| [ARIS](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | <img src="https://img.shields.io/github/stars/wanshuiyin/Auto-claude-code-research-in-sleep?style=for-the-badge" height="36"> | **Claude Code** + MCP（Codex, llm-chat, Zotero, Obsidian） | Anthropic Claude, OpenAI GPT, GLM-5, MiniMax, Kimi, Qwen, DeepSeek, LongCat；任何 OpenAI 兼容 API | Claude Code skills 套件，用于自主 ML 研究：跨模型评审循环、想法发现流水线、实验自动化与论文撰写。 |

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
| [DeepResearchAgent](https://github.com/SkyworkAI/DeepResearchAgent) | <img src="https://img.shields.io/github/stars/SkyworkAI/DeepResearchAgent?style=for-the-badge" height="36"> | 自研（Autogenesis 自演化协议），MMEngine 配置 | OpenRouter（多模型访问） | 昆仑万维出品。层级多智能体系统，顶层规划智能体协调多个专业化底层智能体。 |
| [OpenScholar](https://github.com/AkariAsai/OpenScholar) | <img src="https://img.shields.io/github/stars/AkariAsai/OpenScholar?style=for-the-badge" height="36"> | 自研 RAG（PyTorch, HuggingFace, Contriever） | OpenAI (GPT-4o), Llama 3.1 8B（自部署）；Semantic Scholar API, You.com | 检索增强语言模型，搜索 4500 万篇论文。发表于 Nature。超越 PaperQA2 和 Perplexity Pro。 |
| [Idea2Paper](https://github.com/AgentAlphaAGI/Idea2Paper) | <img src="https://img.shields.io/github/stars/AgentAlphaAGI/Idea2Paper?style=for-the-badge" height="36"> | 自研AgentAlpha 框架 (多智能体协作), 向量数据库, 知识图谱 (KG) | DeepSeek V3/R1, Claude 3.5, GPT-4o; Semantic Scholar, ArXiv API | 专业科研灵感探索引擎：通过多 Agent 协同进行深度文献挖掘与知识图谱对齐，能够将朴素的idea进行新颖性包装、辅助研究者从零构建结构化课题方案。 |

## ⚙️ 自动化实验与代码智能体

> 自动化编码、实验执行和迭代优化。这些项目是自动化研究系统的"双手"。

| 项目 | Stars | 框架 / 工具 | 支持的 LLM API | 简介 |
|------|-------|-------------|----------------|------|
| [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | <img src="https://img.shields.io/github/stars/Significant-Gravitas/AutoGPT?style=for-the-badge" height="36"> | 自研（Agent Builder, 工作流模块），Docker | OpenAI, Anthropic, Groq, Llama, AI/ML API（300+ 模型） | 最早的自主 AI 智能体框架之一。包含 Forge（智能体创建）、基准测试套件和用户界面。 |
| [OpenHands](https://github.com/All-Hands-AI/OpenHands) | <img src="https://img.shields.io/github/stars/All-Hands-AI/OpenHands?style=for-the-badge" height="36"> | 自研智能体框架，可组合 Python 库 | Anthropic Claude, OpenAI GPT, MiniMax；任何 LLM | AI 驱动的软件开发平台。自主编码智能体可编辑文件、运行命令、浏览网页。SWE-Bench Verified 达 72%。 |
| [Aider](https://github.com/Aider-AI/aider) | <img src="https://img.shields.io/github/stars/Aider-AI/aider?style=for-the-badge" height="36"> | 自研（AI 结对编程 CLI），Git 集成 | Anthropic Claude, OpenAI, DeepSeek, OpenRouter, Ollama；几乎任何 LLM | 终端中的 AI 结对编程。支持多文件编辑、Git 集成。广泛用作研究流水线中的编码基础设施。 |
| [SWE-agent](https://github.com/SWE-agent/SWE-agent) | <img src="https://img.shields.io/github/stars/SWE-agent/SWE-agent?style=for-the-badge" height="36"> | 自研（YAML 配置驱动），面向研究场景 | OpenAI (GPT-4o), Anthropic (Sonnet 4, Claude 3.7)；可配置 | 普林斯顿出品。将 LLM 转化为修复真实 GitHub Issue 的软件工程智能体。开创 SWE-Bench 基准。 |

## 📋 Awesome Lists 与综述

> 自动化科研领域的精选集合和综述论文。

| 项目 | Stars | 简介 |
|------|-------|------|
| [awesome-ai-for-science](https://github.com/ai-boost/awesome-ai-for-science) | <img src="https://img.shields.io/github/stars/ai-boost/awesome-ai-for-science?style=for-the-badge" height="36"> | AI for Science 工具、库、论文、数据集和框架的精选列表，覆盖物理、化学、生物和材料科学等领域。 |

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
- 拥有 **1,000+ GitHub stars**（或是在顶级会议发表、特别知名的项目）
- 与自动化科研直接相关
- 开源且仓库活跃

请按每个分类中的 star 数降序排列。

---

## 📈 Star 趋势

[![Star History Chart](https://api.star-history.com/svg?repos=karpathy/autoresearch,SakanaAI/AI-Scientist,bytedance/deer-flow,stanford-oval/storm,assafelovic/gpt-researcher,Alibaba-NLP/DeepResearch,langchain-ai/open_deep_research&type=Date)](https://star-history.com/#karpathy/autoresearch&SakanaAI/AI-Scientist&bytedance/deer-flow&stanford-oval/storm&assafelovic/gpt-researcher&Alibaba-NLP/DeepResearch&langchain-ai/open_deep_research&Date)

---

## 📄 许可证

[CC0 1.0 Universal](LICENSE)
