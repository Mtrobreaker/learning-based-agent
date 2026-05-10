# agent/agent.py

from agent.movies import MOVIES
from agent.utility import UtilityCalculator
from agent.processor import (
    clean_input,
    extract_preferences
)

from agent.memory import Memory
from agent.learner import Learner


class LearningAgent:

    def __init__(self):

        self.utility = UtilityCalculator()
        self.memory = Memory()
        self.learner = Learner()

    def recommend_movie(self, user_input):

        cleaned = clean_input(user_input)

        preferences = extract_preferences(cleaned)

        if not preferences:
            return "I could not understand preferences."

        best_movie = None
        best_score = -1

        for movie in MOVIES:

            learning_score = (
                self.learner.get_learning_score(
                    movie["name"]
                )
            )

            score = self.utility.calculate_score(
                movie,
                preferences,
                learning_score
            )

            if score > best_score:

                best_score = score
                best_movie = movie

        self.memory.set_last_recommendation(
            best_movie["name"]
        )

        return (
            f"\n🎬 Recommended: {best_movie['name']}"
            f"\n⭐ Score: {best_score}"
        )

    def learn_from_feedback(self, feedback):

        movie = self.memory.get_last_recommendation()

        if not movie:
            return "No recommendation to learn from."

        if feedback == "like":

            self.learner.reward_movie(movie)

            return f"Learned that you like {movie} 👍"

        elif feedback == "dislike":

            self.learner.penalize_movie(movie)

            return f"Learned that you dislike {movie} 👎"

        return "Unknown feedback."