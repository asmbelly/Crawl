from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.live import Live
from rich.text import Text
from rich.rule import Rule

from search import search
from scraper import scrape_all
from brain import ask
from config import MODEL

console = Console()

BANNER = """
      [bold dark_orange]▄█▄   ▄█▄[/bold dark_orange]
    [bold dark_orange]██████ ██████[/bold dark_orange]
   [bold dark_orange]█████████████[/bold dark_orange]  [bold white]CRAWL[/bold white]
    [bold orange1]███[/bold orange1][bold dark_orange]█████[/bold dark_orange][bold orange1]███[/bold orange1]
      [bold orange1]███████[/bold orange1]
        [bold orange1]███[/bold orange1]
"""

def show_banner():
    console.print(BANNER)
    console.print(
        Panel(
            f"[bold white]Web-browsing AI assistant[/bold white]\n[dim]Powered by [bold]{MODEL}[/bold] via Ollama  •  Search by DuckDuckGo[/dim]",
            border_style="dark_orange",
            padding=(0, 2)
        )
    )
    console.print()

def run():
    show_banner()
    console.print("[dim]Type your question below. Type [bold]exit[/bold] to quit.[/dim]\n")

    while True:
        try:
            query = Prompt.ask("[bold dark_orange]crawl[/bold dark_orange][white]>[/white]")
        except (KeyboardInterrupt, EOFError):
            console.print("\n[dim]Goodbye! 🐜[/dim]")
            break

        if query.strip().lower() in ("exit", "quit", "q"):
            console.print("[dim]Goodbye! 🐜[/dim]")
            break

        if not query.strip():
            continue

        # Step 1: Search
        with Live(console=console, refresh_per_second=10) as live:
            live.update(Text("🐜 Scouting the web...", style="dark_orange dim"))
            results = search(query)

        if not results:
            console.print("[red]No search results found. Try a different query.[/red]\n")
            continue

        console.print(f"[dim]Found {len(results)} results. Reading pages...[/dim]")

        # Step 2: Scrape
        with Live(console=console, refresh_per_second=10) as live:
            live.update(Text("📄 Reading pages...", style="dim"))
            enriched = scrape_all(results)

        if not enriched:
            enriched = results

        console.print(f"[dim]Thinking with {MODEL}...[/dim]\n")

        # Step 3: Ask the model
        with Live(console=console, refresh_per_second=10) as live:
            live.update(Text("🧠 Generating answer...", style="dim"))
            answer = ask(query, enriched)

        # Display answer
        console.print(Rule(style="dark_orange"))
        console.print(Panel(
            answer,
            title="[bold dark_orange]Crawl[/bold dark_orange]",
            border_style="dark_orange",
            padding=(1, 2)
        ))
        console.print()

        # Show sources
        console.print("[dim]Sources:[/dim]")
        for i, r in enumerate(enriched[:5], 1):
            console.print(f"  [dim]{i}. {r['title']} — {r['url']}[/dim]")
        console.print()

if __name__ == "__main__":
    run()
