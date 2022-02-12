from fastapi import FastAPI
from mangum import Mangum



app = FastAPI(title='Cryptocurrency API',
              description='API to track current prices and trading signals')


@app.get("/")
def read_root():
    return {"message": "from FastAPI & API Gateway"}


# to make it work with Amazon Lambda, we create a handler object
handler = Mangum(app=app)