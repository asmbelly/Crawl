import ollama
from config import MODEL

def build_prompt(query: str, results: list[dict]) -> str:
    """Build a prompt from the user query and scraped web results."""
    context = ""
    for i, r in enumerate(results, 1):
        context += f"\n--- Source {i}: {r['title']} ({r['url']}) ---\n"
        context += r.get("content", r.get("snippet", "")) + "\n"

    prompt = f"""You are Crawl, a smart web browsing assistant. 
A user asked: "{query}"

Here is information gathered from the web:
{context}

Based on the above sources, give a clear, accurate, and helpful answer to the user's question.
Cite which sources you used by mentioning Source 1, Source 2, etc.
If the sources don't fully answer the question, say so honestly.
Do NOT ask follow-up questions or invite further conversation at the end of your response. Just answer and stop.
"""
    return prompt


def ask(query: str, results: list[dict]) -> str:
    """Send the prompt to the local Ollama model and return the response."""
    prompt = build_prompt(query, results)
    try:
        response = ollama.chat(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}]
        )
        return response["message"]["content"]
    except Exception as e:
        return f"Model error: {e}\nMake sure Ollama is running and '{MODEL}' is pulled."