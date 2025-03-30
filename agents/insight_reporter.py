from utils.llm_runner import run_llm
import json

def generate_insight_report():
    with open("data/tweets_analyzed.json") as f:
        tweets = json.load(f)

    prompt = "Analyze these tweets about OneCard and summarize sentiments, praise, or complaints:\n"
    for t in tweets[:200]:
        prompt += f"- {t['content']} (Sentiment: {t['sentiment']})\n"
    prompt += "\nGenerate a concise internal insight report, don't make any assumption by yourself, if there is no data report it as data missing"

    report = run_llm(prompt)
    with open("data/insight_report.txt", "w") as f:
        f.write(report)
    return report
