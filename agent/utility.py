# agent/utility.py

class UtilityCalculator:

    def calculate_score(
        self,
        movie,
        preferences,
        learning_score
    ):

        score = 0

        for genre in preferences:

            if genre in movie["genres"]:
                score += 10

        score += movie["rating"] * 2

        # 🔥 learning bonus
        score += learning_score

        return score