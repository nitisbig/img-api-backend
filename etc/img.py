import requests
import base64
import json


api_key = 'AIzaSyAHdfm1hMGp5eO205B_lkkyIZYmHoGb5Fc'
url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-image:generateContent'


headers = {
    'Content-Type': 'application/json',
    'x-goog-api-key': api_key,
}

payload =  {
    "contents": [
        {"parts": [{"text": "1886 train passing between bridge"}]}
    ]
}

response = requests.post(url, headers=headers, json=payload)
result = response.json()

img_base64 = None

if img_base64 is None:
    try:
        img_base64 = result["candidates"][0]["content"]["parts"][1]["inlineData"]["data"]
    except KeyError:
        pass
if img_base64 is None:
    try:
        img_base64 = result["candidates"][0]["content"]["parts"][0]["inlineData"]["data"]
    except KeyError:
        pass

img_bytes = base64.b64decode(img_base64)
out_file = 'train.png'
with open(out_file, 'wb') as f:
    f.write(img_bytes)


