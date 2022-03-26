import uvicorn
import os
from fastapi import FastAPI
from starlette.responses import FileResponse
from TEST_app import ExtractHyperLinksWithBaseAddress
from api_model import RequestInputModel
from TEST_app import GetConfigByElementNameValue, AttributeConstructor_Specific
from parser_class import StaticParser
from utilities.api_utilities import UseConfig
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


# @app.post(f"{api_url}/scrape")
# async def get_config(request: Request):
#     config = await request.json()
#     soup = GetMeTheSoup(config["url"])
#     response = {}
#     UseConfig(soup, config, response)
#     return response

@app.post("/scrape-links/")
async def ExtractHyperLinks(request: RequestInputModel):
    json_dict = request.dict()
    # Need to make this function more generic, remove "links"
    config_dict = GetConfigByElementNameValue(json_dict, "links")
    base_address = config_dict["base_address"]
    hyper_links = ExtractHyperLinksWithBaseAddress(json_dict, base_address)
    return hyper_links


@app.post("/scrape-classes/")
async def ExtractClassElements(request: RequestInputModel):
    json_dict = request.dict()

    class_attributes = AttributeConstructor_Specific(json_dict, "class")
    # Need to get url from config list, otherwise this is working well
    url = "https://realpython.github.io/fake-jobs/"
    # The idea with this is we will eventually only need to pass the config into Static parser
    # We wont need any of these function calls soon and the class will handle all of this
    target_class_data = StaticParser(
        url=url, attributes=class_attributes)

    element_list = target_class_data.GetElementByAttribute()

    element_dicts = target_class_data.ElementBuilder(element_list)

    grouped_results = target_class_data.ResultElementGrouper(element_dicts)

    results = target_class_data.ResultHandler(grouped_results)

    return results


if __name__ == '__main__':
    uvicorn.run("api:app", reload=True, port=port, host=host)
