import os
from dotenv import load_dotenv
load_dotenv()

from fetcher import fetch_articles
from summarizer import summarize_articles
from emailer import send_email
from config import TOPIC

def run():
    print(f"Topic: {TOPIC}")
    print("Fetching articles...")
    articles = fetch_articles()

    if not articles:
        print("No matching articles found. No email sent.")
        return

    print("Summarizing with Claude...")
    summary = summarize_articles(articles)

    print("Sending email...")
    send_email(summary, articles)

    print("Done.")

if __name__ == "__main__":
    run()
