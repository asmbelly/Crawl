import requests
from bs4 import BeautifulSoup
from config import MAX_PAGE_CHARS, TIMEOUT

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
}

def scrape(url: str) -> str:
    """Fetch a URL and return clean readable text from the page."""
    try:
        response = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Remove junk tags
        for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
            tag.decompose()

        text = soup.get_text(separator=" ", strip=True)
        # Collapse whitespace
        text = " ".join(text.split())
        return text[:MAX_PAGE_CHARS]
    except Exception:
        return ""


def scrape_all(results: list[dict]) -> list[dict]:
    """Scrape page content for each search result."""
    enriched = []
    for r in results:
        content = scrape(r["url"])
        if content:
            r["content"] = content
            enriched.append(r)
    return enriched
