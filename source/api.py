import uvicorn
import os
from fastapi import FastAPI, Request
from starlette.responses import FileResponse
from utilities.api_utilities import UseConfig
from utilities.general_utilities import GetMeTheSoup
from dotenv import load_dotenv

load_dotenv()

api_url = os.getenv('API_URL')
port = int(os.getenv('PORT'))
host = os.getenv('HOST')

app = FastAPI(
    title='Web Scraper of Doom',
    openapi_url=api_url
)

#app.mount("/static", StaticFiles(directory='static'))


@app.get("/")
async def serve_static():
    return FileResponse('static/index.html', media_type='text/html')


@app.get("/styles.css")
async def load_css():
    return FileResponse('static/styles.css')


@app.get("/script.js")
async def load_js():
    return FileResponse('static/script.js')


@app.post(f"{api_url}/scrape")
async def get_config(request: Request):
    config = await request.json()
    soup = GetMeTheSoup(config["url"])
    response = {}
    UseConfig(soup, config, response)
    return response

if __name__ == '__main__':
    uvicorn.run("api:app", reload=True, port=port, host=host)
