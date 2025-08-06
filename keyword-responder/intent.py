import random
from weather_func import get_weather
from time_func import get_time
from responses import get_intent
from responses import responses
from dict_func import get_definition



def chat():
    print("Bot: Hello! Ask me something. Type 'bye' to exit.")
    waiting_for_response = False 
    waiting_intent = None 
    
    while True: 
        user_input = input("You: ").strip()

        if not user_input:
            continue
        
        if waiting_for_response:
            if waiting_intent == "weather":
                print("Bot:", get_weather(user_input))
                waiting_for_response = False
                waiting_intent = None
                continue
            elif waiting_intent == "time":
                print("Bot:", get_time(user_input))
                waiting_for_response = False
                waiting_intent = None
                continue
            elif waiting_intent == "define":
                print("Bot:", get_definition(user_input))
                waiting_for_response = False
                waiting_intent = None
                continue

        intent = get_intent(user_input)

        if intent == "farewell":
            print("Bot:", random.choice(responses[intent]))
            break
        elif intent in ["weather", "time", "define"]:
            print("Bot:", random.choice(responses[intent]))
            waiting_for_response = True
            waiting_intent = intent  
        elif intent in responses:
            print("Bot:", random.choice(responses[intent]))
        else:
            print("Bot: I didn't quite get that.")
