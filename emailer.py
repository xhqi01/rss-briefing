import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import date
from config import TOPIC, EMAIL_SUBJECT_PREFIX

def send_email(summary, articles):
    sender   = os.environ["EMAIL_SENDER"]
    password = os.environ["EMAIL_PASSWORD"]
    receiver = os.environ["RECIPIENT_EMAIL"]

    subject = f"{EMAIL_SUBJECT_PREFIX} — {date.today().strftime('%b %d, %Y')}"

    # Convert markdown to basic HTML
    html_body = summary \
        .replace("## ", "<h3 style='margin:18px 0 6px;font-size:13px;text-transform:uppercase;letter-spacing:0.08em;color:#1a1a1a'>") \
        .replace("**", "") \
        .replace("*[", "<em style='color:#888'>[") \
        .replace("]*", "]</em>") \
        .replace("- ", "• ") \
        .replace("\n", "<br>")

    sources_html = "".join(
        f'<li><a href="{a["url"]}" style="color:#888;font-size:11px;text-decoration:none">'
        f'{a["source"]} — {a["title"][:70]}</a></li>'
        for a in articles[:12]
    )

    body = f"""
    <html><body style="font-family:monospace;background:#f7f6f3;padding:32px;margin:0">
    <div style="max-width:580px;margin:0 auto;background:#fff;border:1px solid #e0e0e0;padding:28px">

      <div style="border-bottom:1px solid #eee;padding-bottom:12px;margin-bottom:20px">
        <div style="font-size:11px;color:#aaa;letter-spacing:0.1em;text-transform:uppercase">{EMAIL_SUBJECT_PREFIX}</div>
        <div style="font-size:13px;color:#555;margin-top:2px">{date.today().strftime("%A, %B %d, %Y")} · {len(articles)} article{"s" if len(articles) != 1 else ""} scanned</div>
        <div style="font-size:11px;color:#bbb;margin-top:2px">{TOPIC}</div>
      </div>

      <div style="font-size:13px;line-height:1.75;color:#333">
        {html_body}
      </div>

      <div style="margin-top:24px;padding-top:16px;border-top:1px solid #eee">
        <div style="font-size:10px;color:#bbb;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:8px">Sources</div>
        <ul style="margin:0;padding:0 0 0 14px;list-style:disc">
          {sources_html}
        </ul>
      </div>

      <div style="margin-top:20px;font-size:10px;color:#ddd">
        rss-briefing · powered by Claude · github.com/xhqi01/rss-briefing
      </div>
    </div>
    </body></html>"""

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"]    = sender
    msg["To"]      = receiver
    msg.attach(MIMEText(body, "html"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())

    print(f"  ✓ Email sent to {receiver}")
