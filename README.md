# ai-agents-sentiment-analysis
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

