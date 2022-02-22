from fastapi import FastAPI, Request
from starlette.responses import RedirectResponse
import uvicorn
from utilities import UseConfig
import json

app = FastAPI()


@app.get("/")
async def main():
    return RedirectResponse(url="/docs/")


@app.post("/scrape")
async def get_config(request: Request):
    config = await request.json()
    response = {}
    UseConfig(config, response)
    return response  # seems to return better without json.dumps


if __name__ == '__main__':
    uvicorn.run("api:app", reload=True, port=8000, host='127.0.0.1')
