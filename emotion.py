from api_utils import call_huggingface_api
from config import EMOTION_API_URL, logger, grouped_emotions

def analyze_emotion(text, score_threshold=0.1):
    try:
        if not isinstance(text, str) or not text.strip():
            raise ValueError("Input text must be a non-empty string.")

        payload = {"inputs": text}
        result = call_huggingface_api(EMOTION_API_URL, payload)

        
        emotions = [
            {"emotion": item["label"], "score": item["score"]}
            for item in result[0] if item["score"] >= score_threshold
        ]

        if not emotions:
            logger.info("No significant emotions detected.")
            return {"type": "Emotion", "grouped_emotions": None, "individual_emotions": None}

       
        sorted_emotions = sorted(emotions, key=lambda x: x["score"], reverse=True)

      
        grouped_results = {"positive": 0, "negative": 0, "neutral": 0, "mixed": 0}
        for emotion in sorted_emotions:
            for category, group in grouped_emotions.items():
                if emotion["emotion"] in group:
                    grouped_results[category] += emotion["score"]
                    break

   
        total_score = sum(grouped_results.values())
        if total_score > 0:
            grouped_results = {key: score / total_score for key, score in grouped_results.items()}

        
        return {
            "type": "Emotion",
            "grouped_emotions": grouped_results,
            "individual_emotions": sorted_emotions  
        }

    except Exception as e:
        logger.error(f"Emotion analysis error: {e}")
        return {"error": str(e)}
