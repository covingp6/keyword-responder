import random
from weather import get_weather
from responses import get_intent
from responses import responses


def chat():
    print("Bot: Hello! Ask me something. Type 'bye' to exit.")
    waiting_for_location = False 

    while True: 
        user_input = input("You: ").strip()

        if not user_input:
            continue

        if waiting_for_location:
            print("Bot:", get_weather(user_input))
            waiting_for_location = False
            continue

        intent = get_intent(user_input)

        if intent == "farewell":
            print("Bot:", random.choice(responses[intent]))
            break
        elif intent == "weather":
            print("Bot:", random.choice(responses[intent]))
            waiting_for_location = True
        elif intent in responses:
            print("Bot:", random.choice(responses[intent]))
        else:
            print("Bot: I didn't quite get that.")