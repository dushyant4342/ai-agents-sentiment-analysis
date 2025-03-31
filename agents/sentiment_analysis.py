import json
import csv
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch.nn.functional as F
import torch
from datetime import datetime
from utils.llm_runner import run_llm

from datetime import datetime, timedelta, timezone
import pytz
from utils.config import REDDIT_TIME_FILTER  # if it's in your config
# Create IST time suffix
ist = pytz.timezone("Asia/Kolkata")
now_ist = datetime.now(ist)
timestamp_suffix = now_ist.strftime(f"%Y-%m-%d_%H-%M_{REDDIT_TIME_FILTER}")


tokenizer = AutoTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment")
model = AutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment")

def analyze_sentiment(posts):
    results = []

    for post in posts:
        content_text = post.get("selftext", "")
        inputs = tokenizer(content_text, return_tensors="pt", truncation=True, max_length=512)
        outputs = model(**inputs)
        probs = F.softmax(outputs.logits, dim=1)
        score = torch.max(probs).item()
        label = torch.argmax(probs).item()
        sentiment = ["Negative", "Neutral", "Positive"][label]

        post["sentiment"] = sentiment
        post["score"] = round(score, 4)

        comments_text = " ".join(post["comments"])
        print("=" * 80)


        # === 🧠 TITLE SUMMARY ===
        title_prompt = (
            f"<s>[INST] Summarize the following Reddit post title in less than 20 words:\n"
            f"{post['title']}\n"
            f"[/INST]"
        )
        title_summary = run_llm(title_prompt).strip()

        print("🧠 Title Insight:", title_summary)
        print("=" * 80)

        # === 🧠 CONTENT SUMMARY ===
        content_prompt = (
            f"<s>[INST] Summarize the following Reddit post content in less than 50 words:\n"
            f"{content_text}\n"
            f"[/INST]"
        )
        content_summary = run_llm(content_prompt).strip()

        print("🧠 Content Insight:", content_summary)
        print("=" * 80)

        # === 🧠 COMMENTS SUMMARY ===
        comments_prompt = (
            f"<s>[INST] Summarize the user comments below in less than 50 words:\n"
            f"{comments_text}\n"
            f"[/INST]"
        )
        comments_summary = run_llm(comments_prompt).strip()
        print("🧠 Comments Insight:", comments_summary)


        # 📝 Save individual insights
        post["title_insight"] = title_summary
        post["content_insight"] = content_summary
        post["comments_insight"] = comments_summary

        # ✅ Append to final results
        results.append(post)

    # 💾 Save structured data to JSON
    with open(f"data/reddit_analyzed_{timestamp_suffix}.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    # 💾 Export to CSV
    with open(f"data/reddit_export_{timestamp_suffix}.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([
            "Title", "Content", "Comments", "Sentiment", "Sentiment Score",
            "Posted Date", "URL",
            "Title Insight", "Content Insight", "Comments Insight"
        ])

        for post in results:
            comments_text = "; ".join(post["comments"])
            writer.writerow([
                post["title"],
                post.get("selftext", ""),
                comments_text,
                post["sentiment"],
                post["score"],
                post["created_utc"],
                post["url"],
                post["title_insight"],
                post["content_insight"],
                post["comments_insight"]
            ])

    print("✅ Exported to data/reddit_export.csv with clean insights and scores.")
    print(f"✅ Export complete. {len(results)} posts written.")

    return results
