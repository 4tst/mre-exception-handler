import logging

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from src.sub_app import sub_app_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    max_age=600,
)

log = logging.getLogger("app")

app.include_router(sub_app_router)


@app.exception_handler(Exception)
async def exception_handler(request: Request, ex: Exception):
    log.error("Unhandled exception: %s", ex)
    return JSONResponse(content=dict(success=False))


@app.exception_handler(AssertionError)
# @app.exception_handler(ValueError)
async def exception_handler(request: Request, ex: Exception):
    log.error("Unhandled exception: %s", ex)
    return JSONResponse(content=dict(success=False))


@app.post("/queryAppConfig")
async def query_app_config():
    assert True == False


if __name__ == "__main__":
    uvicorn.run("server:app", port=8083, reload=True, workers=6)
