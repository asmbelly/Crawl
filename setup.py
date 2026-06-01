from setuptools import setup, find_packages

setup(
    name="crawl",
    version="1.0.0",
    description="A local web-browsing AI assistant powered by Ollama and DuckDuckGo",
    author="asmbelly",
    packages=find_packages(),
    py_modules=["main", "search", "scraper", "brain", "config"],
    install_requires=[
        "ddgs",
        "beautifulsoup4",
        "requests",
        "rich",
        "ollama",
    ],
    entry_points={
        "console_scripts": [
            "crawl=main:run",
        ],
    },
    python_requires=">=3.10",
)
