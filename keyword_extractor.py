import spacy

nlp = spacy.load("en_core_web_sm")

def extract_keywords(text):
    doc = nlp(text)

    keywords = set()

    # Noun phrases (better context)
    for chunk in doc.noun_chunks:
        if len(chunk.text.split()) > 1:
            keywords.add(chunk.text.strip())

    # Important single words
    for token in doc:
        if (
            token.pos_ in ["NOUN", "PROPN"]
            and not token.is_stop
            and len(token.text) > 2
        ):
            keywords.add(token.text.strip())

    return list(keywords)