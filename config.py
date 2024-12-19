import os
import logging

# API URLs
SENTIMENT_API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment"
TOXICITY_API_URL = "https://api-inference.huggingface.co/models/unitary/toxic-bert"
EMOTION_API_URL = "https://api-inference.huggingface.co/models/SamLowe/roberta-base-go_emotions"

# API Token
API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN", "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")

# Logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Sentiment label mapping
label_to_sentiment = {"LABEL_0": "Negative", "LABEL_1": "Neutral", "LABEL_2": "Positive"}
# Emotion grouping configuration
grouped_emotions = {
    "positive": ["admiration", "amusement", "approval", "caring", "excitement", "gratitude", "happiness", "love", "optimism", "pride", "relief"],
    "negative": ["anger", "annoyance", "disappointment", "disapproval", "disgust", "fear", "grief", "remorse", "sadness"],
    "neutral": ["neutral", "realization", "confusion"],
    "mixed": ["desire", "embarrassment", "surprise"]
}
