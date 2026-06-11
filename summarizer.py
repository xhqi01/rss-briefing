import os
import anthropic
from config import TOPIC, BRIEF_FOCUS

def summarize_articles(articles):
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    articles_block = "\n\n".join(
        f"SOURCE: {a['source']}\nTITLE: {a['title']}\nURL: {a['url']}\nSNIPPET: {a['summary']}"
        for a in articles
    )

    prompt = f"""You are an intelligence analyst producing a daily news briefing.

Topic: {TOPIC}

Focus guidelines:
{BRIEF_FOCUS.strip()}

Articles from the past 24 hours:
{articles_block}

Produce a concise briefing with this structure:

## Overview
2-3 sentence executive summary of the most important developments.

## Key Developments
Bullet points, most critical first. Cite source in brackets e.g. *[Reuters]*

## What to Watch
1-2 things to monitor in the next 24-48 hours.

Rules:
- Factual and neutral only. No speculation.
- Omit sections with no relevant content.
- No repeated information.
- Under 400 words total."""

    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}],
    )

    return message.content[0].text
