# ── EDIT THIS FILE TO CUSTOMIZE YOUR BRIEFING ────────────────────────────────

# What topic are you monitoring?
TOPIC = "The ongoing war involving Iran"

# What should the briefing focus on?
BRIEF_FOCUS = """
Cover: military operations, airstrikes, diplomatic negotiations, sanctions, key figures.
Ignore: domestic politics unrelated to the conflict, sports, entertainment.
"""

# Keywords to filter articles (at least one must appear in title or summary)
KEYWORDS = [
    "iran", "tehran", "irgc", "israel", "gaza", "hezbollah",
    "hamas", "beirut", "ceasefire", "airstrike", "missile",
    "nuclear", "sanctions", "netanyahu", "khamenei",
]

# RSS feeds to scan
SOURCES = [
    {"name": "Reuters World", "url": "https://feeds.reuters.com/reuters/worldNews"},
    {"name": "BBC World",     "url": "http://feeds.bbci.co.uk/news/world/rss.xml"},
    {"name": "Al Jazeera",    "url": "https://www.aljazeera.com/xml/rss/all.xml"},
    {"name": "AP Top News",   "url": "https://rsshub.app/apnews/topics/apf-topnews"},
    {"name": "Guardian World","url": "https://www.theguardian.com/world/rss"},
    {"name": "NYT World",     "url": "https://rss.nytimes.com/services/xml/rss/nyt/World.xml"},
]

# How many hours back to scan
HOURS_BACK = 24

# Email subject prefix
EMAIL_SUBJECT_PREFIX = "Daily Briefing"
