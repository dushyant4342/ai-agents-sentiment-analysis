from utils.llm_runner import run_llm
import json
from utils.config import *


from datetime import datetime, timedelta, timezone
import pytz
from utils.config import REDDIT_TIME_FILTER  # if it's in your config

# Create IST time suffix
ist = pytz.timezone("Asia/Kolkata")
now_ist = datetime.now(ist)
timestamp_suffix = now_ist.strftime(f"%Y-%m-%d_%H-%M_{REDDIT_TIME_FILTER}")


def generate_insight_report(source_file="data/reddit_analyzed.json"):
    with open(source_file) as f:
        posts = json.load(f)

    if not posts:
        print("⚠️ No posts to analyze. Skipping report generation.")
        return "⚠️ No Reddit data available for this date range."

    prompt = (
        "<s>[INST] You are an internal analyst reviewing customer Reddit feedback..."
        "Please write a concise internal insight report with the following sections:\n"
        "- Common positive themes\n"
        "- Common complaints or concerns\n"
        "- Emerging issues or praise\n"
        "- Overall sentiment analysis summary\n\n"
        "Here are the posts:\n\n"
    )

    for i, post in enumerate(posts[:INSIGHT_POST_LIMIT], start=1):
        prompt += (
            f"{i}. Title: {post['title']}\n"
            f"   Sentiment: {post['sentiment']} (score: {post['score']})\n"
            f"   Content Insight: {post.get('content_insight', '')}\n"
            f"   Comments Insight: {post.get('comments_insight', '')}\n\n"
        )

    prompt += "Generate the internal insight report based on these observations.\n[/INST]"


    report = run_llm(prompt)

    with open(f"data/reddit_insight_{timestamp_suffix}.txt", "w", encoding="utf-8") as f:
        f.write(report)

    return report
