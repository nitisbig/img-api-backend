import requests
import base64
import json


api_key = 'AIzaSyAHdfm1hMGp5eO205B_lkkyIZYmHoGb5Fc'
url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-tts:generateContent'

headers = {
    "Content-Type": "application/json",
    "x-goog-api-key": api_key
}

payload ={
    "contents": [
        {
            "parts": [{"text": "Hello to nitesh for building api"}]
        }
    ],
    "generationConfig": {
        "responseModalities": ["AUDIO"],
        "speechConfig": {
            "voiceConfig": {
                "prebuiltVoiceConfig": {
                    "voiceName": "Kore"
                }
            }
        }
    }
}

response = requests.post(url, headers=headers, json=payload)
result = response.json()

audio_b64  = result["candidates"][0]["content"]["parts"][0]["inlineData"]["data"]
audio_bites = base64.b64decode(audio_b64)

out_file = 'my.pcm'

with open(out_file, 'wb') as f:
    f.write(audio_bites)