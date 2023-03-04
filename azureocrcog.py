# azure cognitive service for OCR

import os
import requests
import json
import sys

# Add your Computer Vision subscription key and endpoint to your environment variables.


subscription_key = '<key1>'
endpoint = 'https://mdcog.cognitiveservices.azure.com/'

analyze_url = endpoint + "vision/v3.2/ocr"

# Set image_url to the URL of an image that you want to analyze.

image_url = "https://support.smartbear.com/testcomplete/docs/_images/testing-with/object-identification/ocr/ocr-test-script.png"

headers = {'Ocp-Apim-Subscription-Key': subscription_key}
params = {'language': 'unk', 'detectOrientation': 'true'}
data = {'url': image_url}
response = requests.post(analyze_url, headers=headers,
                            params=params, json=data)
print(response.json())