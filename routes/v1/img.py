import uuid


from fastapi import APIRouter, Security
from fastapi.security.api_key import APIKeyBase
from lib.fetch_img import fetch_img
from pydantic import BaseModel
from lib.verify_api import verify

router = APIRouter(prefix="/v1", tags=['Img'])
unique_id = uuid.uuid4()

class PromptValidate(BaseModel):
    prompt: str
    size: str = '1024x1024'

@router.get('/')
def root(api_key: APIKeyBase = Security(verify)):
    return {'status': 'ok'}

@router.post('/img')
def get_img(p: PromptValidate, api_key: APIKeyBase = Security(verify)):
    b64img = fetch_img(p.prompt+f'size: {p.size}')
    data_uri = f"data:image/png;base64,{b64img}"
    data = {
        "data": {
            "id": unique_id,
            "imgUrl": data_uri,
        }
    }
    return data