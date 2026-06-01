<p align="center">
  <pre>
   ██████╗██████╗  █████╗ ██╗    ██╗██╗     
  ██╔════╝██╔══██╗██╔══██╗██║    ██║██║     
  ██║     ██████╔╝███████║██║ █╗ ██║██║     
  ██║     ██╔══██╗██╔══██║██║███╗██║██║     
  ╚██████╗██║  ██║██║  ██║╚███╔███╔╝███████╗
   ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚══════╝
  </pre>
</p>

<p align="center">
  <b>A local web-browsing AI assistant. No API keys. No cloud. Just answers.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.10+-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/powered%20by-Ollama-black?style=flat-square"/>
  <img src="https://img.shields.io/badge/search-DuckDuckGo-orange?style=flat-square"/>
  <img src="https://img.shields.io/badge/license-MIT-green?style=flat-square"/>
</p>

---

## What is Crawl?

Crawl is a terminal-based AI assistant that searches the web and answers your questions — fully locally, completely free. No OpenAI API key. No Anthropic API key. Nothing.

Like an ant scouting ahead, Crawl goes out, finds what you need, and brings it back.

It works by:
1. Searching DuckDuckGo for your question
2. Scraping and reading the top results
3. Feeding that content into a local AI model via Ollama
4. Returning a clean, sourced answer in your terminal

---

## Features

- **Fully local** — everything runs on your machine, nothing is sent to external AI services
- **No API keys** — no accounts, no subscriptions, no costs
- **Source citations** — every answer shows exactly where the information came from
- **Any Ollama model** — swap between gemma3, phi3, llama3.2, mistral, or any other model you have pulled
- **Configurable** — control result count, page read depth, timeout, and model via `config.py`
- **Lightweight** — minimal dependencies, runs in any terminal
- **Windows executable** — no Python required for the pre-built `.exe` release

---

## Requirements

- **Python 3.10 or newer** — [python.org](https://python.org)
- **Ollama** — [ollama.com](https://ollama.com) (runs the local AI model)
- A pulled Ollama model (default: `gemma3`, ~3.3GB)

---

## Installation

### Option A — Windows Executable (easiest)

1. Download `crawl.exe` from the [latest release](https://github.com/asmbelly/Crawl/releases/latest)
2. Install [Ollama](https://ollama.com) and pull a model: `ollama pull gemma3`
3. Run `crawl.exe` from anywhere

---

### Option B — From source

#### Step 1 — Install Ollama

Download and install Ollama from [ollama.com](https://ollama.com), then pull a model:

```bash
ollama pull gemma3
```

> You can use any Ollama model. Lighter options: `phi3`, `llama3.2`, `mistral`

---

#### Step 2 — Clone the repo

```bash
git clone https://github.com/asmbelly/crawl
cd crawl
```

---

#### Step 3 — Install Crawl as a CLI tool

```bash
pip install -e .
```

This installs Crawl globally so you can run it from anywhere with just:

```bash
crawl
```

---

#### Alternative — Run directly without installing

```bash
pip install -r requirements.txt
python main.py
```

---

## Usage

Once installed, just open any terminal and type:

```bash
crawl
```

Then ask anything:

```
crawl> what is quantum computing?
crawl> latest news on space exploration
crawl> how does the stock market work?
```

Type `exit` or `quit` to close.

---

## Configuration

Edit `config.py` to customize Crawl:

```python
MODEL = "gemma3"       # Any Ollama model (phi3, llama3.2, mistral, etc.)
MAX_RESULTS = 5        # Number of web results to fetch
MAX_PAGE_CHARS = 3000  # Characters to read per page
TIMEOUT = 10           # Web request timeout in seconds
```

### Switching models

```bash
ollama pull phi3        # Lighter, faster (~2GB)
ollama pull llama3.2    # Great balance of speed and quality
ollama pull mistral     # Strong reasoning
```

Then update `MODEL` in `config.py`.

---

## Dependencies

| Package | Purpose |
|---|---|
| `ddgs` | DuckDuckGo search (no API key needed) |
| `beautifulsoup4` | Web page scraping |
| `requests` | HTTP requests |
| `rich` | Terminal UI and formatting |
| `ollama` | Local AI model interface |

Install all at once:

```bash
pip install -r requirements.txt
```

---

## Troubleshooting

**"Model error" or connection refused**
> Make sure Ollama is running. On Windows it usually runs in the background after install. Try opening the Ollama app or running `ollama serve` in a separate terminal.

**Slow responses**
> The model runs locally on your CPU. Larger models like `gemma3` take 30–90 seconds. Try `phi3` for faster responses.

**No search results**
> DuckDuckGo occasionally rate-limits requests. Wait a moment and try again.

---

## Contributing

Contributions are welcome. Here's how to get involved:

### Getting started

1. Fork the repo
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/Crawl`
3. Create a branch: `git checkout -b feature/your-feature-name`
4. Make your changes
5. Push and open a pull request against `main`

### What's worth contributing

- Support for additional search backends
- Better scraping/parsing for specific site types
- Streaming output as the model generates
- Config file support (TOML/JSON instead of editing `config.py` directly)
- Linux/macOS packaging
- Bug fixes and error handling improvements

### Guidelines

- Keep it local-first — no changes that require external API keys
- Match the existing code style
- Test your changes before opening a PR
- Write a clear PR description explaining what you changed and why

### Reporting bugs

Open an issue with your OS, Python version, Ollama version, and the exact error message.

---

## Mascot

Crawl's mascot is a pixel art ant — small, fast, and always busy finding what you need.

---

## Disclaimer

This is an independent open source project. Not affiliated with, sponsored by, or endorsed by any AI company. Built for fun and learning.

---

## License

MIT — free to use, modify, and distribute.
