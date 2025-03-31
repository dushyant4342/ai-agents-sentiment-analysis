from agents import reddit_content_retrieval, sentiment_analysis, insight_reporter

def run_reddit_workflow():
    posts = reddit_content_retrieval.fetch_reddit_posts()
    if not posts:
        print("⚠️ Skipping analysis and report generation (no posts found).")
        return
    print("✅ Fetched Reddit Posts successfully")

    print("✅ Sentiment Analysis started")
    analyzed = sentiment_analysis.analyze_sentiment(posts)

    print("✅ Insight reporter agent work started")
    report = insight_reporter.generate_insight_report("data/reddit_analyzed.json")
    print("\n📊 Reddit Insight Report:\n", report)



    print("\n✅ Reddit workflow completed successfully.")