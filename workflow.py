from agents import content_retrieval, sentiment_analysis, insight_reporter

def run_workflow(days):
    print("\n🚀 Starting Workflow...\n")
    tweets = content_retrieval.fetch_tweets_serpapi(days=days)
    print(days, "days") # Print the number of days for which tweets are fetched
    analyzed = sentiment_analysis.analyze_sentiment(tweets)
    report = insight_reporter.generate_insight_report()
    print("\n🔍 Final Insight Report:\n", report)
