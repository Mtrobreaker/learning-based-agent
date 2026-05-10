# agent/learner.py

import json
import os


class Learner:

    def __init__(self):

        self.file_path = "data/learning.json"

        if not os.path.exists(self.file_path):

            with open(self.file_path, "w") as file:
                json.dump({}, file)

    def load_learning_data(self):

        with open(self.file_path, "r") as file:
            return json.load(file)

    def save_learning_data(self, data):

        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)

    def reward_movie(self, movie_name):

        data = self.load_learning_data()

        data[movie_name] = data.get(movie_name, 0) + 5

        self.save_learning_data(data)

    def penalize_movie(self, movie_name):

        data = self.load_learning_data()

        data[movie_name] = data.get(movie_name, 0) - 5

        self.save_learning_data(data)

    def get_learning_score(self, movie_name):

        data = self.load_learning_data()

        return data.get(movie_name, 0)