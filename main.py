

from fastapi import FastAPI
from routes import text_gen
from routes import img_gen

app = FastAPI()

app.include_router(text_gen.router)
app.include_router(img_gen.router)

@app.get('/')
def root():
    return {'message': True}
