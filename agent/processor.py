# agent/processor.py

def clean_input(user_input: str) -> str:
    return user_input.lower().strip()


def extract_preferences(user_input: str):

    genres = [
        "action",
        "sci-fi",
        "romance",
        "drama",
        "thriller",
        "adventure"
    ]

    preferences = []

    for genre in genres:

        if genre in user_input:
            preferences.append(genre)

    return preferences