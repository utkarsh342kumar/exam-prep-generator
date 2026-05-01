import random
import re
from keyword_extractor import extract_keywords
from difficulty import get_difficulty


def clean_sentences(text):
    # Better sentence splitting
    sentences = re.split(r'(?<=[.!?]) +', text)
    return [s.strip() for s in sentences if len(s.split()) > 5]


def generate_options(correct, keywords):
    distractors = list(set(keywords) - {correct})

    # Pick 3 distractors if possible
    if len(distractors) >= 3:
        options = random.sample(distractors, 3)
    else:
        options = distractors

    options.append(correct)
    random.shuffle(options)

    return options


def create_fill_blank(sentence, keyword):
    # Replace only exact word
    pattern = r'\b' + re.escape(keyword) + r'\b'
    return re.sub(pattern, "_____", sentence, count=1)


def generate_mcqs(text, num_questions=5):
    keywords = extract_keywords(text)
    sentences = clean_sentences(text)

    mcqs = []

    for sentence in sentences:
        for keyword in keywords:

            # ✅ Removed sentence restriction (important fix)
            if keyword.lower() in sentence.lower():

                question = create_fill_blank(sentence, keyword)

                if "_____" not in question:
                    continue

                options = generate_options(keyword, keywords)

                mcqs.append({
                    "question": question,
                    "options": options,
                    "answer": keyword,
                    "difficulty": get_difficulty(question)
                })

                # Stop when required number reached
                if len(mcqs) >= num_questions:
                    return mcqs

    return mcqs