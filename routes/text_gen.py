
from fastapi import APIRouter
from pydantic import BaseModel

import requests

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"
api_key = "AIzaSyAHdfm1hMGp5eO205B_lkkyIZYmHoGb5Fc"


router = APIRouter(prefix='/text', tags=['Text'])

class TextSchema(BaseModel):
    text: str

def generate_text(text: str):    
    headers = {
        'Content-Type': 'application/json',
        'x-goog-api-key': api_key,
    }
    data = {
        "contents": [
            {"parts": [{"text": text}]}
        ]
    }
    res =requests.post(url, headers=headers, json=data)
    return res.json()


@router.get('/')
def root():
    return {'status': 'ok'}

@router.post('/')
def gen_text(res: TextSchema):
    response = generate_text(res.text)
    return response