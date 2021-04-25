import requests
import os
import json

# Quotes Api
def get_quote():
    response = requests.get(os.getenv('QUOTE_API'))
    json_data = json.loads(response.text)
    quote = f'''{json_data[0]['q']}
~{json_data[0]['a']}'''
    return(quote)