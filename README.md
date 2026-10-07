<h1 align="center">🔬 Awesome Auto Research</h1>

<p align="center">
  A curated list of open-source projects that automate scientific research — from literature review to idea generation, experiment execution, paper writing, and peer review.
</p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
  &nbsp;·&nbsp; <a href="README.md">English</a>
  &nbsp;·&nbsp; <a href="README_CN.md">中文</a>
  &nbsp;·&nbsp; <a href="#-table-of-contents">Browse tools</a>
  &nbsp;·&nbsp; <a href="#-contributing">Contribute</a>
</p>

<p align="center">
  <img src="fig/banner_research.jpg" alt="Illustrated scientific research workflow, from literature review to experiments and paper writing" width="800">
</p>

**📅 Star counts last verified: 2026-10-07**

---

## 📑 Table of Contents

| [🧪 Autonomous Research Systems](#-autonomous-research-systems)<br><sub>20 projects · Ideas, experiments & papers</sub> | [📚 Deep Research & Literature Synthesis](#-deep-research--literature-synthesis)<br><sub>10 projects · Search, read & synthesize</sub> | [⚙️ Research Implementation & Experimentation](#️-research-implementation--experimentation)<br><sub>11 projects · Code, run & optimize</sub> |
|:---:|:---:|:---:|
| [✍️ Academic Writing & Communication](#️-academic-writing--communication)<br><sub>4 projects · Write, illustrate & review</sub> | [🔧 Research Skills & Plugin Collections](#-research-skills--plugin-collections)<br><sub>3 projects · Extend your research agent</sub> | [📋 Awesome Lists & Surveys](#-awesome-lists--surveys)<br><sub>4 projects · Explore the research landscape</sub> |

---

## 🧪 Autonomous Research Systems

> Multi-stage systems that autonomously handle several parts of the research loop, such as hypothesis generation, experimentation, analysis, and manuscript preparation.

| Project & Stars | Description | Framework & LLM APIs |
|---|---|---|
| [autoresearch](https://github.com/karpathy/autoresearch)<br><img src="https://img.shields.io/github/stars/karpathy/autoresearch?style=flat" alt="GitHub stars" height="20"> | By Andrej Karpathy. A minimal single-GPU research harness where an external coding agent repeatedly edits `train.py` and runs fixed five-minute nanochat experiments under instructions in `program.md`. | <b>Tools:</b> Custom (PyTorch, nanochat)<br><b>Models:</b> External coding agents such as Anthropic Claude Code and OpenAI Codex |
| [ARIS](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)<br><img src="https://img.shields.io/github/stars/wanshuiyin/Auto-claude-code-research-in-sleep?style=flat" alt="GitHub stars" height="20"> | Research workflow skills with independent cross-model review loops, persistent research memory, idea discovery, experiment automation, proof audits, and paper writing; also available as a standalone CLI. | <b>Tools:</b> **Claude Code** / Codex CLI skills and plugins, ARIS-Code CLI, MCP, Zotero, Obsidian<br><b>Models:</b> Anthropic Claude, OpenAI Codex; alternative executors/reviewers via OpenAI-compatible APIs |
| [RD-Agent](https://github.com/microsoft/RD-Agent)<br><img src="https://img.shields.io/github/stars/microsoft/RD-Agent?style=flat" alt="GitHub stars" height="20"> | Microsoft. Research and development agents for data science, quant factor/model evolution, Kaggle automation, paper-to-code implementation, and LLM fine-tuning. | <b>Tools:</b> Custom + **LiteLLM**, Docker, Qlib<br><b>Models:</b> OpenAI, Azure OpenAI, DeepSeek; LiteLLM-supported providers |
| [AI-Scientist](https://github.com/SakanaAI/AI-Scientist)<br><img src="https://img.shields.io/github/stars/SakanaAI/AI-Scientist?style=flat" alt="GitHub stars" height="20"> | Template-based scientific discovery system that automates idea generation, coding, experiments, manuscript writing, and paper review. | <b>Tools:</b> Custom (templates, LaTeX pipeline)<br><b>Models:</b> OpenAI, Anthropic Claude, DeepSeek, Gemini, OpenRouter, open-weight models |
| [AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw)<br><img src="https://img.shields.io/github/stars/aiming-lab/AutoResearchClaw?style=flat" alt="GitHub stars" height="20"> | 23-stage autonomous or human-in-the-loop research pipeline: idea → literature → domain-specific experiments → multi-agent review → LaTeX paper, with six intervention modes. | <b>Tools:</b> Custom pipeline, **OpenClaw** / ACP, Docker, LaTeX, OpenAlex, Semantic Scholar<br><b>Models:</b> OpenAI-compatible APIs (OpenRouter, DeepSeek, MiniMax); ACP-compatible coding agents |
| [AI-Scientist-v2](https://github.com/SakanaAI/AI-Scientist-v2)<br><img src="https://img.shields.io/github/stars/SakanaAI/AI-Scientist-v2?style=flat" alt="GitHub stars" height="20"> | Template-free scientific discovery system using progressive agentic tree search to generate hypotheses, run experiments, analyze results, and write manuscripts. | <b>Tools:</b> Custom (BFTS agentic tree search, AIDE)<br><b>Models:</b> OpenAI, Anthropic Claude (AWS Bedrock), Gemini |
| [Agent Laboratory](https://github.com/SamuelSchmidgall/AgentLaboratory)<br><img src="https://img.shields.io/github/stars/SamuelSchmidgall/AgentLaboratory?style=flat" alt="GitHub stars" height="20"> | End-to-end autonomous research workflow with specialized agents for literature review, experimentation, and report writing. | <b>Tools:</b> Custom multi-agent (arXiv, HuggingFace, LaTeX)<br><b>Models:</b> OpenAI (o1/o3/GPT-4o), DeepSeek |
| [AI-Researcher](https://github.com/HKUDS/AI-Researcher)<br><img src="https://img.shields.io/github/stars/HKUDS/AI-Researcher?style=flat" alt="GitHub stars" height="20"> | NeurIPS 2025 Spotlight. Fully autonomous system covering literature review, hypothesis generation, algorithm implementation, and manuscript preparation. | <b>Tools:</b> Custom + **LiteLLM**, Docker, Gradio<br><b>Models:</b> OpenAI, Anthropic, Gemini, DeepSeek, OpenRouter; LiteLLM-supported providers |
| [claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar)<br><img src="https://img.shields.io/github/stars/Galaxy-Dawn/claude-scholar?style=flat" alt="GitHub stars" height="20"> | Semi-automated academic research assistant covering literature review, coding, experiments, writing, publication, and project knowledge management, with separate coding-agent branches. | <b>Tools:</b> **Claude Code** / Codex CLI / Kimi Code CLI / OpenCode, Zotero MCP, Obsidian, LaTeX<br><b>Models:</b> Anthropic Claude, OpenAI (Codex), Moonshot Kimi; OpenCode-configured providers |
| [EvoScientist](https://github.com/EvoScientist/EvoScientist)<br><img src="https://img.shields.io/github/stars/EvoScientist/EvoScientist?style=flat" alt="GitHub stars" height="20"> | Self-evolving research assistant with six sub-agents for planning, research, coding, debugging, analysis, and writing; persistent memory and reusable skills across CLI/TUI, WebUI, and messaging channels. | <b>Tools:</b> **LangChain** + **LangGraph** + DeepAgents, MCP, Docker<br><b>Models:</b> Anthropic, OpenAI, Google Gemini, DeepSeek, MiniMax, NVIDIA NIM, OpenRouter; configurable providers |
| [Biomni](https://github.com/snap-stanford/Biomni)<br><img src="https://img.shields.io/github/stars/snap-stanford/Biomni?style=flat" alt="GitHub stars" height="20"> | Stanford. General-purpose biomedical AI agent that autonomously executes research tasks across biology and medicine, combining LLM reasoning, retrieval, and tool/code use. | <b>Tools:</b> Custom biomedical agent + code execution, datalake, know-how library<br><b>Models:</b> Anthropic, OpenAI, Azure OpenAI, Gemini, Groq, AWS Bedrock, Ollama; custom OpenAI-compatible APIs |
| [DeepScientist](https://github.com/ResearAI/DeepScientist)<br><img src="https://img.shields.io/github/stars/ResearAI/DeepScientist?style=flat" alt="GitHub stars" height="20"> | Local-first autonomous research studio. Findings Memory + Bayesian optimization orchestrate baseline reproduction → branched experiments → LaTeX paper drafts. | <b>Tools:</b> Custom (Bayesian optimization, Findings Memory, Research Map), Git worktrees, LaTeX<br><b>Models:</b> Codex CLI, Claude Code, Kimi Code, OpenCode |
| [DATAGEN](https://github.com/zi-yue-1129/DATAGEN)<br><img src="https://img.shields.io/github/stars/zi-yue-1129/DATAGEN?style=flat" alt="GitHub stars" height="20"> | AI-driven multi-agent research assistant automating hypothesis generation, data analysis, visualization, and report writing. | <b>Tools:</b> **LangChain** + **LangGraph**, MCP, reusable skills, Firecrawl / fastCRW<br><b>Models:</b> OpenAI, Anthropic, Gemini, Ollama, Groq, Atlas Cloud, OrcaRouter |
| [AutoSci](https://github.com/skyllwt/AutoSci)<br><img src="https://img.shields.io/github/stars/skyllwt/AutoSci?style=flat" alt="GitHub stars" height="20"> | Memory-centric research system spanning literature review, ideation, experiments, analysis, and writing, with guided method iteration and separate Codex/OpenCode preview branches. | <b>Tools:</b> Memory-centric agent framework, persistent knowledge graph, web dashboard<br><b>Models:</b> Claude Code; preview support for Codex and OpenCode |
| [Idea2Paper](https://github.com/AgentAlphaAGI/Idea2Paper)<br><img src="https://img.shields.io/github/stars/AgentAlphaAGI/Idea2Paper?style=flat" alt="GitHub stars" height="20"> | Its Idea2Story module builds a literature knowledge graph, retrieves research patterns, and refines raw ideas into structured research stories through anchored multi-agent review. | <b>Tools:</b> Custom multi-agent pipeline, knowledge graph, embedding retrieval, anchored review<br><b>Models:</b> Configurable LLM endpoints and OpenAI-compatible embeddings APIs |
| [InternAgent](https://github.com/InternScience/InternAgent)<br><img src="https://img.shields.io/github/stars/InternScience/InternAgent?style=flat" alt="GitHub stars" height="20"> | Shanghai AI Lab. InternAgent-1.5 coordinates hypothesis generation, experiments, scientific paper reproduction, and deep research, with persistent memory across discovery runs. | <b>Tools:</b> Custom discovery / deep-research pipeline, coding-agent experiment backends, persistent memory<br><b>Models:</b> OpenAI-compatible APIs, OpenRouter, Anthropic Claude |
| [NanoResearch](https://github.com/OpenRaiser/NanoResearch)<br><img src="https://img.shields.io/github/stars/OpenRaiser/NanoResearch?style=flat" alt="GitHub stars" height="20"> | End-to-end idea-to-paper pipeline with real local or SLURM experiments; Evo mode adapts reusable skills, memory, and routing across research runs. | <b>Tools:</b> Nine-stage pipeline, Evo skills/memory/policy loop, local/SLURM execution, LaTeX<br><b>Models:</b> OpenAI-compatible APIs; Claude Code |
| [K-Dense BYOK](https://github.com/K-Dense-AI/k-dense-byok)<br><img src="https://img.shields.io/github/stars/K-Dense-AI/k-dense-byok?style=flat" alt="GitHub stars" height="20"> | Local AI co-scientist for literature, data analysis, code execution, figures, and reports, with 181 scientific skills and a hash-chained lab notebook that records executed steps and artifacts. | <b>Tools:</b> Local-first workspace, Pi agent runtime, scientific skills, specialist agents, MCP, Ollama<br><b>Models:</b> OpenRouter; direct OpenAI, Anthropic, Gemini and other provider APIs; supported subscriptions; Ollama / OpenAI-compatible local servers |
| [data-to-paper](https://github.com/Technion-Kishony-lab/data-to-paper)<br><img src="https://img.shields.io/github/stars/Technion-Kishony-lab/data-to-paper?style=flat" alt="GitHub stars" height="20"> | Turns research datasets into transparent, traceable, and verifiable manuscripts, with agents for analysis, interpretation, literature search, and writing. | <b>Tools:</b> Multi-agent pipeline, code execution, LaTeX, Semantic Scholar<br><b>Models:</b> OpenAI API; optional DeepInfra |
| [Robin](https://github.com/Future-House/robin)<br><img src="https://img.shields.io/github/stars/Future-House/robin?style=flat" alt="GitHub stars" height="20"> | FutureHouse's multi-agent system for scientific discovery, coordinating literature research, data analysis, and experimental planning. | <b>Tools:</b> Multi-agent scientific discovery system, **LiteLLM**, Edison platform, Docker / Jupyter<br><b>Models:</b> LiteLLM-supported providers; Edison platform for literature and data-analysis agents |

[↑ Back to contents](#-table-of-contents)

## 📚 Deep Research & Literature Synthesis

> Projects focused on automated information gathering, literature review, and report generation.

| Project & Stars | Description | Framework & LLM APIs |
|---|---|---|
| [DeerFlow](https://github.com/bytedance/deer-flow)<br><img src="https://img.shields.io/github/stars/bytedance/deer-flow?style=flat" alt="GitHub stars" height="20"> | ByteDance. DeerFlow 2.0 super-agent harness for research, coding, and reports, with sub-agents, persistent memory, reusable skills, project workspaces, and scheduled tasks. | <b>Tools:</b> **LangChain** + **LangGraph**, MCP, extensible skills, sandboxes, InfoQuest<br><b>Models:</b> OpenAI-compatible APIs, OpenRouter, vLLM; Codex CLI and Claude Code-backed providers |
| [STORM](https://github.com/stanford-oval/storm)<br><img src="https://img.shields.io/github/stars/stanford-oval/storm?style=flat" alt="GitHub stars" height="20"> | Stanford. LLM-powered knowledge curation system that generates full-length Wikipedia-like articles with citations. Features Co-STORM. | <b>Tools:</b> **DSPy** + **LiteLLM**, Streamlit<br><b>Models:</b> LiteLLM-supported providers; web search and custom document retrievers |
| [GPT Researcher](https://github.com/assafelovic/gpt-researcher)<br><img src="https://img.shields.io/github/stars/assafelovic/gpt-researcher?style=flat" alt="GitHub stars" height="20"> | Autonomous web and local-document research agent with source-tracked reports, PDF/Word/Markdown export, multi-agent workflows, and a coding-agent skill. | <b>Tools:</b> **LangGraph** / AG2, MCP, Claude Skill, FastAPI, NextJS<br><b>Models:</b> OpenAI, Anthropic Claude, Gemini; any OpenAI-compatible API |
| [Tongyi DeepResearch](https://github.com/Alibaba-NLP/DeepResearch)<br><img src="https://img.shields.io/github/stars/Alibaba-NLP/DeepResearch?style=flat" alt="GitHub stars" height="20"> | Alibaba. Open-weight Tongyi-DeepResearch-30B-A3B model for long-horizon information seeking, with ReAct and IterResearch-based heavy inference modes. | <b>Tools:</b> Custom (ReAct, IterResearch, GRPO RL); Serper, Jina, SandboxFusion<br><b>Models:</b> OpenAI-compatible, OpenRouter; Tongyi-30B-A3B, Dashscope/Bailian |
| [Open Deep Research](https://github.com/langchain-ai/open_deep_research)<br><img src="https://img.shields.io/github/stars/langchain-ai/open_deep_research?style=flat" alt="GitHub stars" height="20"> | LangChain. Open-source deep research framework with configurable MCP tools and search APIs. | <b>Tools:</b> **LangChain** + **LangGraph**, MCP, LangSmith<br><b>Models:</b> LangChain-supported providers (OpenAI, Anthropic, OpenRouter, Ollama); tool calling and structured output required |
| [PaperQA2](https://github.com/Future-House/paper-qa)<br><img src="https://img.shields.io/github/stars/Future-House/paper-qa?style=flat" alt="GitHub stars" height="20"> | Agentic RAG for scientific literature and local documents, with iterative retrieval, contextual summarization, citations, and support for PDF text, tables, figures, and equations. | <b>Tools:</b> Custom agentic RAG + **LiteLLM**, Pydantic, tantivy, multimodal document readers<br><b>Models:</b> OpenAI, Anthropic, Gemini, Ollama, llama.cpp; any LiteLLM provider |
| [local-deep-research](https://github.com/LearningCircuit/local-deep-research)<br><img src="https://img.shields.io/github/stars/LearningCircuit/local-deep-research?style=flat" alt="GitHub stars" height="20"> | Local-first agentic research with dynamically selected web and academic search engines, a searchable document library, MCP integration, and per-user encrypted storage. | <b>Tools:</b> **LangChain** + **LangGraph**, FastAPI, FAISS, SQLCipher, SearXNG<br><b>Models:</b> Ollama, LM Studio, llama.cpp; OpenAI, Anthropic, Gemini, OpenRouter, Requesty; compatible endpoints |
| [Auto-Deep-Research](https://github.com/HKUDS/Auto-Deep-Research)<br><img src="https://img.shields.io/github/stars/HKUDS/Auto-Deep-Research?style=flat" alt="GitHub stars" height="20"> | AutoAgent-based deep research assistant with browser and file workflows, configurable LiteLLM backends, and support for both function-calling and non-function-calling models. | <b>Tools:</b> AutoAgent Framework + **LiteLLM**, Docker<br><b>Models:</b> Anthropic, OpenAI, Gemini, Mistral, Groq, OpenRouter, DeepSeek; any OpenAI-compatible |
| [OpenScholar](https://github.com/AkariAsai/OpenScholar)<br><img src="https://img.shields.io/github/stars/AkariAsai/OpenScholar?style=flat" alt="GitHub stars" height="20"> | Retrieval-augmented scientific question answering with self-reflective generation and source-grounded citations; releases inference, retriever, and OpenScholar-8B training code. | <b>Tools:</b> Custom RAG, HuggingFace / PyTorch, torchtune training, retriever and reranker<br><b>Models:</b> OpenAI (GPT-4o), Llama 3.1 8B (self-hosted); Semantic Scholar API, You.com |
| [OpenResearcher](https://github.com/TIGER-AI-Lab/OpenResearcher)<br><img src="https://img.shields.io/github/stars/TIGER-AI-Lab/OpenResearcher?style=flat" alt="GitHub stars" height="20"> | Open deep-research training and inference recipe releasing the OpenResearcher-30B-A3B model, 96K agent trajectories, browser tools, and benchmark evaluation code. | <b>Tools:</b> Megatron-LM (training), vLLM (serving), HuggingFace, Tevatron, BM25 + Qwen3-Embedding, Serper<br><b>Models:</b> OpenResearcher-30B-A3B (open-weight release); OpenAI API (scoring) |

[↑ Back to contents](#-table-of-contents)

## ⚙️ Research Implementation & Experimentation

> Coding, orchestration, and experiment-optimization systems that implement research ideas and run iterative empirical loops.

| Project & Stars | Description | Framework & LLM APIs |
|---|---|---|
| [OpenHands](https://github.com/OpenHands/OpenHands)<br><img src="https://img.shields.io/github/stars/OpenHands/OpenHands?style=flat" alt="GitHub stars" height="20"> | Self-hosted developer control center for coding agents and automations. Agent Canvas runs agents across local, remote, and cloud backends and schedules reusable workflows. | <b>Tools:</b> Agent Canvas, OpenHands Agent Server / SDK, ACP, Docker<br><b>Models:</b> Configurable LLM providers; Claude Code, Codex, Gemini, and ACP-compatible agents |
| [Aider](https://github.com/Aider-AI/aider)<br><img src="https://img.shields.io/github/stars/Aider-AI/aider?style=flat" alt="GitHub stars" height="20"> | AI pair programming in your terminal. Uses repository maps for code context, edits multiple files, and integrates with Git, linting, and tests. | <b>Tools:</b> AI pair-programming CLI, **LiteLLM**, repository maps, Git integration<br><b>Models:</b> Anthropic, OpenAI, Gemini, DeepSeek, OpenRouter, Ollama; OpenAI-compatible APIs |
| [SWE-agent](https://github.com/SWE-agent/SWE-agent)<br><img src="https://img.shields.io/github/stars/SWE-agent/SWE-agent?style=flat" alt="GitHub stars" height="20"> | Princeton and Stanford. Configurable coding agent that edits repositories, uses tools, and fixes GitHub issues. Current development primarily focuses on [mini-swe-agent](https://github.com/SWE-agent/mini-swe-agent). | <b>Tools:</b> YAML-configurable agent, **LiteLLM**, SWE-ReX<br><b>Models:</b> OpenAI, Anthropic; LiteLLM-supported providers |
| [DeepCode](https://github.com/HKUDS/DeepCode)<br><img src="https://img.shields.io/github/stars/HKUDS/DeepCode?style=flat" alt="GitHub stars" height="20"> | Coding agent for research reproduction and software engineering. Its Paper2Code workflow carries papers and reference repositories through planning, implementation, and experiment-based verification, with resumable sessions and parallel agents. | <b>Tools:</b> Custom agent harness, shared local service, TUI / Desktop / Web, Skills, MCP, Git worktrees<br><b>Models:</b> OpenAI, Anthropic, Gemini, DeepSeek, OpenRouter, Ollama, vLLM; OpenAI-compatible APIs |
| [ClawTeam](https://github.com/HKUDS/ClawTeam)<br><img src="https://img.shields.io/github/stars/HKUDS/ClawTeam?style=flat" alt="GitHub stars" height="20"> | Multi-agent orchestration for parallel experiments and coding tasks. CLI agents coordinate through shared task state and messages, while Git worktrees isolate changes; includes an autoresearch swarm example. | <b>Tools:</b> Python CLI, tmux, Git worktrees, shared tasks, file / ZeroMQ transport<br><b>Models:</b> Agent-dependent: Claude Code, Codex, OpenClaw, Cursor, Gemini CLI, and other CLI agents |
| [Paper2Code](https://github.com/going-doer/Paper2Code)<br><img src="https://img.shields.io/github/stars/going-doer/Paper2Code?style=flat" alt="GitHub stars" height="20"> | ICLR 2026. Converts machine-learning papers into runnable codebases through planning, analysis, and generation agents. | <b>Tools:</b> Multi-agent planning, analysis, and code generation; vLLM<br><b>Models:</b> OpenAI; open-weight models through vLLM |
| [Paper2Agent](https://github.com/jmiao24/Paper2Agent)<br><img src="https://img.shields.io/github/stars/jmiao24/Paper2Agent?style=flat" alt="GitHub stars" height="20"> | Turns research papers and their codebases into MCP servers and reusable skills, exposing scientific methods, data, and workflows as callable tools. | <b>Tools:</b> Agent Skills, parallel specialist agents, MCP, paper / codebase analysis<br><b>Models:</b> Agent-dependent: Claude Code, Codex, and other skill-compatible coding agents |
| [DeepResearchAgent](https://github.com/SkyworkAI/DeepResearchAgent)<br><img src="https://img.shields.io/github/stars/SkyworkAI/DeepResearchAgent?style=flat" alt="GitHub stars" height="20"> | Skywork. Composable self-evolving agent runtime that registers agents, tools, environments, and memory as versioned resources and tracks proposed, assessed, and committed improvements. | <b>Tools:</b> Custom (RSPL / SEPL self-evolution protocol), MMEngine configs, persistent memory, versioned resources<br><b>Models:</b> OpenRouter, OpenAI, Anthropic, Google Gemini; configurable API bases |
| [MLE-agent](https://github.com/MLSysOps/MLE-agent)<br><img src="https://img.shields.io/github/stars/MLSysOps/MLE-agent?style=flat" alt="GitHub stars" height="20"> | ML engineering agent for baseline construction, local execution, debugging, and Kaggle workflows, with code retrieval and project reports. | <b>Tools:</b> Python CLI, Kaggle, code RAG, local execution<br><b>Models:</b> OpenAI, Anthropic, Gemini, DeepSeek, Mistral, Ollama, vLLM; optional LiteLLM |
| [AIDE](https://github.com/WecoAI/aideml)<br><img src="https://img.shields.io/github/stars/WecoAI/aideml?style=flat" alt="GitHub stars" height="20"> | Open-source reference implementation of AIDE. Searches a tree of candidate ML programs, using execution results and a user-defined metric to guide drafting, debugging, and improvement. [[paper]](https://arxiv.org/abs/2502.13138) | <b>Tools:</b> Agentic tree search, Python CLI, Streamlit, Docker<br><b>Models:</b> OpenAI, Anthropic, Gemini; OpenAI-compatible local models such as Ollama |
| [CORAL](https://github.com/Human-Agent-Society/CORAL)<br><img src="https://img.shields.io/github/stars/Human-Agent-Society/CORAL?style=flat" alt="GitHub stars" height="20"> | Infrastructure for autoresearch-style experiment loops. Parallel coding agents share findings and reusable skills, while graders evaluate attempts; supports multi-island exploration and migration. | <b>Tools:</b> Multi-agent Git worktrees, graders, shared state, Docker, optional **LiteLLM**<br><b>Models:</b> Claude Code, OpenCode, Codex, Cursor Agent, Kiro; optional LiteLLM gateway |

[↑ Back to contents](#-table-of-contents)

## ✍️ Academic Writing & Communication

> Tools focused on reading, polishing, illustrating, presenting, and responding to reviews for scientific work.

| Project & Stars | Description | Framework & LLM APIs |
|---|---|---|
| [ChatPaper](https://github.com/kaixindelele/ChatPaper)<br><img src="https://img.shields.io/github/stars/kaixindelele/ChatPaper?style=flat" alt="GitHub stars" height="20"> | Uses ChatGPT to summarize arXiv and local PDF papers, translate and polish manuscripts, analyze reviews, and draft reviewer responses. | <b>Tools:</b> PyMuPDF, arxiv.py, Flask, Gradio, Docker<br><b>Models:</b> OpenAI |
| [PaperBanana](https://github.com/dwzhu-pku/PaperBanana)<br><img src="https://img.shields.io/github/stars/dwzhu-pku/PaperBanana?style=flat" alt="GitHub stars" height="20"> | Reference-driven academic illustration framework with Retriever, Planner, Stylist, Visualizer, and Critic agents. Iteratively generates diagrams and plots from scientific content, with configurable vision-language and image models. | <b>Tools:</b> Five-agent illustration pipeline, Gradio, Streamlit, OpenRouter<br><b>Models:</b> Google Gemini; OpenAI, Anthropic, and other providers through OpenRouter |
| [Paper2Poster](https://github.com/Paper2Poster/Paper2Poster)<br><img src="https://img.shields.io/github/stars/Paper2Poster/Paper2Poster?style=flat" alt="GitHub stars" height="20"> | NeurIPS 2025. Converts a paper PDF into an editable academic poster (`.pptx`). Also provides a lightweight coding-agent skill for preparing poster-ready content. | <b>Tools:</b> Multi-agent pipeline, editable PowerPoint output, vLLM, Docker<br><b>Models:</b> OpenAI; open-weight language and vision models through vLLM |
| [ChatReviewer](https://github.com/nishiwen1214/ChatReviewer)<br><img src="https://img.shields.io/github/stars/nishiwen1214/ChatReviewer?style=flat" alt="GitHub stars" height="20"> | Uses ChatGPT to summarize paper strengths and weaknesses and suggest improvements. Its ChatResponse tool drafts point-by-point responses to reviewer comments; based on ChatPaper. | <b>Tools:</b> Python, PyMuPDF, tiktoken, Gradio, Docker, HuggingFace Spaces<br><b>Models:</b> OpenAI |

[↑ Back to contents](#-table-of-contents)

## 🔧 Research Skills & Plugin Collections

> Reusable skill sets and plugin ecosystems that integrate with coding agents (Claude Code, Codex, Gemini CLI, etc.) to enable research workflows.

| Project & Stars | Description | Framework & LLM APIs |
|---|---|---|
| [scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)<br><img src="https://img.shields.io/github/stars/K-Dense-AI/scientific-agent-skills?style=flat" alt="GitHub stars" height="20"> | 177 scientific and research skills covering biology, chemistry, medicine, physics, engineering, Earth science, data analysis, and scientific communication, with reusable guidance for packages, databases, and workflows. | <b>Tools:</b> Agent Skills / Agent Plugins, scientific Python libraries, scientific databases<br><b>Models:</b> Agent-agnostic: Claude Code, Cursor, Codex, Google Antigravity, and compatible hosts |
| [AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs)<br><img src="https://img.shields.io/github/stars/Orchestra-Research/AI-Research-SKILLs?style=flat" alt="GitHub stars" height="20"> | 98 skills across 23 categories for the AI research lifecycle, including an autoresearch orchestration layer, ideation, training, evaluation, experiments, and paper writing. | <b>Tools:</b> Agent Skills, DeepSpeed, vLLM, LangChain, W&B, MLflow<br><b>Models:</b> Agent-agnostic: Claude Code, Codex, Gemini CLI, OpenCode, and compatible hosts |
| [OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills)<br><img src="https://img.shields.io/github/stars/FreedomIntelligence/OpenClaw-Medical-Skills?style=flat" alt="GitHub stars" height="20"> | 869 medical and scientific skills spanning clinical reports, genomics, drug discovery, bioinformatics, structural biology, and biomedical databases, aggregated from multiple skill collections. | <b>Tools:</b> Agent Skills, **OpenClaw** / **NanoClaw**, biomedical tools and databases<br><b>Models:</b> Host-agent providers through OpenClaw / NanoClaw |

[↑ Back to contents](#-table-of-contents)

## 📋 Awesome Lists & Surveys

> Curated collections and survey papers on the auto-research landscape.

| Project & Stars | Description |
|---|---|
| [awesome-autoresearch](https://github.com/webfuse-com/awesome-autoresearch)<br><img src="https://img.shields.io/github/stars/webfuse-com/awesome-autoresearch?style=flat" alt="GitHub stars" height="20"> | Curated index of autonomous improvement loops and research agents inspired by Karpathy's autoresearch, including platform ports, domain adaptations, evaluations, and case studies. |
| [awesome-ai-for-science](https://github.com/ai4s-research/awesome-ai-for-science)<br><img src="https://img.shields.io/github/stars/ai4s-research/awesome-ai-for-science?style=flat" alt="GitHub stars" height="20"> | Curated list of AI tools, libraries, papers, datasets, and frameworks for scientific discovery across physics, chemistry, biology, and materials. |
| [Autonomous-Agents](https://github.com/tmgthb/Autonomous-Agents)<br><img src="https://img.shields.io/github/stars/tmgthb/Autonomous-Agents?style=flat" alt="GitHub stars" height="20"> | Daily-updated curated collection of research papers on autonomous LLM agents. Covers multi-agent systems, scientific computing, robotics, and more. |
| [Awesome-Deep-Research](https://github.com/DavidZWZ/Awesome-Deep-Research)<br><img src="https://img.shields.io/github/stars/DavidZWZ/Awesome-Deep-Research?style=flat" alt="GitHub stars" height="20"> | Curated collection of agentic deep research products, open-source implementations, research papers, benchmarks, and applications; includes a position paper on reasoning-driven search. |

[↑ Back to contents](#-table-of-contents)

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
