import requests

api_key = 'AIzaSyAHdfm1hMGp5eO205B_lkkyIZYmHoGb5Fc'
url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-image:generateContent'



def fetch_img(prompt: str):
    headers = {
    'Content-Type': 'application/json',
    'x-goog-api-key': api_key,
    }
    payload =  {
    "contents": [
        {"parts": [{"text": prompt}]}
    ]
    }
    response = requests.post(url, headers=headers, json=payload)
    results = response.json()
    
    img_b64 = None

    for part in results["candidates"][0]["content"]["parts"]:
        if "inlineData" in part:
            img_b64 = part['inlineData']['data']
            break

    return img_b64
