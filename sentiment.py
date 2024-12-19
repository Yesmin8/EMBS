from api_utils import call_huggingface_api
from config import SENTIMENT_API_URL, label_to_sentiment, logger

def analyze_sentiment(text):

    try:
        if not isinstance(text, str) or not text.strip():
            raise ValueError("Input text must be a non-empty string.")

        payload = {"inputs": text}
        result = call_huggingface_api(SENTIMENT_API_URL, payload)

        return [
            {"sentiment": label_to_sentiment.get(item["label"], "Unknown"), "score": item["score"]}
            for item in result[0]
        ]
    except Exception as e:
        logger.error(f"Sentiment analysis error: {e}")
        return {"error": str(e)}
