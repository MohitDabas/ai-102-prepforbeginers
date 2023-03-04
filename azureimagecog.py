# azure cognitive services image analysis

import os
import requests
import json
import sys

# Add your Computer Vision subscription key and endpoint to your environment variables.
subscription_key = '9b877c7d11ec4bd49678080626b62785'
endpoint = 'https://mdcog.cognitiveservices.azure.com/'

analyze_url = endpoint + "vision/v2.1/analyze"

# Set image_url to the URL of an image that you want to analyze.

image_url = "https://www.washingtonpost.com/rf/image_1484w/2010-2019/WashingtonPost/2017/08/14/Others/Images/2017-08-10/AP_627055807091.JPG"

headers = {'Ocp-Apim-Subscription-Key': subscription_key}
params = {'visualFeatures': 'Categories,Description,Color'}
data = {'url': image_url}
response = requests.post(analyze_url, headers=headers,
                         params=params, json=data)
print(response.json())