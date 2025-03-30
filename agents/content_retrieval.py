from serpapi import GoogleSearch
import json
from datetime import datetime, timedelta

def fetch_tweets_serpapi(query=None, days = 2 , max_results=200):
    if not query:
           query = (
        ' "OneCard" OR "onecard" OR "one card" OR "One card" OR "One Card" OR "@GetOneCardIN" OR "@OneCardHelp" '
        '-site:twitter.com/OneCardHelp '
        '-site:twitter.com/GetOneCardIN '
        'site:twitter.com '
        'after:' + (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
         )
    
    since_date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
    print(f'since_date:{since_date}')

    search = GoogleSearch({
        "q": query,
        "engine": "google",
        "location": "India",
        "hl": "en",
        "gl": "in",
        "num": max_results,
        "api_key": "",
        "start": 0,
        "filter": 0,  # Show all results, including similar ones
        "no_cache": True  # Avoid cached results
    })

    results = search.get_dict()
    tweets = []

    if "organic_results" in results:
        for item in results["organic_results"]:
            tweet = {
                "title": item.get("title"),
                "link": item.get("link"),
                "snippet": item.get("snippet"),
                "date": item.get("date", since_date),
                "content": item.get("snippet")
            }
            tweets.append(tweet)
            print(f"\n📝 Tweet: {tweet['content']}")
    
    with open("data/tweets.json", "w", encoding="utf-8") as f:
        json.dump(tweets, f, indent=2, ensure_ascii=False)

    if not tweets:
        print("\n⚠️ No relevant tweets retrieved!")

    return tweets

#curl "https://serpapi.com/search.json?q=OneCard+site%3Atwitter.com&api_key=snknsvkn" - test locally
