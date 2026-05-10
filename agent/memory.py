# agent/memory.py

class Memory:

    def __init__(self):

        self.last_recommendation = None

    def set_last_recommendation(self, movie_name):

        self.last_recommendation = movie_name

    def get_last_recommendation(self):

        return self.last_recommendation