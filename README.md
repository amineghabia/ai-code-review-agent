# 🤖 AI Code Review Agent

An autonomous AI agent that automatically reviews Python code on every Pull Request and posts a structured analysis as a comment.

Built with **LangGraph**, **LangChain**, and **Groq API** — deployed as a **GitHub Action**.

![AI Code Review bot commenting on a PR](docs/Screenshot%20review%20code%20agent.jpeg)

---

## What it does

Every time a Pull Request is opened or updated, the agent:

1. Detects all modified `.py` files in the PR
2. Runs 4 specialized analysis tools on each file:
   - 🔴 **Bug detection** — logic errors, unhandled edge cases, broad exceptions
   - 🟡 **Security audit** — hardcoded credentials, `eval()` usage, injection risks
   - 🔵 **Style review** — PEP8 violations, naming, function complexity
   - ✅ **Refactoring suggestions** — duplication, structure improvements
3. Posts a structured Markdown report as a PR comment

---

## Architecture

```
Pull Request opened
        ↓
GitHub Action triggers
        ↓
review.py reads changed .py files
        ↓
LangGraph agent (ReAct loop)
   ├── tool: detecter_bugs
   ├── tool: verifier_securite
   ├── tool: analyser_style
   └── tool: suggerer_refactoring
        ↓
Structured Markdown report posted as PR comment
```

The agent uses **Groq API** (llama-3.3-70b) in production and **Ollama** (qwen2.5:3b) for local development — switching automatically based on the `GROQ_API_KEY` environment variable.

---

## Local usage

**Requirements:** Python 3.11+, [Ollama](https://ollama.com) running with `qwen2.5:3b`

```bash
git clone https://github.com/amineghabia/ai-code-review-agent.git
cd ai-code-review-agent

python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt

python review.py your_file.py
```

The report is printed to stdout and saved as `review_<filename>.md`.

---

## Deploy to your repo (GitHub Action)

1. Copy `.github/workflows/code-review.yml` to your repository
2. Go to **Settings → Secrets and variables → Actions**
3. Add a secret named `GROQ_API_KEY` with your [Groq API key](https://console.groq.com)
4. Open a Pull Request — the bot will comment automatically

---

## Tech stack

| Tool | Role |
|------|------|
| [LangGraph](https://github.com/langchain-ai/langgraph) | Agent orchestration (ReAct state graph) |
| [LangChain](https://github.com/langchain-ai/langchain) | LLM interface & tool definitions |
| [Groq API](https://console.groq.com) | LLM in production (llama-3.3-70b) |
| [Ollama](https://ollama.com) | LLM for local development (qwen2.5:3b) |
| GitHub Actions | CI/CD — triggers on every Pull Request |

---

## Skills demonstrated

`AI Agents` · `LangGraph` · `ReAct Pattern` · `LLM Tool Use` · `Prompt Engineering` · `GitHub Actions` · `CI/CD` · `Python`
