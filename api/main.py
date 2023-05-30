# coding=utf-8

from fastapi import FastAPI

from router import router
from utils.config import load_env

load_env()

app = FastAPI()

# app.middleware('http')(auth_middleware)

app.include_router(router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
