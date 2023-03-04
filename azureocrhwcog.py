import requests 
 
# Replace with your own subscription key and endpoint 
subscription_key = '9b877c7d11ec4bd49678080626b62785'
endpoint = 'https://mdcog.cognitiveservices.azure.com/'
 
# Set the API URL 
url = endpoint + 'vision/v3.1/read/analyze' 
 
# Set the image URL 
image_url = 'https://raw.githubusercontent.com/MicrosoftDocs/azure-docs/master/articles/cognitive-services/Computer-vision/Images/readsample.jpg' 
 
# Set the request headers and body 
headers = { 
    'Ocp-Apim-Subscription-Key': subscription_key, 
    'Content-Type': 'application/json' 
} 
body = { 
    'url': image_url 
} 
 
# Send the API request and get the response 
response = requests.post(url, headers=headers, json=body) 
response.raise_for_status() 
 
# Get the operation ID from the response headers 
operation_url = response.headers['Operation-Location'] 

 
# Poll the operation status until it is completed 
status_url = operation_url + '/status' 
while True: 
    status_response = requests.get(operation_url, headers=headers) 
    print(status_response.json())
    status_response.raise_for_status() 
    status = status_response.json()['status'] 
    if status == 'succeeded': 
        break 
 
