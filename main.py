from preprocessing import preprocess_text
from sentiment import analyze_sentiment
from toxicity import test_toxicity
from emotion import analyze_emotion
from config import logger

def main():
    input_text = "The food tasted amazing, but the service was awful."

    logger.info("Starting NLP pipeline.")
    processed_data = preprocess_text(input_text)
    logger.info(f"Processed Data: {processed_data}")

    sentiment_result = analyze_sentiment(input_text)
    logger.info(f"Sentiment Analysis: {sentiment_result}")

    toxicity_result = test_toxicity(input_text)
    logger.info(f"Toxicity Analysis: {toxicity_result}")

    emotion_result = analyze_emotion(input_text)
    logger.info(f"Emotion Analysis: {emotion_result}")

if __name__ == "__main__":
    main()
