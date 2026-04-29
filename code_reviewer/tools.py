import os
from langchain_core.tools import tool


def _llm_analyze(prompt: str) -> str:
    if os.getenv("GROQ_API_KEY"):
        from langchain_groq import ChatGroq
        llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)
    else:
        from langchain_ollama import ChatOllama
        llm = ChatOllama(model="qwen2.5:3b")
    return llm.invoke(prompt).content


@tool
def analyser_style(code: str) -> str:
    """Check PEP8 compliance, naming conventions, function length, and complexity."""
    return _llm_analyze(
        "You are a Python style reviewer. List all style issues (PEP8 violations, "
        "poor naming, functions over 20 lines, high complexity) in this code. "
        "Be specific with line references where possible. If no issues, say so.\n\n"
        f"Code:\n```python\n{code}\n```"
    )


@tool
def detecter_bugs(code: str) -> str:
    """Find potential bugs, logic errors, unhandled edge cases, and broad exceptions."""
    return _llm_analyze(
        "You are a Python bug hunter. Find potential bugs, logic errors, unhandled "
        "edge cases, and overly broad exception handlers. Be specific. "
        "If no issues found, say so.\n\n"
        f"Code:\n```python\n{code}\n```"
    )


@tool
def verifier_securite(code: str) -> str:
    """Find security vulnerabilities: hardcoded credentials, injections, exposed data."""
    return _llm_analyze(
        "You are a security auditor. Find security issues: hardcoded credentials, "
        "SQL injection risks, exposed sensitive data, use of eval/exec, insecure operations. "
        "Be specific. If no issues found, say so.\n\n"
        f"Code:\n```python\n{code}\n```"
    )


@tool
def suggerer_refactoring(code: str) -> str:
    """Suggest the top refactoring improvements: extract functions, reduce duplication."""
    return _llm_analyze(
        "You are a Python architect. Suggest the top 3 refactoring improvements: "
        "extract functions, reduce duplication, apply design patterns, improve readability. "
        "Be concise and actionable.\n\n"
        f"Code:\n```python\n{code}\n```"
    )
