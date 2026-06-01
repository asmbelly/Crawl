from ddgs import DDGS
from config import MAX_RESULTS

def search(query: str) -> list[dict]:
    """Search DuckDuckGo and return a list of results with title, url, and snippet."""
    results = []
    try:
        with DDGS() as ddgs:
            for r in ddgs.text(query, max_results=MAX_RESULTS):
                results.append({
                    "title": r.get("title", ""),
                    "url": r.get("href", ""),
                    "snippet": r.get("body", "")
                })
    except Exception as e:
        print(f"Search error: {e}")
    return results
