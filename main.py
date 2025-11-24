

from fastapi import FastAPI, Depends, Security, HTTPException
from routes import text_gen
from routes import img_gen
from fastapi.security.api_key import APIKeyHeader, APIKeyBase
from starlette.status import HTTP_401_UNAUTHORIZED


app = FastAPI()

api_key = 'thisiskey'

def get_api_key(api_key_header: str = Security(APIKeyHeader(name='x-api-key', auto_error=False))):
    if api_key_header == api_key:
        return api_key_header
    raise HTTPException(
        status_code= HTTP_401_UNAUTHORIZED,
        detail='Invalid or missing api key'
    )


app.include_router(text_gen.router)
app.include_router(img_gen.router)

@app.get('/')
def root():
    return {'message': True}

@app.get('/protected')
def secret(api: APIKeyBase = Depends(get_api_key)):
    return {'access': 'allowed'}
