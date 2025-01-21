import os
import praw
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis")
model = AutoModelForSequenceClassification.from_pretrained("mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis")

def analyze_sentiment(text):
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)
    scores = outputs.logits.softmax(dim=1).detach().numpy()[0]
    labels = ["negative", "neutral", "positive"]
    return labels[scores.argmax()]

def get_reddit_posts(subreddit_name, stock_symbol, limit=100):
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT")
    )
    subreddit = reddit.subreddit(subreddit_name)
    return [post.title for post in subreddit.search(stock_symbol, limit=limit)]
