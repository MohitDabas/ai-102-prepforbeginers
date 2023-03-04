# azure sentiment analysis

import os
import requests
import json

# Add your subscription key and endpoint

subscription_key = "<key1>"
endpoint = "https://mdlangtext.cognitiveservices.azure.com"


# analysze sentiment
def sentiment_analysis(text):

    path = '/text/analytics/v3.0/sentiment'
    constructed_url = endpoint + path
    headers = {'Ocp-Apim-Subscription-Key': subscription_key}
    params = {'showStats': True}
    documents = {'documents': [
        {'id': '1', 'language': 'en', 'text': text}
    ]}

    response = requests.post(constructed_url, headers=headers, params=params, json=documents)
    sentiments = response.json()
    return sentiments

sentiment_positive_score=sentiment_analysis("I am very nervous")['documents'][0]['confidenceScores']['positive']
sentiment_negative_score=sentiment_analysis("I am very nervous")['documents'][0]['confidenceScores']['negative']

print(sentiment_positive_score,sentiment_negative_score)