from fastapi import APIRouter
from app.models.sentiment import TextInput, SentimentOutput
from textblob import TextBlob

router = APIRouter()

@router.post("/analyze", response_model=SentimentOutput)
def analyze_sentiment(payload: TextInput):
    blob = TextBlob(payload.text)
    polarity = blob.sentiment.polarity
    sentiment = "neutral"
    if polarity > 0:
        sentiment = "positive"
    elif polarity < 0:
        sentiment = "negative"
    return SentimentOutput(sentiment=sentiment, polarity=polarity)
