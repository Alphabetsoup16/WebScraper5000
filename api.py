from fastapi import FastAPI
from starlette.responses import RedirectResponse
import uvicorn

app = FastAPI()


@app.get("/")
async def main():
    return RedirectResponse(url="/docs/")


if __name__ == '__main__':
    uvicorn.run("api:app", reload=True, port=8000, host='127.0.0.1')
