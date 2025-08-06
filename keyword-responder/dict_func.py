import requests

def get_definition(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)

    if response.status_code != 200:
        return f"Sorry, I couldn't get a definition for '{word}'."
    
    data = response.json()
    try:
        meaning = data[0]["meanings"][0]
        definition = meaning["definitions"][0]["definition"]
        part_of_speech = meaning["partOfSpeech"]
        
        return f"{word.title()} ({part_of_speech}): {definition}"
    
    except (IndexError, KeyError):
        return f"Definition not available for '{word}'."