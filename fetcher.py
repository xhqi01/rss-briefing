import feedparser
from datetime import datetime, timezone, timedelta
from config import SOURCES, KEYWORDS, HOURS_BACK

def fetch_articles():
    cutoff  = datetime.now(timezone.utc) - timedelta(hours=HOURS_BACK)
    results = []
    seen    = set()

    for source in SOURCES:
        try:
            feed = feedparser.parse(source["url"])
            for entry in feed.entries:
                title   = entry.get("title", "")
                summary = entry.get("summary", "") or entry.get("description", "")
                link    = entry.get("link", "")

                # Deduplicate by URL
                if link in seen:
                    continue

                # Date filter
                published = entry.get("published_parsed")
                if published:
                    pub_dt = datetime(*published[:6], tzinfo=timezone.utc)
                    if pub_dt < cutoff:
                        continue

                # Keyword filter
                text = (title + " " + summary).lower()
                if not any(kw.lower() in text for kw in KEYWORDS):
                    continue

                seen.add(link)
                results.append({
                    "source":  source["name"],
                    "title":   title,
                    "url":     link,
                    "summary": summary[:400],
                })

        except Exception as e:
            print(f"  ✗ {source['name']}: {e}")

    print(f"  Found {len(results)} matching articles across {len(SOURCES)} sources")
    return results
