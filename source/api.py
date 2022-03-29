import uvicorn
import os
from fastapi import FastAPI
from starlette.responses import FileResponse
from api_model import RequestInputModel
from parser_class import StaticParser
from BETA_app import AttributeConstructor_Specific, ExtractHyperLinksWithBaseAddress, GetConfigByElementNameValue
from dotenv import load_dotenv

load_dotenv()

api_url = os.getenv('API_URL')
port = int(os.getenv('PORT'))
host = os.getenv('HOST')

app = FastAPI(
    title='Web Scraper of Doom'
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


@app.post("/scrape-links/")
async def ExtractHyperLinks(request: RequestInputModel):
    json_dict = request.dict()
    config_dict = GetConfigByElementNameValue(json_dict, "links")
    base_address = config_dict["base_address"]
    hyper_links = ExtractHyperLinksWithBaseAddress(json_dict, base_address)
    return hyper_links


@app.post("/scrape-classes/")
async def ExtractClassElements(request: RequestInputModel):
    json_dict = request.dict()

    class_attributes = AttributeConstructor_Specific(json_dict, "class")

    # TODO: The idea with this is we will eventually only need to pass the config into Static parser
    class_data = StaticParser(config=json_dict, attributes=class_attributes)

    return class_data.ResultHandler()


if __name__ == '__main__':
    uvicorn.run("api:app", reload=True, port=port, host=host)
