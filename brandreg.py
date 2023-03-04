# azure cognitive service for brand recognition

import os
import requests
import json
import sys

# Add your Computer Vision subscription key and endpoint to your environment variables.

subscription_key = '<key1>'
endpoint = 'https://mdcog.cognitiveservices.azure.com/'

analyze_url = endpoint + "vision/v3.2/analyze?visualFeatures=Brands"

# Set image_url to the URL of an image that you want to analyze.

image_url = "https://resize.indiatvnews.com/en/resize/newbucket/715_-/2018/04/pjimage-3-1524555823.jpg"

headers = {'Ocp-Apim-Subscription-Key': subscription_key}

data = {'url': image_url}

response = requests.post(analyze_url, headers=headers, json=data)

print(response.json())
