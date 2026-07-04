import requests
from markdownify import markdownify as md
from pathlib import Path

from .constants import BASE_URL, MARKDOWN_DIR, PER_PAGE
from .utils import slugify


def fetch_articles(page: int = 1) -> list:
    """
    Fetch one page of articles from Zendesk.
    """

    response = requests.get(
        BASE_URL,
        params={
            "page": page,
            "per_page": PER_PAGE,
        },
    )

    response.raise_for_status()

    data = response.json()

    return data["articles"]

def convert_to_markdown(article: dict) -> str:
    """
    Convert article HTML body into Markdown.
    """

    body = md(article["body"])

    return f"""# {article["title"]}

Article URL: {article["html_url"]}

{body}
"""

def save_markdown(article: dict, markdown: str) -> None:
    """
    Save markdown into data/markdown.
    """

    MARKDOWN_DIR.mkdir(parents=True, exist_ok=True)

    filename = slugify(article["title"]) + ".md"

    filepath = MARKDOWN_DIR / filename

    filepath.write_text(markdown, encoding="utf-8")


def process_article(article: dict) -> None:
    """
    Convert and save one article.
    """

    markdown = convert_to_markdown(article)

    save_markdown(article, markdown)

def run(limit: int = PER_PAGE):
    """
    Scrape first N articles.
    """

    articles = fetch_articles()

    for article in articles[:limit]:
        process_article(article)

    print(f"Saved {min(limit, len(articles))} articles.")