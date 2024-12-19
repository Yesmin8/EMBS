# EMBS Mental Health NLP Project

This project is part of the EMBS challenge and focuses on developing a mental health chatbot and analysis system. It incorporates advanced NLP techniques to analyze user-generated text and offers features such as emotion detection, toxicity analysis, and sentiment evaluation.

---

## Features
1. **Preprocessing**  
   - Includes tokenization, stopword removal, and lemmatization.  
   - Ensures clean and consistent input for analysis.

2. **Sentiment Analysis**  
   - Detects whether text expresses positive, neutral, or negative sentiment.  
   - Utilizes Hugging Face's sentiment analysis API.

3. **Emotion Analysis**  
   - Recognizes emotions from text using the GoEmotions model.  
   - Groups emotions into positive, negative, neutral, or mixed categories.

4. **Toxicity Detection**  
   - Identifies and measures the toxicity level in user-generated content.  
   - Helps maintain a healthy and supportive environment.

5. **Community Analysis**  
   - Processes and analyzes posts and comments in the chatbot's community platform.  
   - Detects trends and ensures content aligns with mental health support goals.

---

## Project Structure
.
├── main.py              # Main script to run the NLP pipeline
├── preprocessing.py     # Preprocessing text module
├── sentiment.py         # Sentiment analysis module
├── emotion.py           # Emotion detection module
├── toxicity.py          # Toxicity analysis module
├── config.py            # Configuration file for API settings and utilities
├── api_utils.py         # Helper functions for making API requests
├── requirements.txt     # Required Python dependencies
├── venv/                # Virtual environment

---

## Prerequisites

### System Requirements:
- **Python**: Version 3.8 or later.  
- **Virtual Environment**: Recommended for isolating dependencies.

### Required Libraries:
- `spacy`
- `requests`
- Hugging Face API access.

To install dependencies, run:
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```
---
## Usage

### Activate the virtual environment:
bash
Copier le code
```
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
Run the main script:
```
bash
Copier le code
```
python main.py
```
Explore the features:

Modify or add data in the relevant modules.
Leverage APIs for sentiment, emotion, and toxicity detection.
