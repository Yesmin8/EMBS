import spacy
from config import logger

try:
    nlp = spacy.load("en_core_web_sm")
    logger.info("SpaCy model loaded successfully.")
except Exception as e:
    logger.error(f"Failed to load SpaCy model: {e}")
    raise

def preprocess_text(text):

    try:
        if not isinstance(text, str) or not text.strip():
            raise ValueError("Input text must be a non-empty string.")

        doc = nlp(text.lower())
        important_tokens = [
            token.text for token in doc
            if not token.is_stop and not token.is_punct or token.dep_ in {"neg", "amod", "advmod"}
        ]
        lemmatized_tokens = [token.lemma_ for token in doc]
        spacy_entities = [(ent.text, ent.label_) for ent in doc.ents]

        return {
            "important_tokens": important_tokens,
            "lemmatized_tokens": lemmatized_tokens,
            "spacy_entities": spacy_entities
        }
    except Exception as e:
        logger.error(f"Error in preprocessing text: {e}")
        return {"error": str(e)}
