<h1 align="center">🔬 Awesome Auto Research</h1>

<p align="center">
  精选开源自动化科研项目，覆盖文献综述、想法生成、实验执行、论文撰写与同行评审。
</p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
  &nbsp;·&nbsp; <a href="README.md">English</a>
  &nbsp;·&nbsp; <a href="README_CN.md">中文</a>
  &nbsp;·&nbsp; <a href="#-目录">浏览工具</a>
  &nbsp;·&nbsp; <a href="#-贡献指南">参与贡献</a>
</p>

<p align="center">
  <img src="fig/banner_research.jpg" alt="科学研究流程插画，涵盖文献阅读、实验与论文撰写" width="800">
</p>

<sub>**📅 Star 数据最后验证时间：2026-10-07**</sub>

---

## 📑 目录

<table width="100%">
  <tr>
    <td align="center" width="33%"><a href="#-自主研究系统"><b>🧪 自主研究系统</b></a><br><sub>20 个项目 · 想法、实验与论文</sub></td>
    <td align="center" width="33%"><a href="#-深度调研与文献综合"><b>📚 深度调研与文献综合</b></a><br><sub>10 个项目 · 检索、阅读与综述</sub></td>
    <td align="center" width="33%"><a href="#️-研究实现与实验"><b>⚙️ 研究实现与实验</b></a><br><sub>11 个项目 · 编码、运行与优化</sub></td>
  </tr>
  <tr>
    <td align="center" width="33%"><a href="#️-学术写作与传播"><b>✍️ 学术写作与传播</b></a><br><sub>4 个项目 · 写作、配图与审稿</sub></td>
    <td align="center" width="33%"><a href="#-研究-skills-与插件合集"><b>🔧 研究 Skills 与插件合集</b></a><br><sub>3 个项目 · 扩展研究 agent</sub></td>
    <td align="center" width="33%"><a href="#-awesome-lists-与综述"><b>📋 Awesome Lists 与综述</b></a><br><sub>4 个项目 · 浏览研究工具全景</sub></td>
  </tr>
</table>

---

## 🧪 自主研究系统

> 自主完成科研闭环中多个阶段的系统，例如假设生成、实验、分析和论文准备。

