I want you to make a plan in which we read all the csv data and make three columns as summary of title, selftext, comments. Then do a sentiment analysis on the column combined title, selftext with a sentiment score and sentiment positive, negative, neutral. Then analyse the complete data between onecard vs competitors sentiments, what they prefer and which card they suggest and what is their opinion about one card and all possible insights which you can compare between onecard vs competitors, after finding everything try to add it in a final csv file.

combined_text should be only two columns 'title', 'selftext' and find sentiment score & sentiment (positive,negative,neutral) on the combined_text column

Create three new columns as summary of title, summary_selftext & summary_comments.

Set token size in the model,To make sure token doesnot exceed in any of the content

Use model twitter-roberta-base-sentiment for sentiment analysis and model mistral-7b-instruct for text summarization

Set device to T4 gpu to complete it fast.

Also, suggest me a code which can send a good short to the point summary on gchat with webhook, summary should be around sentiments ratio, why these sentiments and think something good about the summary. If possible make the summary in Gchat colourful based on sentiments which will be easy to read for my team mates.