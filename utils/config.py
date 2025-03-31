from dotenv import load_dotenv
import os

load_dotenv()

REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")
START_DAYS_AGO = int(os.getenv("START_DAYS_AGO", 7))
END_DAYS_AGO = int(os.getenv("END_DAYS_AGO", 5))
REDDIT_SEARCH_LIMIT = int(os.getenv("REDDIT_SEARCH_LIMIT", 10))

#KEYWORD = [kw.strip().lower() for kw in os.getenv("KEYWORDS", "onecard").split(",")]

REDDIT_SUBREDDIT = os.getenv("REDDIT_SUBREDDIT", "all")
REDDIT_TIME_FILTER = os.getenv("REDDIT_TIME_FILTER", "week")

KEYWORDS = list(set(kw.strip().lower() for kw in os.getenv("KEYWORD", "onecard").split(","))) #unique keywords, with small letter as reddit api search is not case sensitive

INSIGHT_POST_LIMIT = int(os.getenv("INSIGHT_POST_LIMIT", 10)) #for insight_reporter.py