| 项目与 Stars | 简介 | 框架与 LLM API |
|---|---|---|
| [autoresearch](https://github.com/karpathy/autoresearch)<br><img src="https://img.shields.io/github/stars/karpathy/autoresearch?style=flat" alt="GitHub stars" height="20"> | Andrej Karpathy 出品的极简单 GPU 研究框架：外部编码 agent 按 `program.md` 指令反复修改 `train.py`，并运行固定五分钟的 nanochat 实验。 | <b>工具:</b> 自研（PyTorch, nanochat）<br><b>接入:</b> Anthropic Claude Code、OpenAI Codex 等外部编码 agent |
| [ARIS](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)<br><img src="https://img.shields.io/github/stars/wanshuiyin/Auto-claude-code-research-in-sleep?style=flat" alt="GitHub stars" height="20"> | 科研工作流 skills，支持独立跨模型评审循环、持久研究记忆、想法发现、实验自动化、证明审查与论文撰写，同时提供独立 CLI。 | <b>工具:</b> **Claude Code** / Codex CLI skills 与插件、ARIS-Code CLI、MCP、Zotero、Obsidian<br><b>接入:</b> Anthropic Claude, OpenAI Codex；经 OpenAI 兼容 API 配置其他执行/评审模型 |
| [RD-Agent](https://github.com/microsoft/RD-Agent)<br><img src="https://img.shields.io/github/stars/microsoft/RD-Agent?style=flat" alt="GitHub stars" height="20"> | 微软出品。面向数据科学的研发 agent，支持量化因子/模型演化、Kaggle 自动化、论文到代码实现和 LLM 微调。 | <b>工具:</b> 自研 + **LiteLLM**, Docker, Qlib<br><b>接入:</b> OpenAI, Azure OpenAI, DeepSeek；LiteLLM 支持的提供商 |
| [AI-Scientist](https://github.com/SakanaAI/AI-Scientist)<br><img src="https://img.shields.io/github/stars/SakanaAI/AI-Scientist?style=flat" alt="GitHub stars" height="20"> | 基于研究模板的科学发现系统，自动完成想法生成、编码、实验、论文撰写和评审。 | <b>工具:</b> 自研（模板系统, LaTeX 流水线）<br><b>接入:</b> OpenAI, Anthropic Claude, DeepSeek, Gemini, OpenRouter, 开源模型 |
| [AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw)<br><img src="https://img.shields.io/github/stars/aiming-lab/AutoResearchClaw?style=flat" alt="GitHub stars" height="20"> | 23 阶段自主或人在回路科研流水线：idea → 文献 → 领域专用实验 → 多 agent 评审 → LaTeX 论文，支持六种干预模式。 | <b>工具:</b> 自研流水线、**OpenClaw** / ACP、Docker、LaTeX、OpenAlex、Semantic Scholar<br><b>接入:</b> OpenAI 兼容 API（OpenRouter, DeepSeek, MiniMax）；ACP 兼容编码 agent |
| [AI-Scientist-v2](https://github.com/SakanaAI/AI-Scientist-v2)<br><img src="https://img.shields.io/github/stars/SakanaAI/AI-Scientist-v2?style=flat" alt="GitHub stars" height="20"> | 无需预编写研究模板的科学发现系统，通过渐进式 agentic 树搜索生成假设、执行实验、分析结果并撰写论文。 | <b>工具:</b> 自研（BFTS 智能体树搜索, AIDE）<br><b>接入:</b> OpenAI, Anthropic Claude（AWS Bedrock）, Gemini |
| [Agent Laboratory](https://github.com/SamuelSchmidgall/AgentLaboratory)<br><img src="https://img.shields.io/github/stars/SamuelSchmidgall/AgentLaboratory?style=flat" alt="GitHub stars" height="20"> | 端到端自主研究工作流，包含文献综述、实验和报告撰写的专用智能体。 | <b>工具:</b> 自研多智能体（arXiv, HuggingFace, LaTeX）<br><b>接入:</b> OpenAI (o1/o3/GPT-4o), DeepSeek |
| [AI-Researcher](https://github.com/HKUDS/AI-Researcher)<br><img src="https://img.shields.io/github/stars/HKUDS/AI-Researcher?style=flat" alt="GitHub stars" height="20"> | NeurIPS 2025 Spotlight。完全自主系统，覆盖文献综述、假设生成、算法实现和可投稿论文准备。 | <b>工具:</b> 自研 + **LiteLLM**, Docker, Gradio<br><b>接入:</b> OpenAI, Anthropic, Gemini, DeepSeek, OpenRouter；LiteLLM 支持的提供商 |
| [claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar)<br><img src="https://img.shields.io/github/stars/Galaxy-Dawn/claude-scholar?style=flat" alt="GitHub stars" height="20"> | 半自动学术研究助手，覆盖文献综述、编码、实验、写作、投稿和项目知识管理，为不同编码 agent 提供独立分支。 | <b>工具:</b> **Claude Code** / Codex CLI / Kimi Code CLI / OpenCode, Zotero MCP, Obsidian, LaTeX<br><b>接入:</b> Anthropic Claude, OpenAI（Codex）, Moonshot Kimi；OpenCode 配置的提供商 |
| [EvoScientist](https://github.com/EvoScientist/EvoScientist)<br><img src="https://img.shields.io/github/stars/EvoScientist/EvoScientist?style=flat" alt="GitHub stars" height="20"> | 自我进化的科研助手，由六个子 agent 分工规划、调研、编码、调试、分析和写作；持久记忆与可复用 skills 可在 CLI/TUI、WebUI 和消息通道间使用。 | <b>工具:</b> **LangChain** + **LangGraph** + DeepAgents, MCP, Docker<br><b>接入:</b> Anthropic, OpenAI, Google Gemini, DeepSeek, MiniMax, NVIDIA NIM, OpenRouter；可配置提供商 |
| [Biomni](https://github.com/snap-stanford/Biomni)<br><img src="https://img.shields.io/github/stars/snap-stanford/Biomni?style=flat" alt="GitHub stars" height="20"> | 斯坦福出品。通用生物医学 AI 智能体，可在生物与医学研究中自主执行任务，结合 LLM 推理、检索增强与工具/代码调用。 | <b>工具:</b> 生物医学自研智能体 + 代码执行、数据湖、know-how 知识库<br><b>接入:</b> Anthropic, OpenAI, Azure OpenAI, Gemini, Groq, AWS Bedrock, Ollama；自定义 OpenAI 兼容 API |
| [DeepScientist](https://github.com/ResearAI/DeepScientist)<br><img src="https://img.shields.io/github/stars/ResearAI/DeepScientist?style=flat" alt="GitHub stars" height="20"> | Local-first 自主研究 studio。Findings Memory 与贝叶斯优化编排基线复现 → 分支实验 → LaTeX 论文草稿。 | <b>工具:</b> 自研（贝叶斯优化、Findings Memory、Research Map），Git worktrees, LaTeX<br><b>接入:</b> Codex CLI, Claude Code, Kimi Code, OpenCode |
| [DATAGEN](https://github.com/zi-yue-1129/DATAGEN)<br><img src="https://img.shields.io/github/stars/zi-yue-1129/DATAGEN?style=flat" alt="GitHub stars" height="20"> | AI 驱动的多智能体研究助手，自动完成假设生成、数据分析、可视化和报告撰写。 | <b>工具:</b> **LangChain** + **LangGraph**、MCP、可复用 skills、Firecrawl / fastCRW<br><b>接入:</b> OpenAI, Anthropic, Gemini, Ollama, Groq, Atlas Cloud, OrcaRouter |
| [AutoSci](https://github.com/skyllwt/AutoSci)<br><img src="https://img.shields.io/github/stars/skyllwt/AutoSci?style=flat" alt="GitHub stars" height="20"> | 以持久记忆为核心的科研系统，覆盖文献综述、构思、实验、分析和写作，新增引导式方法迭代，并提供独立 Codex/OpenCode 预览分支。 | <b>工具:</b> 记忆中心式 agent 框架、持久化知识图谱、Web 仪表盘<br><b>接入:</b> Claude Code；预览支持 Codex 和 OpenCode |
| [Idea2Paper](https://github.com/AgentAlphaAGI/Idea2Paper)<br><img src="https://img.shields.io/github/stars/AgentAlphaAGI/Idea2Paper?style=flat" alt="GitHub stars" height="20"> | 其 Idea2Story 模块构建文献知识图谱、检索研究模式，并通过锚定多 agent 评审将原始 idea 完善为结构化科研叙事。 | <b>工具:</b> 自研多 agent 流水线、知识图谱、embedding 检索、锚定评审<br><b>接入:</b> 可配置 LLM 端点与 OpenAI 兼容 embeddings API |
| [InternAgent](https://github.com/InternScience/InternAgent)<br><img src="https://img.shields.io/github/stars/InternScience/InternAgent?style=flat" alt="GitHub stars" height="20"> | 上海 AI Lab 出品。InternAgent-1.5 编排假设生成、实验、科学论文复现和深度调研，跨研究轮次保留持久记忆。 | <b>工具:</b> 自研科学发现/深度调研流水线、编码 agent 实验后端、持久记忆<br><b>接入:</b> OpenAI 兼容 API, OpenRouter, Anthropic Claude |
| [NanoResearch](https://github.com/OpenRaiser/NanoResearch)<br><img src="https://img.shields.io/github/stars/OpenRaiser/NanoResearch?style=flat" alt="GitHub stars" height="20"> | 从 idea 到论文的端到端流水线，可在本地或 SLURM 执行真实实验；Evo 模式跨研究轮次调整可复用 skills、记忆和路由。 | <b>工具:</b> 九阶段流水线、Evo skills/记忆/策略循环、本地/SLURM 执行、LaTeX<br><b>接入:</b> OpenAI 兼容 API；Claude Code |
| [K-Dense BYOK](https://github.com/K-Dense-AI/k-dense-byok)<br><img src="https://img.shields.io/github/stars/K-Dense-AI/k-dense-byok?style=flat" alt="GitHub stars" height="20"> | 本地 AI 科研协作者，支持文献、数据分析、代码执行、图表和报告；提供 181 个科学 skills，以哈希链实验日志记录执行步骤与产物。 | <b>工具:</b> 本地优先工作区、Pi agent 运行时、科学 skills、专家 agent、MCP、Ollama<br><b>接入:</b> OpenRouter；OpenAI、Anthropic、Gemini 等直接 API；支持的订阅账户；Ollama / OpenAI 兼容本地服务 |
| [data-to-paper](https://github.com/Technion-Kishony-lab/data-to-paper)<br><img src="https://img.shields.io/github/stars/Technion-Kishony-lab/data-to-paper?style=flat" alt="GitHub stars" height="20"> | 将科研数据集转化为透明、可追溯、可验证的论文，由多个 agent 分工完成分析、解释、文献检索与写作。 | <b>工具:</b> 多智能体流水线、代码执行、LaTeX、Semantic Scholar<br><b>接入:</b> OpenAI API；可选 DeepInfra |
| [Robin](https://github.com/Future-House/robin)<br><img src="https://img.shields.io/github/stars/Future-House/robin?style=flat" alt="GitHub stars" height="20"> | FutureHouse 的多智能体科学发现系统，协同完成文献调研、数据分析与实验规划。 | <b>工具:</b> 多 agent 科学发现系统、**LiteLLM**、Edison 平台、Docker / Jupyter<br><b>接入:</b> LiteLLM 支持的提供商；Edison 平台提供文献与数据分析 agent |

[↑ 返回目录](#-目录)

## 📚 深度调研与文献综合

> 聚焦于自动信息收集、文献综述和报告生成。

| 项目与 Stars | 简介 | 框架与 LLM API |
|---|---|---|
| [DeerFlow](https://github.com/bytedance/deer-flow)<br><img src="https://img.shields.io/github/stars/bytedance/deer-flow?style=flat" alt="GitHub stars" height="20"> | 字节跳动出品。DeerFlow 2.0 super-agent 框架，用于调研、编码和报告，支持子 agent、持久记忆、可复用 skills、项目工作区与定时任务。 | <b>工具:</b> **LangChain** + **LangGraph**、MCP、可扩展 skills、沙箱、InfoQuest<br><b>接入:</b> OpenAI 兼容 API, OpenRouter, vLLM；Codex CLI 与 Claude Code 后端 |
| [STORM](https://github.com/stanford-oval/storm)<br><img src="https://img.shields.io/github/stars/stanford-oval/storm?style=flat" alt="GitHub stars" height="20"> | 斯坦福出品。LLM 驱动的知识管理系统，生成带引用的完整维基百科风格文章。支持 Co-STORM 人机协作。 | <b>工具:</b> **DSPy** + **LiteLLM**, Streamlit<br><b>接入:</b> LiteLLM 支持的提供商；网页搜索与自定义文档检索器 |
| [GPT Researcher](https://github.com/assafelovic/gpt-researcher)<br><img src="https://img.shields.io/github/stars/assafelovic/gpt-researcher?style=flat" alt="GitHub stars" height="20"> | 自主网页与本地文档调研 agent，生成可追溯来源的报告，支持 PDF/Word/Markdown 导出、多 agent 工作流和编码 agent skill。 | <b>工具:</b> **LangGraph** / AG2、MCP、Claude Skill、FastAPI、NextJS<br><b>接入:</b> OpenAI, Anthropic Claude, Gemini；任何 OpenAI 兼容 API |
| [Tongyi DeepResearch](https://github.com/Alibaba-NLP/DeepResearch)<br><img src="https://img.shields.io/github/stars/Alibaba-NLP/DeepResearch?style=flat" alt="GitHub stars" height="20"> | 阿里巴巴出品。面向长周期信息检索的 Tongyi-DeepResearch-30B-A3B 开源权重模型，支持 ReAct 和基于 IterResearch 的 heavy 推理模式。 | <b>工具:</b> 自研（ReAct, IterResearch, GRPO RL）；Serper, Jina, SandboxFusion<br><b>接入:</b> OpenAI 兼容, OpenRouter；通义-30B-A3B, Dashscope/百炼 |
| [Open Deep Research](https://github.com/langchain-ai/open_deep_research)<br><img src="https://img.shields.io/github/stars/langchain-ai/open_deep_research?style=flat" alt="GitHub stars" height="20"> | LangChain 出品。开源深度调研框架，可配置 MCP 工具和搜索 API。 | <b>工具:</b> **LangChain** + **LangGraph**, MCP, LangSmith<br><b>接入:</b> LangChain 支持的提供商（OpenAI, Anthropic, OpenRouter, Ollama）；需支持工具调用与结构化输出 |
| [PaperQA2](https://github.com/Future-House/paper-qa)<br><img src="https://img.shields.io/github/stars/Future-House/paper-qa?style=flat" alt="GitHub stars" height="20"> | 面向科学文献与本地文档的 agentic RAG，支持迭代检索、上下文摘要、引用，以及 PDF 文本、表格、图像和公式解析。 | <b>工具:</b> 自研 agentic RAG + **LiteLLM**、Pydantic、tantivy、多模态文档解析器<br><b>接入:</b> OpenAI, Anthropic, Gemini, Ollama, llama.cpp；任何 LiteLLM 支持的提供商 |
| [local-deep-research](https://github.com/LearningCircuit/local-deep-research)<br><img src="https://img.shields.io/github/stars/LearningCircuit/local-deep-research?style=flat" alt="GitHub stars" height="20"> | 本地优先的 agentic 调研系统，可动态选择网页与学术搜索引擎，提供可检索文档库、MCP 集成和按用户加密的存储。 | <b>工具:</b> **LangChain** + **LangGraph**, FastAPI, FAISS, SQLCipher, SearXNG<br><b>接入:</b> Ollama, LM Studio, llama.cpp；OpenAI, Anthropic, Gemini, OpenRouter, Requesty；兼容端点 |
| [Auto-Deep-Research](https://github.com/HKUDS/Auto-Deep-Research)<br><img src="https://img.shields.io/github/stars/HKUDS/Auto-Deep-Research?style=flat" alt="GitHub stars" height="20"> | 基于 AutoAgent 的深度调研助手，支持浏览器与文件工作流、可配置 LiteLLM 后端，以及支持或不支持 function-calling 的模型。 | <b>工具:</b> AutoAgent 框架 + **LiteLLM**, Docker<br><b>接入:</b> Anthropic, OpenAI, Gemini, Mistral, Groq, OpenRouter, DeepSeek；任何 OpenAI 兼容 |
| [OpenScholar](https://github.com/AkariAsai/OpenScholar)<br><img src="https://img.shields.io/github/stars/AkariAsai/OpenScholar?style=flat" alt="GitHub stars" height="20"> | 支持自反思生成与来源引用的检索增强科学问答系统，公开推理、检索器和 OpenScholar-8B 训练代码。 | <b>工具:</b> 自研 RAG、HuggingFace / PyTorch、torchtune 训练、检索器与重排器<br><b>接入:</b> OpenAI (GPT-4o), Llama 3.1 8B（自部署）；Semantic Scholar API, You.com |
| [OpenResearcher](https://github.com/TIGER-AI-Lab/OpenResearcher)<br><img src="https://img.shields.io/github/stars/TIGER-AI-Lab/OpenResearcher?style=flat" alt="GitHub stars" height="20"> | 公开的深度调研训练与推理方案，发布 OpenResearcher-30B-A3B 模型、96K agent 轨迹、浏览器工具和基准评估代码。 | <b>工具:</b> Megatron-LM（训练）, vLLM（部署）, HuggingFace, Tevatron, BM25 + Qwen3-Embedding, Serper<br><b>接入:</b> OpenResearcher-30B-A3B（开源权重）; OpenAI API（评分） |

[↑ 返回目录](#-目录)

## ⚙️ 研究实现与实验

> 用于实现研究想法、编排实验并进行迭代优化的编码、调度与实验系统。

| 项目与 Stars | 简介 | 框架与 LLM API |
|---|---|---|
| [OpenHands](https://github.com/OpenHands/OpenHands)<br><img src="https://img.shields.io/github/stars/OpenHands/OpenHands?style=flat" alt="GitHub stars" height="20"> | 面向编码 agent 与自动化任务的自托管开发控制中心。Agent Canvas 可连接本地、远程和云端运行环境，调度可复用工作流。 | <b>工具:</b> Agent Canvas, OpenHands Agent Server / SDK, ACP, Docker<br><b>接入:</b> 可配置 LLM 提供商；Claude Code, Codex, Gemini 及 ACP 兼容 agent |
| [Aider](https://github.com/Aider-AI/aider)<br><img src="https://img.shields.io/github/stars/Aider-AI/aider?style=flat" alt="GitHub stars" height="20"> | 终端中的 AI 结对编程。通过代码库映射获取上下文，支持多文件修改，并集成 Git、代码检查和测试。 | <b>工具:</b> AI 结对编程 CLI, **LiteLLM**，代码库映射，Git 集成<br><b>接入:</b> Anthropic, OpenAI, Gemini, DeepSeek, OpenRouter, Ollama；OpenAI 兼容 API |
| [SWE-agent](https://github.com/SWE-agent/SWE-agent)<br><img src="https://img.shields.io/github/stars/SWE-agent/SWE-agent?style=flat" alt="GitHub stars" height="20"> | 普林斯顿与斯坦福出品。可配置的编码智能体，通过工具修改代码库并修复 GitHub Issue；当前开发主要转向 [mini-swe-agent](https://github.com/SWE-agent/mini-swe-agent)。 | <b>工具:</b> YAML 配置智能体、**LiteLLM**、SWE-ReX<br><b>接入:</b> OpenAI, Anthropic；LiteLLM 支持的提供商 |
| [DeepCode](https://github.com/HKUDS/DeepCode)<br><img src="https://img.shields.io/github/stars/HKUDS/DeepCode?style=flat" alt="GitHub stars" height="20"> | 面向科研复现与软件工程的编码 agent。Paper2Code 工作流将论文与参考代码库转化为开发计划、代码实现和实验验证，支持会话恢复与并行 agent。 | <b>工具:</b> 自研 agent harness、共享本地服务、TUI / Desktop / Web、Skills、MCP、Git worktrees<br><b>接入:</b> OpenAI, Anthropic, Gemini, DeepSeek, OpenRouter, Ollama, vLLM；OpenAI 兼容 API |
| [ClawTeam](https://github.com/HKUDS/ClawTeam)<br><img src="https://img.shields.io/github/stars/HKUDS/ClawTeam?style=flat" alt="GitHub stars" height="20"> | 面向并行实验与编码任务的多智能体编排工具。CLI agent 通过共享任务状态和消息协作，以 Git worktrees 隔离修改，并提供 autoresearch 集群示例。 | <b>工具:</b> Python CLI, tmux, Git worktrees、共享任务、文件 / ZeroMQ 通信<br><b>接入:</b> 由所用 agent 决定：Claude Code, Codex, OpenClaw, Cursor, Gemini CLI 等 CLI agent |
| [Paper2Code](https://github.com/going-doer/Paper2Code)<br><img src="https://img.shields.io/github/stars/going-doer/Paper2Code?style=flat" alt="GitHub stars" height="20"> | ICLR 2026。通过规划、分析与生成 agent，将机器学习论文转化为可运行代码库。 | <b>工具:</b> 多智能体规划、分析与代码生成；vLLM<br><b>接入:</b> OpenAI；经 vLLM 使用开源权重模型 |
| [Paper2Agent](https://github.com/jmiao24/Paper2Agent)<br><img src="https://img.shields.io/github/stars/jmiao24/Paper2Agent?style=flat" alt="GitHub stars" height="20"> | 将研究论文及其代码库转化为 MCP 服务器和可复用 skills，把科学方法、数据和工作流暴露为可调用工具。 | <b>工具:</b> Agent Skills、并行专用 agent、MCP、论文 / 代码库分析<br><b>接入:</b> 由所用 agent 决定：Claude Code, Codex 及其他支持 skill 的编码 agent |
| [DeepResearchAgent](https://github.com/SkyworkAI/DeepResearchAgent)<br><img src="https://img.shields.io/github/stars/SkyworkAI/DeepResearchAgent?style=flat" alt="GitHub stars" height="20"> | 昆仑万维出品。可组合的自演化 agent 运行时，将 agent、工具、环境和记忆注册为版本化资源，跟踪改进的提出、评估与提交。 | <b>工具:</b> 自研（RSPL / SEPL 自演化协议）、MMEngine 配置、持久记忆、版本化资源<br><b>接入:</b> OpenRouter, OpenAI, Anthropic, Google Gemini；可配置 API base |
| [MLE-agent](https://github.com/MLSysOps/MLE-agent)<br><img src="https://img.shields.io/github/stars/MLSysOps/MLE-agent?style=flat" alt="GitHub stars" height="20"> | 面向 ML 工程的智能体，支持基线搭建、本地运行、调试和 Kaggle 工作流，并提供代码检索与项目报告。 | <b>工具:</b> Python CLI, Kaggle、代码 RAG、本地执行<br><b>接入:</b> OpenAI, Anthropic, Gemini, DeepSeek, Mistral, Ollama, vLLM；可选 LiteLLM |
| [AIDE](https://github.com/WecoAI/aideml)<br><img src="https://img.shields.io/github/stars/WecoAI/aideml?style=flat" alt="GitHub stars" height="20"> | AIDE 的开源参考实现。搜索候选 ML 程序构成的树，以执行结果和用户指定指标引导代码生成、调试与改进。[[论文]](https://arxiv.org/abs/2502.13138) | <b>工具:</b> 智能体树搜索、Python CLI, Streamlit, Docker<br><b>接入:</b> OpenAI, Anthropic, Gemini；Ollama 等提供 OpenAI 兼容接口的本地模型 |
| [CORAL](https://github.com/Human-Agent-Society/CORAL)<br><img src="https://img.shields.io/github/stars/Human-Agent-Society/CORAL?style=flat" alt="GitHub stars" height="20"> | 面向 autoresearch 风格实验循环的基础设施。并行编码 agent 共享发现与可复用 skills，由评分器评估尝试，并支持多岛探索和迁移。 | <b>工具:</b> 多智能体 Git worktrees、评分器、共享状态、Docker、可选 **LiteLLM**<br><b>接入:</b> Claude Code, OpenCode, Codex, Cursor Agent, Kiro；可选 LiteLLM 网关 |

[↑ 返回目录](#-目录)

## ✍️ 学术写作与传播

> 聚焦于科学成果阅读、润色、配图、展示与审稿回复的工具。

| 项目与 Stars | 简介 | 框架与 LLM API |
|---|---|---|
| [ChatPaper](https://github.com/kaixindelele/ChatPaper)<br><img src="https://img.shields.io/github/stars/kaixindelele/ChatPaper?style=flat" alt="GitHub stars" height="20"> | 用 ChatGPT 总结 arXiv 与本地 PDF 论文、翻译和润色稿件、分析审稿意见并起草回复。 | <b>工具:</b> PyMuPDF, arxiv.py, Flask, Gradio, Docker<br><b>接入:</b> OpenAI |
| [PaperBanana](https://github.com/dwzhu-pku/PaperBanana)<br><img src="https://img.shields.io/github/stars/dwzhu-pku/PaperBanana?style=flat" alt="GitHub stars" height="20"> | 参考驱动的学术插图框架，由检索、规划、风格、可视化和评审五类 agent 迭代生成科学示意图与图表，可配置视觉语言和图像生成模型。 | <b>工具:</b> 五 agent 配图流水线、Gradio, Streamlit, OpenRouter<br><b>接入:</b> Google Gemini；经 OpenRouter 使用 OpenAI, Anthropic 等提供商 |
| [Paper2Poster](https://github.com/Paper2Poster/Paper2Poster)<br><img src="https://img.shields.io/github/stars/Paper2Poster/Paper2Poster?style=flat" alt="GitHub stars" height="20"> | NeurIPS 2025。将论文 PDF 转换为可编辑学术海报（`.pptx`），另提供用于准备海报内容的轻量编码 agent skill。 | <b>工具:</b> 多智能体流水线、可编辑 PowerPoint 输出、vLLM, Docker<br><b>接入:</b> OpenAI；经 vLLM 使用开源权重语言与视觉模型 |
| [ChatReviewer](https://github.com/nishiwen1214/ChatReviewer)<br><img src="https://img.shields.io/github/stars/nishiwen1214/ChatReviewer?style=flat" alt="GitHub stars" height="20"> | 用 ChatGPT 总结论文优缺点并提出改进建议；配套 ChatResponse 可根据审稿意见起草逐点回复。基于 ChatPaper 开发。 | <b>工具:</b> Python, PyMuPDF, tiktoken, Gradio, Docker, HuggingFace Spaces<br><b>接入:</b> OpenAI |

[↑ 返回目录](#-目录)

## 🔧 研究 Skills 与插件合集

> 可复用的 skill 集合和插件生态，集成到编码 agent（Claude Code、Codex、Gemini CLI 等）中以实现研究工作流。

| 项目与 Stars | 简介 | 框架与 LLM API |
|---|---|---|
| [scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)<br><img src="https://img.shields.io/github/stars/K-Dense-AI/scientific-agent-skills?style=flat" alt="GitHub stars" height="20"> | 177 个科学与研究 skills，覆盖生物、化学、医学、物理、工程、地球科学、数据分析和科学传播，为软件包、数据库与工作流提供可复用指导。 | <b>工具:</b> Agent Skills / Agent Plugins、科学计算 Python 库、科学数据库<br><b>接入:</b> Agent 无关：Claude Code, Cursor, Codex, Google Antigravity 及兼容宿主 |
| [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs)<br><img src="https://img.shields.io/github/stars/Orchestra-Research/AI-Research-SKILLs?style=flat" alt="GitHub stars" height="20"> | 98 个 skills 覆盖 23 个类别，贯穿 AI 研究全生命周期，包括 autoresearch 编排、想法生成、训练、评测、实验和论文撰写。 | <b>工具:</b> Agent Skills, DeepSpeed, vLLM, LangChain, W&B, MLflow<br><b>接入:</b> Agent 无关：Claude Code, Codex, Gemini CLI, OpenCode 及兼容宿主 |
| [OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills)<br><img src="https://img.shields.io/github/stars/FreedomIntelligence/OpenClaw-Medical-Skills?style=flat" alt="GitHub stars" height="20"> | 869 个医学与科学 skills，覆盖临床报告、基因组学、药物发现、生信、结构生物学和生医数据库，汇集自多个 skill 集合。 | <b>工具:</b> Agent Skills、**OpenClaw** / **NanoClaw**、生医工具与数据库<br><b>接入:</b> 经 OpenClaw / NanoClaw 使用宿主 agent 的模型提供商 |

[↑ 返回目录](#-目录)

## 📋 Awesome Lists 与综述

> 自动化科研领域的精选集合和综述论文。

| 项目与 Stars | 简介 |
|---|---|
| [awesome-autoresearch](https://github.com/webfuse-com/awesome-autoresearch)<br><img src="https://img.shields.io/github/stars/webfuse-com/awesome-autoresearch?style=flat" alt="GitHub stars" height="20"> | Karpathy autoresearch 风格的自主改进循环与研究 agent 精选索引，涵盖平台移植、领域扩展、评测与应用案例。 |
| [awesome-ai-for-science](https://github.com/ai4s-research/awesome-ai-for-science)<br><img src="https://img.shields.io/github/stars/ai4s-research/awesome-ai-for-science?style=flat" alt="GitHub stars" height="20"> | AI for Science 工具、库、论文、数据集和框架的精选列表，覆盖物理、化学、生物和材料科学等领域。 |
| [Autonomous-Agents](https://github.com/tmgthb/Autonomous-Agents)<br><img src="https://img.shields.io/github/stars/tmgthb/Autonomous-Agents?style=flat" alt="GitHub stars" height="20"> | 每日更新的自主 LLM Agent 研究论文合集，覆盖多智能体系统、科学计算、机器人等领域。 |
| [Awesome-Deep-Research](https://github.com/DavidZWZ/Awesome-Deep-Research)<br><img src="https://img.shields.io/github/stars/DavidZWZ/Awesome-Deep-Research?style=flat" alt="GitHub stars" height="20"> | Agentic deep research 精选合集，涵盖产业界产品、开源实现、研究论文、评测基准和应用，并附推理驱动搜索的观点论文。 |

[↑ 返回目录](#-目录)

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

[查看交互式 Star History 图表](https://www.star-history.com/?repos=karpathy%2Fautoresearch%2CSakanaAI%2FAI-Scientist%2Cmicrosoft%2FRD-Agent%2Caiming-lab%2FAutoResearchClaw%2Ckaixindelele%2FChatPaper%2Csnap-stanford%2FBiomni%2CEvoScientist%2FEvoScientist%2CResearAI%2FDeepScientist%2CInternScience%2FInternAgent%2Cbytedance%2Fdeer-flow%2Cstanford-oval%2Fstorm%2Cassafelovic%2Fgpt-researcher%2CAlibaba-NLP%2FDeepResearch%2CLearningCircuit%2Flocal-deep-research%2Cskyllwt%2FAutoSci%2COpenRaiser%2FNanoResearch%2Cgoing-doer%2FPaper2Code%2CFuture-House%2Frobin&type=date)

---

## 📄 许可证

[CC0 1.0 Universal](LICENSE)
