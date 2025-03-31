# Sentiment Analysis Agents
This project is a modular AI agent pipeline built to analyze public sentiment around the OneCard ecosystem (including OneScore and FPLTech) across social media — starting with Reddit (with optional Twitter support).

🧩 System Overview
The project is built using local language models and open APIs to run entirely on your local machine — no external LLM API costs required.

It supports:
📅 Custom date ranges
📚 Multi-keyword filtering
📈 Sentiment scoring
✍️ Summarization & reporting
🧠 Autonomous agents working in coordination
🤖 AI Agent Workflow
Agent	Role
🗂️ ContentRetrievalAgent	Fetches Reddit posts using keyword filters and date range
❤️ SentimentAnalysisAgent	Uses Roberta to analyze post sentiment and score confidence
🧾 InsightReporterAgent	Uses Mistral LLM to summarize title/content/comments
🧠 InsightAggregatorAgent	Compiles a high-level internal insight report for strategy
The agents are autonomously triggered via reddit_workflow.py and export structured data and summaries to:
data/reddit_posts.json
data/reddit_analyzed.json
data/reddit_export.csv
data/reddit_insight.txt

📚 Key Libraries Used
praw – Reddit API wrapper
transformers – Hugging Face sentiment model
llama-cpp-python – Local LLM runner for GGUF models
torch – Sentiment prediction engine
csv/json – Output formats
dotenv – Configurable .env loading
datetime – Date range filtering

🧠 Models Used
Task	Model
Sentiment Analysis	cardiffnlp/twitter-roberta-base-sentiment (HF Transformers)
LLM Summarization	mistral-7b-instruct-v0.1.Q5_K_M.gguf via llama-cpp-python
🌐 APIs and Data Sources
✅ Reddit API via praw
❌ No need for Twitter API (optional SerpAPI fallback possible)
✅ Fully offline for LLM processing (no OpenAI/Anthropic API usage)

🗝️ Keywords Supported
Defined in .env as comma-separated list:
KEYWORD=onecard,one card,OneCard,One Card,one credit card,onescore
Only posts matching at least one of these keywords are processed.

⚙️ Config via .env
All key settings can be controlled without editing code:
REDDIT_CLIENT_ID=your_id
REDDIT_CLIENT_SECRET=your_secret
REDDIT_USER_AGENT=your_app_name
KEYWORD=onecard,one card,OneCard
REDDIT_SUBREDDIT=CreditCardsIndia
REDDIT_TIME_FILTER=week
REDDIT_SEARCH_LIMIT=25
INSIGHT_POST_LIMIT=10

📦 Output Files
File	Description
reddit_posts.json	Raw fetched Reddit data
reddit_analyzed.json	Posts with sentiment & LLM summaries
reddit_export.csv	CSV report with title, content, comments, sentiment, score, insights
reddit_insight.txt	Final internal summary report







#Rough work ai-agents-sentiment-analysis
sentiment-analysis, dashboard creation, Insight Reporter Agent, Content Creator etc.


                  ┌───────────────────────┐
                  │   Workflow Manager    │
                  └──────────┬────────────┘
                             │
           ┌────────────────▼────────────────┐
           │        ContentRetrievalAgent     │
           │   (scrapes tweets using snscrape)│
           └────────────────┬────────────────┘
                            │
              ┌─────────────▼────────────┐
              │ SentimentAnalysisAgent   │
              │ (analyzes tweets locally)│
              └─────────────┬────────────┘
                            │
         ┌──────────────────▼──────────────────┐
         │         InsightReporterAgent        │
         │  (generates report using mistral)   │
         └──────────────────┬──────────────────┘
                            ▼
                (optional) ContentCreatorAgent


1. 🔴 PyTorch does not support AMD GPUs out-of-the-box
PyTorch only supports NVIDIA GPUs with CUDA
Your AMD GPU (5300M) will not be used
2. 🔴 Intel UHD is not for model inference
This is an integrated GPU for basic graphics only
PyTorch doesn't support it for model acceleration

✅ What Happens Instead:
PyTorch will run on your CPU by default
This model cardiffnlp/twitter-roberta-base-sentiment is small (~125MB) and runs fine on CPU

Cost: Around $100/month (as of recent pricing information, always check the official X Developer Platform for current prices).
Limits: Includes access to the search/recent endpoint (tweets from the last 7 days). Typically allows fetching around 10,000 tweets per month and posting 50,000 tweets per month.

Getting All Replies to a Specific Tweet: If your search finds an original tweet mentioning "OneCard", and you want to retrieve all replies to that specific tweet (even replies that don't mention "OneCard"), you need to perform a different kind of query. You would typically:
Get the conversation_id of the original tweet from the initial search results.
Make a separate API call using a query operator like conversation_id:<the_id_here> possibly combined with is:reply or targeting replies to the original author (to:<original_author_handle>). This retrieves tweets that are part of that specific conversation thread.
API Call Consumption: Remember that fetching replies, especially via separate conversation_id lookups, consumes your API call limits and tweet fetch limits (e.g., the 10,000 tweets/month on Basic).


Yes, you can reply to customer tweets using the X (Twitter) API.
Fetch the customer's tweet (and its ID).
Generate a reply using an LLM.
Post the reply using the X API's tweet creation endpoint, specifying the customer's tweet ID to make it a reply.


Now, I will try to get the reddit api to work on the same flow instead of twitter.




llama-cpp-python to run local LLMs (like Mistral) efficiently without relying on OpenAI or cloud APIs.
Loads GGUF models (optimized for CPU/GPU)
Runs fully offline ✅
Saves cost 💸
Supports quantization (like Q4/Q5) for speed/memory tradeoffs

The llama_perf_context_print logs show:
⏱️ Load time
🧠 Prompt evaluation (tokens processed)
🛠️ Inference speed (tokens/sec)

Lllama.generate: 12 prefix-match hit, remaining 104 prompt tokens to eval
llama_perf_context_print:        load time =   11300.85 ms
llama_perf_context_print: prompt eval time =   10428.27 ms /   104 tokens (  100.27 ms per token,     9.97 tokens per second)
llama_perf_context_print:        eval time =   10559.36 ms /    59 runs   (  178.97 ms per token,     5.59 tokens per second)
llama_perf_context_print:       total time =   21000.66 ms /   163 tokens

12 prefix-match hit: 12 tokens were cached (faster to reuse)
104 prompt tokens: Number of tokens in your input prompt
59 runs: Tokens the model generated in response

Load time: ~11s → time to load the model into memory
Prompt eval time: ~10.4s → time to process the prompt
Eval time: ~10.5s → time to generate the output
Total time: ~21s → full round-trip (prompt + generation)
