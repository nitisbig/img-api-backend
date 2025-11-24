
from fastapi import APIRouter,Security, HTTPException, Depends
from fastapi.security.api_key import APIKeyBase, APIKeyHeader
from lib.fetch_img import fetch_img
from pydantic import BaseModel
from starlette.status import HTTP_401_UNAUTHORIZED

my_api = 'myapi'

router = APIRouter(prefix="/img", tags=['Img'])

def verify_api(api_key_header: str = Security(APIKeyHeader(name='x-api-key', auto_error=False))):
    if api_key_header == my_api:
        return api_key_header
    raise HTTPException(
        status_code= HTTP_401_UNAUTHORIZED,
        detail='invalid api key'
    )

class PromptValidate(BaseModel):
    prompt: str

@router.get('/')
def root():
    return {'status': 'ok'}

@router.post('/')
def get_img(p: PromptValidate, api_key: APIKeyBase = Depends(verify_api)):
    b64img = fetch_img(p.prompt)
    return b64img