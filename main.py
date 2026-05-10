from agent.agent import LearningAgent

agent = LearningAgent()

print("Learning Agent Started!")

while True:

    user_input = input("\nYou: ").lower().strip()

    if user_input == "exit":
        break

    elif user_input in ["like", "dislike"]:

        response = agent.learn_from_feedback(
            user_input
        )

    else:

        response = agent.recommend_movie(
            user_input
        )

    print(response)