import requests
from docx import Document
import os

subscription_key = "ChaEfI6Y6emNOrpTpLPdSWZhTjDeai8Rx9EdxJ3EuudaDL0n7636JQQJ99AKACHYHv6XJ3w3AAAbACOGM1ci"
endpoint = 'https://api.cognitive.microsofttranslator.com'
location = "eastus2"
target_language = 'pt-br'

def translator_text(text, target_language):
    path = '/translate'
    constructed_url = endpoint + path
    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTracedId': str(os.urandom(16))
    }

    body = [{
        'text': text
    }]
    params = {
        'api-version': 3.0,
        'from': 'en',
        'to': target_language
    }
    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()
    return response[0]["translations"][0]["text"]

