from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
import uvicorn
from utilities import UseConfig

# later this should be a .env value or || 8000
PORT = 8000
# might need to change later for deployment
HOST = '127.0.0.1'
TITLE = 'Web Scraper of Doom'
API_URL = "/api/v1/"

app = FastAPI(
    title=TITLE,
    openapi_url=API_URL
)

app.mount("/static", StaticFiles(directory='static'))


@app.get("/")
async def serve_static():
    return FileResponse('static/index.html', media_type='text/html')


@app.get("/script.js")
async def load_js():
    return FileResponse('static/script.js')


@app.post(f"{API_URL}/scrape")
async def get_config(request: Request):
    config = await request.json()
    response = {}
    UseConfig(config, response)
    return response  # seems to return better without json.dumps


if __name__ == '__main__':
    uvicorn.run("api:app", reload=True, port=PORT, host=HOST)
