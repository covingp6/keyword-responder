intent_map = {
    "greeting": ["hello", "hi", "hey"],
    "farewell": ["bye", "see you", "bye"],
    "thanks": ["thanks", "thank you"],
    "weather": ["weather"],
}

responses = {
    "greeting": ["Hi!", "Hello!", "Nice to meet you!"],
    "farewell": ["Bye!", "Take care!", "See you soon!"],
    "thanks": ["You're welcome!", "No worries!", "Glad I could help!"],
    "weather": ["What location would you like the weather for?"]
}

def get_intent(user_input):
    user_input = user_input.lower()
    for intent, keywords in intent_map.items():
        for keyword in keywords:
            if keyword in user_input:
                return intent
    
    return None