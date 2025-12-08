import uuid
import base64


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


    file_name = f"{uuid.uuid4()}.png"
    file_path = f"static/{file_name}"

    with open(file_path, "wb") as fh:
        fh.write(base64.b64decode(b64img))
    
    server_url = "http://127.0.0.1:8000" 
    full_img_url = f"{server_url}/images/{file_name}"
    data = {
        "data": {
            "id": str(unique_id),
            "imgUrl": full_img_url,
        }
    }
    return data