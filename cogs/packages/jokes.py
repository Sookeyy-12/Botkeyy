import requests
import os
import json

# Joke Api
def get_joke():
    response = requests.get(os.getenv('JOKE_API'))
    json_data = json.loads(response.text)
    if json_data['type'] == "single":
        joke = json_data['joke']
    else:
        joke = json_data['setup'] + " " + json_data['delivery']
    return(joke)