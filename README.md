# rss-briefing

Monitors any topic across major news RSS feeds, summarizes the last 24 hours using Claude, and delivers a clean email briefing every morning via GitHub Actions.

## Customize

Everything lives in `config.py`:

```python
TOPIC = "The ongoing war involving Iran"

BRIEF_FOCUS = """
Cover: military operations, airstrikes, diplomatic negotiations...
Ignore: domestic politics, sports...
"""

KEYWORDS = ["iran", "tehran", "irgc", ...]

SOURCES = [
    {"name": "Reuters World", "url": "https://feeds.reuters.com/reuters/worldNews"},
    ...
]
```

Change `TOPIC`, `BRIEF_FOCUS`, `KEYWORDS`, and `SOURCES` to monitor anything.

## Setup

```bash
git clone https://github.com/xhqi01/rss-briefing.git
cd rss-briefing
pip install -r requirements.txt
cp .env.example .env
```

Fill in `.env`:

```
ANTHROPIC_API_KEY=sk-ant-xxxx
EMAIL_SENDER=you@gmail.com
EMAIL_PASSWORD=xxxx xxxx xxxx xxxx
RECIPIENT_EMAIL=you@gmail.com
```

Gmail App Password: generate at [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords).

Run manually:

```bash
python main.py
```

## Schedule via GitHub Actions

Runs automatically at **8:00 AM JST** every day.

1. Push to GitHub
2. Go to **Settings → Secrets and variables → Actions**
3. Add four secrets: `ANTHROPIC_API_KEY`, `EMAIL_SENDER`, `EMAIL_PASSWORD`, `RECIPIENT_EMAIL`

To trigger manually: **Actions → Daily News Briefing → Run workflow**

## Stack

Python · Claude (claude-haiku) · feedparser · Gmail SMTP · GitHub Actions
