intent_map = {
    "greeting": ["hello", "hi", "hey"],
    "farewell": ["bye", "see you", "bye"],
    "thanks": ["thanks", "thank you"],
    "weather": ["weather"],
    "time": ["time"],
    "define": ["define", "definition"]
}

responses = {
    "greeting": ["Hi!", "Hello!", "Nice to meet you!"],
    "farewell": ["Bye!", "Take care!", "See you soon!"],
    "thanks": ["You're welcome!", "No worries!", "Glad I could help!"],
    "weather": ["Got it. Which location should I check?", "Sure! Just let me know where to check.", "Which location are you curious about the weather in?"],
    "time": ["I'm on it, just tell me which location you're interested in.", "Just give me a location and I'm on it.", "Which location should I check the current time for?"],
    "define": ["Sure, what word do you need the definition of?", "Okay, what word do you need me to define?", "Alright, what word should I define?"]
}

def get_intent(user_input):
    user_input = user_input.lower()
    for intent, keywords in intent_map.items():
        for keyword in keywords:
            if keyword in user_input:
                return intent
    
    return None
