# 🤖 Final Master's Project – MSc in Artificial Intelligence  
**Title:** Elvex: Autonomous Architecture for LLM Agent Generation and Coordination  
**Institution:** Universidad Internacional de La Rioja (UNIR)  
**Presented:** July 2025

## 📘 Overview

This Master's Thesis presents **Elvex**, an autonomous multi-agent architecture designed to dynamically generate and coordinate **specialized LLM-based agents** to solve complex tasks without prior configuration. The system interprets high-level user queries, decomposes them, and orchestrates collaboration between auto-created agents to deliver coherent and high-quality results.

Elvex offers a **fully modular, plug-and-play** solution that adapts to the task’s structure in real time. It abstracts away the need for manual agent wiring, enabling a general-purpose framework for **reasoning, problem-solving, and tool use** through coordination of autonomous agents.

## 🧠 Key Components

- **Agent Generator**: Automatically decides how many agents are needed and defines their specialization based on subtasks.
- **Dynamic Graph Execution**: Orchestrates agent workflows based on task dependency graphs.
- **Task Decomposition and Evaluation**: Converts natural language input into atomic tasks and ensures execution quality.
- **Memory and Context Management**: Preserves relevant context across agents and iterations.

## 🔁 WORKFLOW

```text
1. Task Specifier
        ↓
2. Task Divider
        ↓
3. Task Evaluator
        ↓
4. Orchestrator (Agent Generator & Router)
        ↓
5. Worker Agents (Auto-created based on subtasks)
        ↓
6. Gatherer (Integrates responses from all agents)
        ↓
           ✅ Final Result
```

## 🪛 TECHNOLOGY USED
- **Python**
- **LangGraph**
- **Ollama**
- **OpenAI API**

## ⚙️ SETUP

To run Elvex locally, you need [Ollama](https://ollama.com) installed, or a valid OpenAI API.

1. **Install Ollama**  
   Follow the instructions at: https://ollama.com/download

2. **Download the LLaMA 3 model**  
   ```bash
   ollama pull llama3
   ```
3. Configure the model in the config file

