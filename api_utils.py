import requests
import time
from config import API_TOKEN, logger

def call_huggingface_api(url, payload, retries=3, backoff_factor=2):

    headers = {"Authorization": f"Bearer {API_TOKEN}"}

    for attempt in range(retries):
        try:
            response = requests.post(url, json=payload, headers=headers, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.warning(f"API call attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(backoff_factor ** attempt)
            else:
                logger.error("API call failed after maximum attempts.")
                return {"error": f"API call failed: {e}"}
