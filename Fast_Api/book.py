from fastapi import FastAPI

app = FastAPI()


@app.get('/apis')
async def first_api(): # type: ignore
    return {"id": "123"}


@app.get('/api/{dynamic_param}')
async def first_api(dynamic_param):
    return {"dynamic_param": dynamic_param}