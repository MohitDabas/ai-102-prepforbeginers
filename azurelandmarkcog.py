# azure cognitive service for landmark recognition

import os
import requests
import json
import sys

# Add your Computer Vision subscription key and endpoint to your environment variables.

subscription_key = '<key1>'
endpoint = 'https://mdcog.cognitiveservices.azure.com/'

analyze_url = endpoint + "vision/v3.2/analyze?details=Landmarks"

# Set image_url to the URL of an image that you want to analyze.

image_url = "https://mohitdabas.files.wordpress.com/2022/04/277230822_5259876407402548_3369352471359067352_n.jpg"

headers = {'Ocp-Apim-Subscription-Key': subscription_key}

data = {'url': image_url}

response = requests.post(analyze_url, headers=headers, json=data)

print(response.json())
