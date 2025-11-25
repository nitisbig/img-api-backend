import os
from fastapi import APIRouter, Security, HTTPException, Depends
from fastapi.security.api_key import APIKeyBase,APIKeyHeader
from starlette.status import HTTP_401_UNAUTHORIZED
from pydantic import BaseModel
from dotenv import load_dotenv
load_dotenv()

import requests

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"
api_key = os.getenv('api_key')
my_api = "myapi"

router = APIRouter(prefix='/text', tags=['Text'])

def verify_api(api_key_header: str = Security(APIKeyHeader(name='x-api-key', auto_error=False))):
    if api_key_header == my_api:
        return api_key_header
    raise HTTPException(
        status_code= HTTP_401_UNAUTHORIZED,
        detail='invalid api key'
    )

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
def gen_text(res: TextSchema, api: APIKeyBase = Depends(verify_api)):
    response = generate_text(res.text)
    return response