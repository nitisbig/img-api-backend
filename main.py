from fastapi import FastAPI
from routes import text_gen
from routes import img_gen
from routes import test_gen
from routes.v1 import img
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_methods = ['*'],
    allow_headers = ['*'],
    allow_origins = ['*']
)

app.include_router(text_gen.router)
app.include_router(img_gen.router)
app.include_router(test_gen.router)
app.include_router(img.router)
@app.get('/')
def root():
    return {'message': 'success'}
