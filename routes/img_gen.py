
from fastapi import APIRouter, Security
from fastapi.security.api_key import APIKeyBase
from lib.fetch_img import fetch_img
from pydantic import BaseModel
from lib.verify_api import verify

router = APIRouter(prefix="/img", tags=['Img'])

class PromptValidate(BaseModel):
    prompt: str

@router.get('/')
def root(api_key: APIKeyBase = Security(verify)):
    return {'status': 'ok'}

@router.post('/')
def get_img(p: PromptValidate, api_key: APIKeyBase = Security(verify)):
    b64img = fetch_img(p.prompt)
    return b64img