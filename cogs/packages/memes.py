import requests
import os
import json

# Meme Api
def get_meme():
    response = requests.get(os.getenv('MEME_API'))
    json_data = json.loads(response.text)
    if json_data['nsfw'] == True and json_data['spoiler'] == True:
        pass
    else:
        meme = json_data['url']
    return(meme)