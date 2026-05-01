def get_difficulty(question):
    
    length = len(question)

    if length < 50:
        return "Easy"

    elif length < 100:
        return "Medium"

    else:
        return "Hard"