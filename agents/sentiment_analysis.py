import json
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch.nn.functional as F
import torch

tokenizer = AutoTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment")
model = AutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment")

def analyze_sentiment(tweets):
    results = []
    for tweet in tweets:
        inputs = tokenizer(tweet["content"], return_tensors="pt", truncation=True)
        outputs = model(**inputs)
        probs = F.softmax(outputs.logits, dim=1)
        label = torch.argmax(probs).item()
        sentiment = ["Negative", "Neutral", "Positive"][label]
        tweet["sentiment"] = sentiment
        results.append(tweet)

        print(f"\n📝 Roberta Tweet: {tweet}")
        print(f"➡️ Sentiment: {sentiment}")  # Print sentiment after tweet

    with open("data/tweets_analyzed.json", "w") as f:
        json.dump(results, f, indent=2)

    return results
