import praw
from datetime import datetime
import json
import os
from utils.config import *
from agents.reddit_auth import verify_reddit_auth

from datetime import datetime, timedelta, timezone
import pytz
from utils.config import REDDIT_TIME_FILTER  # if it's in your config

# Create IST time suffix
ist = pytz.timezone("Asia/Kolkata")
now_ist = datetime.now(ist)
timestamp_suffix = now_ist.strftime(f"%Y-%m-%d_%H-%M_{REDDIT_TIME_FILTER}")


reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT
)

def fetch_reddit_posts():
    os.makedirs("data", exist_ok=True)
    verify_reddit_auth(reddit)

    print(f"\n🔍 Searching r/{REDDIT_SUBREDDIT} for keywords: {KEYWORDS} (time_filter={REDDIT_TIME_FILTER})")

    unique_posts = {}

    for kw in KEYWORDS:
        for submission in reddit.subreddit(REDDIT_SUBREDDIT).search(
            kw,
            limit=REDDIT_SEARCH_LIMIT,
            sort="new",
            time_filter=REDDIT_TIME_FILTER
        ):
            if submission.id in unique_posts:
                continue

            content = f"{submission.title} {submission.selftext}".lower()
            if not any(keyword in content for keyword in KEYWORDS):
                continue

            created_date = datetime.utcfromtimestamp(submission.created_utc).strftime('%Y-%m-%d')

            post = {
                "title": submission.title,
                "url": f"https://reddit.com{submission.permalink}",
                "created_utc": created_date,
                "selftext": submission.selftext,
                "comments": []
            }

            try:
                submission.comments.replace_more(limit=None)
                for comment in submission.comments.list():
                    post["comments"].append(comment.body)
            except Exception as e:
                print(f"⚠️ Couldn't fetch comments: {e}")

            unique_posts[submission.id] = post

    posts = list(unique_posts.values())

    with open(f"data/reddit_posts_{timestamp_suffix}.json", "w", encoding="utf-8") as f:
        json.dump(posts, f, indent=2, ensure_ascii=False)

    if not posts:
        print("⚠️ No Reddit posts retrieved.")
    else:
        print(f"✅ {len(posts)} posts saved to reddit_posts.json")

    return posts
