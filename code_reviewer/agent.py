import os
from dotenv import load_dotenv
from langgraph.prebuilt import create_react_agent  # noqa
from code_reviewer.tools import analyser_style, detecter_bugs, verifier_securite, suggerer_refactoring

load_dotenv()

SYSTEM_PROMPT = """You are a senior Python code reviewer.

When given code to review, you MUST:
1. Call analyser_style with the full code
2. Call detecter_bugs with the full code
3. Call verifier_securite with the full code
4. Call suggerer_refactoring with the full code
5. After ALL 4 tools have returned results, write the final review as a Markdown report.

Final report format:
## 🔴 Bugs
## 🟡 Security
## 🔵 Style
## ✅ Refactoring Suggestions
## Summary

Call all tools before writing the report. Do not skip any tool."""


def _get_llm():
    if os.getenv("GROQ_API_KEY"):
        from langchain_groq import ChatGroq
        return ChatGroq(model="llama-3.3-70b-versatile", temperature=0)
    from langchain_ollama import ChatOllama
    return ChatOllama(model="qwen2.5:3b")


def review_code(code: str) -> str:
    llm = _get_llm()
    tools = [analyser_style, detecter_bugs, verifier_securite, suggerer_refactoring]
    agent = create_react_agent(llm, tools=tools, prompt=SYSTEM_PROMPT)

    result = agent.invoke({
        "messages": [("user", f"Review this Python code:\n\n```python\n{code}\n```")]
    })
    return result["messages"][-1].content
