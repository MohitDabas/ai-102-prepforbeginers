import os
import requests
import json

# Add your subscription key and endpoint
subscription_key = "<key1>"
endpoint = "https://mdlangtext.cognitiveservices.azure.com"


#detect language

def language_detect(text):
    
        path = '/text/analytics/v3.0/languages'
        constructed_url = endpoint + path
        headers = {'Ocp-Apim-Subscription-Key': subscription_key}
        params = {'showStats': True}
        documents = {'documents': [
            {'id': '1', 'text': text}
        ]}
    
        response = requests.post(constructed_url, headers=headers, params=params, json=documents)
        languages = response.json()
        return languages

print(language_detect('אני מוהיט'))


