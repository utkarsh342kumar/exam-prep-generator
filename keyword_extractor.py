import spacy

def extract_keywords(text):
    try:
        nlp = spacy.load("en_core_web_sm")
    except:
        from spacy.cli import download
        download("en_core_web_sm")
        nlp = spacy.load("en_core_web_sm")

    doc = nlp(text)

    keywords = []

    for token in doc:
        if token.pos_ in ["NOUN", "PROPN"]:
            keywords.append(token.text)

    return list(set(keywords))
