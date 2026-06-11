# ── EDIT THIS FILE TO CUSTOMIZE YOUR BRIEFING ────────────────────────────────

# What topic are you monitoring?
TOPIC = "AI and machine learning industry news"

# What should the briefing focus on?
BRIEF_FOCUS = """
Cover: new model releases, research breakthroughs, funding rounds, product launches, policy developments.
Ignore: unrelated tech news, entertainment, sports.
"""

# Keywords to filter articles (at least one must appear in title or summary)
KEYWORDS = [
    "openai", "anthropic", "google deepmind", "llm", "large language model",
    "machine learning", "ai model", "generative ai", "chatgpt", "gemini",
    "claude", "gpt", "artificial intelligence", "foundation model",
]

# RSS feeds to scan
SOURCES = [
    {"name": "Reuters Tech",    "url": "https://feeds.reuters.com/reuters/technologyNews"},
    {"name": "BBC Tech",        "url": "http://feeds.bbci.co.uk/news/technology/rss.xml"},
    {"name": "The Verge",       "url": "https://www.theverge.com/rss/index.xml"},
    {"name": "Ars Technica",    "url": "http://feeds.arstechnica.com/arstechnica/index"},
    {"name": "TechCrunch",      "url": "https://techcrunch.com/feed/"},
    {"name": "MIT Tech Review", "url": "https://www.technologyreview.com/feed/"},
]

# How many hours back to scan
HOURS_BACK = 24

# Email subject prefix
EMAIL_SUBJECT_PREFIX = "Daily AI Briefing"
