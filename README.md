# 🔬 Awesome Auto Research [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[English](README.md) | [中文](README_CN.md)

<p align="center">
  <img src="fig/banner_en.jpg" alt="Awesome Auto Research" width="800">
</p>

> 🤖 A curated list of open-source projects that automate scientific research — from literature review to idea generation, experiment execution, paper writing, and peer review.

**📅 Star counts last verified: 2026-10-07**

---

## 📑 Table of Contents

- [🧪 Autonomous Research Systems](#-autonomous-research-systems)
- [📚 Deep Research & Literature Synthesis](#-deep-research--literature-synthesis)
- [⚙️ Research Implementation & Experimentation](#️-research-implementation--experimentation)
- [✍️ Academic Writing & Communication](#️-academic-writing--communication)
- [🔧 Research Skills & Plugin Collections](#-research-skills--plugin-collections)
- [📋 Awesome Lists & Surveys](#-awesome-lists--surveys)
- [💡 How This Differs from General AI Agent Lists](#-how-this-differs-from-general-ai-agent-lists)
- [🤝 Contributing](#-contributing)

---

## 🧪 Autonomous Research Systems

> Multi-stage systems that autonomously handle several parts of the research loop, such as hypothesis generation, experimentation, analysis, and manuscript preparation.

| Project | Stars | Framework / Tools | Supported LLM APIs | Description |
|---------|-------|-------------------|---------------------|-------------|
| [autoresearch](https://github.com/karpathy/autoresearch) | <img src="https://img.shields.io/github/stars/karpathy/autoresearch?style=for-the-badge" height="36"> | Custom (PyTorch, nanochat) | External coding agents such as Anthropic Claude Code and OpenAI Codex | By Andrej Karpathy. A minimal single-GPU research harness where an external coding agent repeatedly edits `train.py` and runs fixed five-minute nanochat experiments under instructions in `program.md`. |
| [ARIS](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | <img src="https://img.shields.io/github/stars/wanshuiyin/Auto-claude-code-research-in-sleep?style=for-the-badge" height="36"> | **Claude Code** / Codex CLI skills and plugins, ARIS-Code CLI, MCP, Zotero, Obsidian | Anthropic Claude, OpenAI Codex; alternative executors/reviewers via OpenAI-compatible APIs | Research workflow skills with independent cross-model review loops, persistent research memory, idea discovery, experiment automation, proof audits, and paper writing; also available as a standalone CLI. |
| [RD-Agent](https://github.com/microsoft/RD-Agent) | <img src="https://img.shields.io/github/stars/microsoft/RD-Agent?style=for-the-badge" height="36"> | Custom + **LiteLLM**, Docker, Qlib | OpenAI, Azure OpenAI, DeepSeek; LiteLLM-supported providers | Microsoft. Research and development agents for data science, quant factor/model evolution, Kaggle automation, paper-to-code implementation, and LLM fine-tuning. |
| [AI-Scientist](https://github.com/SakanaAI/AI-Scientist) | <img src="https://img.shields.io/github/stars/SakanaAI/AI-Scientist?style=for-the-badge" height="36"> | Custom (templates, LaTeX pipeline) | OpenAI, Anthropic Claude, DeepSeek, Gemini, OpenRouter, open-weight models | Template-based scientific discovery system that automates idea generation, coding, experiments, manuscript writing, and paper review. |
| [AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | <img src="https://img.shields.io/github/stars/aiming-lab/AutoResearchClaw?style=for-the-badge" height="36"> | Custom pipeline, **OpenClaw** / ACP, Docker, LaTeX, OpenAlex, Semantic Scholar | OpenAI-compatible APIs (OpenRouter, DeepSeek, MiniMax); ACP-compatible coding agents | 23-stage autonomous or human-in-the-loop research pipeline: idea → literature → domain-specific experiments → multi-agent review → LaTeX paper, with six intervention modes. |
| [AI-Scientist-v2](https://github.com/SakanaAI/AI-Scientist-v2) | <img src="https://img.shields.io/github/stars/SakanaAI/AI-Scientist-v2?style=for-the-badge" height="36"> | Custom (BFTS agentic tree search, AIDE) | OpenAI, Anthropic Claude (AWS Bedrock), Gemini | Template-free scientific discovery system using progressive agentic tree search to generate hypotheses, run experiments, analyze results, and write manuscripts. |
| [Agent Laboratory](https://github.com/SamuelSchmidgall/AgentLaboratory) | <img src="https://img.shields.io/github/stars/SamuelSchmidgall/AgentLaboratory?style=for-the-badge" height="36"> | Custom multi-agent (arXiv, HuggingFace, LaTeX) | OpenAI (o1/o3/GPT-4o), DeepSeek | End-to-end autonomous research workflow with specialized agents for literature review, experimentation, and report writing. |
| [AI-Researcher](https://github.com/HKUDS/AI-Researcher) | <img src="https://img.shields.io/github/stars/HKUDS/AI-Researcher?style=for-the-badge" height="36"> | Custom + **LiteLLM**, Docker, Gradio | OpenAI, Anthropic, Gemini, DeepSeek, OpenRouter; LiteLLM-supported providers | NeurIPS 2025 Spotlight. Fully autonomous system covering literature review, hypothesis generation, algorithm implementation, and manuscript preparation. |
| [claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | <img src="https://img.shields.io/github/stars/Galaxy-Dawn/claude-scholar?style=for-the-badge" height="36"> | **Claude Code** / Codex CLI / Kimi Code CLI / OpenCode, Zotero MCP, Obsidian, LaTeX | Anthropic Claude, OpenAI (Codex), Moonshot Kimi; OpenCode-configured providers | Semi-automated academic research assistant covering literature review, coding, experiments, writing, publication, and project knowledge management, with separate coding-agent branches. |
| [EvoScientist](https://github.com/EvoScientist/EvoScientist) | <img src="https://img.shields.io/github/stars/EvoScientist/EvoScientist?style=for-the-badge" height="36"> | **LangChain** + **LangGraph** + DeepAgents, MCP, Docker | Anthropic, OpenAI, Google Gemini, DeepSeek, MiniMax, NVIDIA NIM, OpenRouter; configurable providers | Self-evolving research assistant with six sub-agents for planning, research, coding, debugging, analysis, and writing; persistent memory and reusable skills across CLI/TUI, WebUI, and messaging channels. |
| [Biomni](https://github.com/snap-stanford/Biomni) | <img src="https://img.shields.io/github/stars/snap-stanford/Biomni?style=for-the-badge" height="36"> | Custom biomedical agent + code execution, datalake, know-how library | Anthropic, OpenAI, Azure OpenAI, Gemini, Groq, AWS Bedrock, Ollama; custom OpenAI-compatible APIs | Stanford. General-purpose biomedical AI agent that autonomously executes research tasks across biology and medicine, combining LLM reasoning, retrieval, and tool/code use. |
| [DeepScientist](https://github.com/ResearAI/DeepScientist) | <img src="https://img.shields.io/github/stars/ResearAI/DeepScientist?style=for-the-badge" height="36"> | Custom (Bayesian optimization, Findings Memory, Research Map), Git worktrees, LaTeX | Codex CLI, Claude Code, Kimi Code, OpenCode | Local-first autonomous research studio. Findings Memory + Bayesian optimization orchestrate baseline reproduction → branched experiments → LaTeX paper drafts. |
| [DATAGEN](https://github.com/zi-yue-1129/DATAGEN) | <img src="https://img.shields.io/github/stars/zi-yue-1129/DATAGEN?style=for-the-badge" height="36"> | **LangChain** + **LangGraph**, MCP, reusable skills, Firecrawl / fastCRW | OpenAI, Anthropic, Gemini, Ollama, Groq, Atlas Cloud, OrcaRouter | AI-driven multi-agent research assistant automating hypothesis generation, data analysis, visualization, and report writing. |
| [AutoSci](https://github.com/skyllwt/AutoSci) | <img src="https://img.shields.io/github/stars/skyllwt/AutoSci?style=for-the-badge" height="36"> | Memory-centric agent framework, persistent knowledge graph, web dashboard | Claude Code; preview support for Codex and OpenCode | Memory-centric research system spanning literature review, ideation, experiments, analysis, and writing, with guided method iteration and separate Codex/OpenCode preview branches. |
| [Idea2Paper](https://github.com/AgentAlphaAGI/Idea2Paper) | <img src="https://img.shields.io/github/stars/AgentAlphaAGI/Idea2Paper?style=for-the-badge" height="36"> | Custom multi-agent pipeline, knowledge graph, embedding retrieval, anchored review | Configurable LLM endpoints and OpenAI-compatible embeddings APIs | Its Idea2Story module builds a literature knowledge graph, retrieves research patterns, and refines raw ideas into structured research stories through anchored multi-agent review. |
| [InternAgent](https://github.com/InternScience/InternAgent) | <img src="https://img.shields.io/github/stars/InternScience/InternAgent?style=for-the-badge" height="36"> | Custom discovery / deep-research pipeline, coding-agent experiment backends, persistent memory | OpenAI-compatible APIs, OpenRouter, Anthropic Claude | Shanghai AI Lab. InternAgent-1.5 coordinates hypothesis generation, experiments, scientific paper reproduction, and deep research, with persistent memory across discovery runs. |
| [NanoResearch](https://github.com/OpenRaiser/NanoResearch) | <img src="https://img.shields.io/github/stars/OpenRaiser/NanoResearch?style=for-the-badge" height="36"> | Nine-stage pipeline, Evo skills/memory/policy loop, local/SLURM execution, LaTeX | OpenAI-compatible APIs; Claude Code | End-to-end idea-to-paper pipeline with real local or SLURM experiments; Evo mode adapts reusable skills, memory, and routing across research runs. |
| [K-Dense BYOK](https://github.com/K-Dense-AI/k-dense-byok) | <img src="https://img.shields.io/github/stars/K-Dense-AI/k-dense-byok?style=for-the-badge" height="36"> | Local-first workspace, Pi agent runtime, scientific skills, specialist agents, MCP, Ollama | OpenRouter; direct OpenAI, Anthropic, Gemini and other provider APIs; supported subscriptions; Ollama / OpenAI-compatible local servers | Local AI co-scientist for literature, data analysis, code execution, figures, and reports, with 181 scientific skills and a hash-chained lab notebook that records executed steps and artifacts. |
| [data-to-paper](https://github.com/Technion-Kishony-lab/data-to-paper) | <img src="https://img.shields.io/github/stars/Technion-Kishony-lab/data-to-paper?style=for-the-badge" height="36"> | Multi-agent pipeline, code execution, LaTeX, Semantic Scholar | OpenAI API; optional DeepInfra | Turns research datasets into transparent, traceable, and verifiable manuscripts, with agents for analysis, interpretation, literature search, and writing. |
| [Robin](https://github.com/Future-House/robin) | <img src="https://img.shields.io/github/stars/Future-House/robin?style=for-the-badge" height="36"> | Multi-agent scientific discovery system, **LiteLLM**, Edison platform, Docker / Jupyter | LiteLLM-supported providers; Edison platform for literature and data-analysis agents | FutureHouse's multi-agent system for scientific discovery, coordinating literature research, data analysis, and experimental planning. |

## 📚 Deep Research & Literature Synthesis

> Projects focused on automated information gathering, literature review, and report generation.

| Project | Stars | Framework / Tools | Supported LLM APIs | Description |
|---------|-------|-------------------|---------------------|-------------|
| [DeerFlow](https://github.com/bytedance/deer-flow) | <img src="https://img.shields.io/github/stars/bytedance/deer-flow?style=for-the-badge" height="36"> | **LangChain** + **LangGraph**, MCP, extensible skills, sandboxes, InfoQuest | OpenAI-compatible APIs, OpenRouter, vLLM; Codex CLI and Claude Code-backed providers | ByteDance. DeerFlow 2.0 super-agent harness for research, coding, and reports, with sub-agents, persistent memory, reusable skills, project workspaces, and scheduled tasks. |
| [STORM](https://github.com/stanford-oval/storm) | <img src="https://img.shields.io/github/stars/stanford-oval/storm?style=for-the-badge" height="36"> | **DSPy** + **LiteLLM**, Streamlit | LiteLLM-supported providers; web search and custom document retrievers | Stanford. LLM-powered knowledge curation system that generates full-length Wikipedia-like articles with citations. Features Co-STORM. |
| [GPT Researcher](https://github.com/assafelovic/gpt-researcher) | <img src="https://img.shields.io/github/stars/assafelovic/gpt-researcher?style=for-the-badge" height="36"> | **LangGraph** / AG2, MCP, Claude Skill, FastAPI, NextJS | OpenAI, Anthropic Claude, Gemini; any OpenAI-compatible API | Autonomous web and local-document research agent with source-tracked reports, PDF/Word/Markdown export, multi-agent workflows, and a coding-agent skill. |
| [Tongyi DeepResearch](https://github.com/Alibaba-NLP/DeepResearch) | <img src="https://img.shields.io/github/stars/Alibaba-NLP/DeepResearch?style=for-the-badge" height="36"> | Custom (ReAct, IterResearch, GRPO RL); Serper, Jina, SandboxFusion | OpenAI-compatible, OpenRouter; Tongyi-30B-A3B, Dashscope/Bailian | Alibaba. Open-weight Tongyi-DeepResearch-30B-A3B model for long-horizon information seeking, with ReAct and IterResearch-based heavy inference modes. |
| [Open Deep Research](https://github.com/langchain-ai/open_deep_research) | <img src="https://img.shields.io/github/stars/langchain-ai/open_deep_research?style=for-the-badge" height="36"> | **LangChain** + **LangGraph**, MCP, LangSmith | LangChain-supported providers (OpenAI, Anthropic, OpenRouter, Ollama); tool calling and structured output required | LangChain. Open-source deep research framework with configurable MCP tools and search APIs. |
| [PaperQA2](https://github.com/Future-House/paper-qa) | <img src="https://img.shields.io/github/stars/Future-House/paper-qa?style=for-the-badge" height="36"> | Custom agentic RAG + **LiteLLM**, Pydantic, tantivy, multimodal document readers | OpenAI, Anthropic, Gemini, Ollama, llama.cpp; any LiteLLM provider | Agentic RAG for scientific literature and local documents, with iterative retrieval, contextual summarization, citations, and support for PDF text, tables, figures, and equations. |
| [local-deep-research](https://github.com/LearningCircuit/local-deep-research) | <img src="https://img.shields.io/github/stars/LearningCircuit/local-deep-research?style=for-the-badge" height="36"> | **LangChain** + **LangGraph**, FastAPI, FAISS, SQLCipher, SearXNG | Ollama, LM Studio, llama.cpp; OpenAI, Anthropic, Gemini, OpenRouter, Requesty; compatible endpoints | Local-first agentic research with dynamically selected web and academic search engines, a searchable document library, MCP integration, and per-user encrypted storage. |
| [Auto-Deep-Research](https://github.com/HKUDS/Auto-Deep-Research) | <img src="https://img.shields.io/github/stars/HKUDS/Auto-Deep-Research?style=for-the-badge" height="36"> | AutoAgent Framework + **LiteLLM**, Docker | Anthropic, OpenAI, Gemini, Mistral, Groq, OpenRouter, DeepSeek; any OpenAI-compatible | AutoAgent-based deep research assistant with browser and file workflows, configurable LiteLLM backends, and support for both function-calling and non-function-calling models. |
| [OpenScholar](https://github.com/AkariAsai/OpenScholar) | <img src="https://img.shields.io/github/stars/AkariAsai/OpenScholar?style=for-the-badge" height="36"> | Custom RAG, HuggingFace / PyTorch, torchtune training, retriever and reranker | OpenAI (GPT-4o), Llama 3.1 8B (self-hosted); Semantic Scholar API, You.com | Retrieval-augmented scientific question answering with self-reflective generation and source-grounded citations; releases inference, retriever, and OpenScholar-8B training code. |
| [OpenResearcher](https://github.com/TIGER-AI-Lab/OpenResearcher) | <img src="https://img.shields.io/github/stars/TIGER-AI-Lab/OpenResearcher?style=for-the-badge" height="36"> | Megatron-LM (training), vLLM (serving), HuggingFace, Tevatron, BM25 + Qwen3-Embedding, Serper | OpenResearcher-30B-A3B (open-weight release); OpenAI API (scoring) | Open deep-research training and inference recipe releasing the OpenResearcher-30B-A3B model, 96K agent trajectories, browser tools, and benchmark evaluation code. |

## ⚙️ Research Implementation & Experimentation

> Coding, orchestration, and experiment-optimization systems that implement research ideas and run iterative empirical loops.

| Project | Stars | Framework / Tools | Supported LLM APIs | Description |
|---------|-------|-------------------|---------------------|-------------|
| [OpenHands](https://github.com/OpenHands/OpenHands) | <img src="https://img.shields.io/github/stars/OpenHands/OpenHands?style=for-the-badge" height="36"> | Agent Canvas, OpenHands Agent Server / SDK, ACP, Docker | Configurable LLM providers; Claude Code, Codex, Gemini, and ACP-compatible agents | Self-hosted developer control center for coding agents and automations. Agent Canvas runs agents across local, remote, and cloud backends and schedules reusable workflows. |
| [Aider](https://github.com/Aider-AI/aider) | <img src="https://img.shields.io/github/stars/Aider-AI/aider?style=for-the-badge" height="36"> | AI pair-programming CLI, **LiteLLM**, repository maps, Git integration | Anthropic, OpenAI, Gemini, DeepSeek, OpenRouter, Ollama; OpenAI-compatible APIs | AI pair programming in your terminal. Uses repository maps for code context, edits multiple files, and integrates with Git, linting, and tests. |
| [SWE-agent](https://github.com/SWE-agent/SWE-agent) | <img src="https://img.shields.io/github/stars/SWE-agent/SWE-agent?style=for-the-badge" height="36"> | YAML-configurable agent, **LiteLLM**, SWE-ReX | OpenAI, Anthropic; LiteLLM-supported providers | Princeton and Stanford. Configurable coding agent that edits repositories, uses tools, and fixes GitHub issues. Current development primarily focuses on [mini-swe-agent](https://github.com/SWE-agent/mini-swe-agent). |
| [DeepCode](https://github.com/HKUDS/DeepCode) | <img src="https://img.shields.io/github/stars/HKUDS/DeepCode?style=for-the-badge" height="36"> | Custom agent harness, shared local service, TUI / Desktop / Web, Skills, MCP, Git worktrees | OpenAI, Anthropic, Gemini, DeepSeek, OpenRouter, Ollama, vLLM; OpenAI-compatible APIs | Coding agent for research reproduction and software engineering. Its Paper2Code workflow carries papers and reference repositories through planning, implementation, and experiment-based verification, with resumable sessions and parallel agents. |
| [ClawTeam](https://github.com/HKUDS/ClawTeam) | <img src="https://img.shields.io/github/stars/HKUDS/ClawTeam?style=for-the-badge" height="36"> | Python CLI, tmux, Git worktrees, shared tasks, file / ZeroMQ transport | Agent-dependent: Claude Code, Codex, OpenClaw, Cursor, Gemini CLI, and other CLI agents | Multi-agent orchestration for parallel experiments and coding tasks. CLI agents coordinate through shared task state and messages, while Git worktrees isolate changes; includes an autoresearch swarm example. |
| [Paper2Code](https://github.com/going-doer/Paper2Code) | <img src="https://img.shields.io/github/stars/going-doer/Paper2Code?style=for-the-badge" height="36"> | Multi-agent planning, analysis, and code generation; vLLM | OpenAI; open-weight models through vLLM | ICLR 2026. Converts machine-learning papers into runnable codebases through planning, analysis, and generation agents. |
| [Paper2Agent](https://github.com/jmiao24/Paper2Agent) | <img src="https://img.shields.io/github/stars/jmiao24/Paper2Agent?style=for-the-badge" height="36"> | Agent Skills, parallel specialist agents, MCP, paper / codebase analysis | Agent-dependent: Claude Code, Codex, and other skill-compatible coding agents | Turns research papers and their codebases into MCP servers and reusable skills, exposing scientific methods, data, and workflows as callable tools. |
| [DeepResearchAgent](https://github.com/SkyworkAI/DeepResearchAgent) | <img src="https://img.shields.io/github/stars/SkyworkAI/DeepResearchAgent?style=for-the-badge" height="36"> | Custom (RSPL / SEPL self-evolution protocol), MMEngine configs, persistent memory, versioned resources | OpenRouter, OpenAI, Anthropic, Google Gemini; configurable API bases | Skywork. Composable self-evolving agent runtime that registers agents, tools, environments, and memory as versioned resources and tracks proposed, assessed, and committed improvements. |
| [MLE-agent](https://github.com/MLSysOps/MLE-agent) | <img src="https://img.shields.io/github/stars/MLSysOps/MLE-agent?style=for-the-badge" height="36"> | Python CLI, Kaggle, code RAG, local execution | OpenAI, Anthropic, Gemini, DeepSeek, Mistral, Ollama, vLLM; optional LiteLLM | ML engineering agent for baseline construction, local execution, debugging, and Kaggle workflows, with code retrieval and project reports. |
| [AIDE](https://github.com/WecoAI/aideml) | <img src="https://img.shields.io/github/stars/WecoAI/aideml?style=for-the-badge" height="36"> | Agentic tree search, Python CLI, Streamlit, Docker | OpenAI, Anthropic, Gemini; OpenAI-compatible local models such as Ollama | Open-source reference implementation of AIDE. Searches a tree of candidate ML programs, using execution results and a user-defined metric to guide drafting, debugging, and improvement. [[paper]](https://arxiv.org/abs/2502.13138) |
| [CORAL](https://github.com/Human-Agent-Society/CORAL) | <img src="https://img.shields.io/github/stars/Human-Agent-Society/CORAL?style=for-the-badge" height="36"> | Multi-agent Git worktrees, graders, shared state, Docker, optional **LiteLLM** | Claude Code, OpenCode, Codex, Cursor Agent, Kiro; optional LiteLLM gateway | Infrastructure for autoresearch-style experiment loops. Parallel coding agents share findings and reusable skills, while graders evaluate attempts; supports multi-island exploration and migration. |

## ✍️ Academic Writing & Communication

> Tools focused on reading, polishing, illustrating, presenting, and responding to reviews for scientific work.

| Project | Stars | Framework / Tools | Supported LLM APIs | Description |
|---------|-------|-------------------|---------------------|-------------|
| [ChatPaper](https://github.com/kaixindelele/ChatPaper) | <img src="https://img.shields.io/github/stars/kaixindelele/ChatPaper?style=for-the-badge" height="36"> | PyMuPDF, arxiv.py, Flask, Gradio, Docker | OpenAI | Uses ChatGPT to summarize arXiv and local PDF papers, translate and polish manuscripts, analyze reviews, and draft reviewer responses. |
| [PaperBanana](https://github.com/dwzhu-pku/PaperBanana) | <img src="https://img.shields.io/github/stars/dwzhu-pku/PaperBanana?style=for-the-badge" height="36"> | Five-agent illustration pipeline, Gradio, Streamlit, OpenRouter | Google Gemini; OpenAI, Anthropic, and other providers through OpenRouter | Reference-driven academic illustration framework with Retriever, Planner, Stylist, Visualizer, and Critic agents. Iteratively generates diagrams and plots from scientific content, with configurable vision-language and image models. |
| [Paper2Poster](https://github.com/Paper2Poster/Paper2Poster) | <img src="https://img.shields.io/github/stars/Paper2Poster/Paper2Poster?style=for-the-badge" height="36"> | Multi-agent pipeline, editable PowerPoint output, vLLM, Docker | OpenAI; open-weight language and vision models through vLLM | NeurIPS 2025. Converts a paper PDF into an editable academic poster (`.pptx`). Also provides a lightweight coding-agent skill for preparing poster-ready content. |
| [ChatReviewer](https://github.com/nishiwen1214/ChatReviewer) | <img src="https://img.shields.io/github/stars/nishiwen1214/ChatReviewer?style=for-the-badge" height="36"> | Python, PyMuPDF, tiktoken, Gradio, Docker, HuggingFace Spaces | OpenAI | Uses ChatGPT to summarize paper strengths and weaknesses and suggest improvements. Its ChatResponse tool drafts point-by-point responses to reviewer comments; based on ChatPaper. |

## 🔧 Research Skills & Plugin Collections

> Reusable skill sets and plugin ecosystems that integrate with coding agents (Claude Code, Codex, Gemini CLI, etc.) to enable research workflows.

| Project | Stars | Framework / Tools | Supported LLM APIs | Description |
|---------|-------|-------------------|---------------------|-------------|
| [scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | <img src="https://img.shields.io/github/stars/K-Dense-AI/scientific-agent-skills?style=for-the-badge" height="36"> | Agent Skills / Agent Plugins, scientific Python libraries, scientific databases | Agent-agnostic: Claude Code, Cursor, Codex, Google Antigravity, and compatible hosts | 177 scientific and research skills covering biology, chemistry, medicine, physics, engineering, Earth science, data analysis, and scientific communication, with reusable guidance for packages, databases, and workflows. |
| [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) | <img src="https://img.shields.io/github/stars/Orchestra-Research/AI-Research-SKILLs?style=for-the-badge" height="36"> | Agent Skills, DeepSpeed, vLLM, LangChain, W&B, MLflow | Agent-agnostic: Claude Code, Codex, Gemini CLI, OpenCode, and compatible hosts | 98 skills across 23 categories for the AI research lifecycle, including an autoresearch orchestration layer, ideation, training, evaluation, experiments, and paper writing. |
| [OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills) | <img src="https://img.shields.io/github/stars/FreedomIntelligence/OpenClaw-Medical-Skills?style=for-the-badge" height="36"> | Agent Skills, **OpenClaw** / **NanoClaw**, biomedical tools and databases | Host-agent providers through OpenClaw / NanoClaw | 869 medical and scientific skills spanning clinical reports, genomics, drug discovery, bioinformatics, structural biology, and biomedical databases, aggregated from multiple skill collections. |

## 📋 Awesome Lists & Surveys

> Curated collections and survey papers on the auto-research landscape.

| Project | Stars | Description |
|---------|-------|-------------|
| [awesome-autoresearch](https://github.com/webfuse-com/awesome-autoresearch) | <img src="https://img.shields.io/github/stars/webfuse-com/awesome-autoresearch?style=for-the-badge" height="36"> | Curated index of autonomous improvement loops and research agents inspired by Karpathy's autoresearch, including platform ports, domain adaptations, evaluations, and case studies. |
| [awesome-ai-for-science](https://github.com/ai4s-research/awesome-ai-for-science) | <img src="https://img.shields.io/github/stars/ai4s-research/awesome-ai-for-science?style=for-the-badge" height="36"> | Curated list of AI tools, libraries, papers, datasets, and frameworks for scientific discovery across physics, chemistry, biology, and materials. |
| [Autonomous-Agents](https://github.com/tmgthb/Autonomous-Agents) | <img src="https://img.shields.io/github/stars/tmgthb/Autonomous-Agents?style=for-the-badge" height="36"> | Daily-updated curated collection of research papers on autonomous LLM agents. Covers multi-agent systems, scientific computing, robotics, and more. |
| [Awesome-Deep-Research](https://github.com/DavidZWZ/Awesome-Deep-Research) | <img src="https://img.shields.io/github/stars/DavidZWZ/Awesome-Deep-Research?style=for-the-badge" height="36"> | Curated collection of agentic deep research products, open-source implementations, research papers, benchmarks, and applications; includes a position paper on reasoning-driven search. |

---

## 💡 How This Differs from General AI Agent Lists

This list focuses specifically on **automating the scientific research process** — not general-purpose AI agents. We include projects that target one or more stages of the research lifecycle:

```
📖 Literature Review → 💡 Idea Generation → 🔍 Novelty Check → 📐 Experiment Design →
💻 Code Implementation → 🚀 Experiment Execution → 📊 Result Analysis → ✍️ Paper Writing → 📝 Peer Review
```

General-purpose coding agents (OpenHands, Aider, SWE-agent) are included because they serve as critical infrastructure for the experiment execution stage.

---

## 🤝 Contributing

PRs welcome! Please ensure the project:
- Has **500+ GitHub stars**
- Is directly related to automating scientific research
- Is open-source with an active repository

Please keep entries sorted by star count (descending) within each category.

---

## 📈 Star History

[View the interactive Star History chart](https://www.star-history.com/?repos=karpathy%2Fautoresearch%2CSakanaAI%2FAI-Scientist%2Cmicrosoft%2FRD-Agent%2Caiming-lab%2FAutoResearchClaw%2Ckaixindelele%2FChatPaper%2Csnap-stanford%2FBiomni%2CEvoScientist%2FEvoScientist%2CResearAI%2FDeepScientist%2CInternScience%2FInternAgent%2Cbytedance%2Fdeer-flow%2Cstanford-oval%2Fstorm%2Cassafelovic%2Fgpt-researcher%2CAlibaba-NLP%2FDeepResearch%2CLearningCircuit%2Flocal-deep-research%2Cskyllwt%2FAutoSci%2COpenRaiser%2FNanoResearch%2Cgoing-doer%2FPaper2Code%2CFuture-House%2Frobin&type=date)

---

## 📄 License

[CC0 1.0 Universal](LICENSE)
