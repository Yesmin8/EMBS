from api_utils import call_huggingface_api
from config import TOXICITY_API_URL, logger

def test_toxicity(text):
    try:
        payload = {"inputs": text}
        result = call_huggingface_api(TOXICITY_API_URL, payload)

        toxic_labels = {item["label"]: item["score"] for item in result[0] if item["score"] > 0.5}
        return {"is_toxic": bool(toxic_labels), "labels": toxic_labels}
    except Exception as e:
        logger.error(f"Toxicity detection error: {e}")
        return {"error": str(e)}
