import requests
import urllib.parse

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '418ba71ce3c44ffeb51fe503fec179ce',
}

params = urllib.parse.urlencode({
    # Request parameters
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender',
    'recognitionModel': 'recognition_04',
    'returnRecognitionModel': 'false',
    'detectionModel': 'detection_03',
    'faceIdTimeToLive': '86400',
})


# Replace the example URL below with the URL of the image you want to analyze.
body = "{'url':'https://upload.wikimedia.org/wikipedia/commons/3/37/Dagestani_man_and_woman.jpg'}"

response=requests.post('https://mdfaceapi.cognitiveservices.azure.com/face/v1.0/detect?%s' % params, headers=headers, data=body)
response.raise_for_status()

print(response.json())  