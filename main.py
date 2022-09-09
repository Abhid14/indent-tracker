from typing import Union
from fastapi import FastAPI
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
import os
import subprocess


app = FastAPI()
app.add_middleware(HTTPSRedirectMiddleware)


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/reload")
async def reload():
    subprocess.Popen("git pull", stdout=subprocess.PIPE).communicate()
    return {"status": "success"}


@app.get("/dump")
async def dump():
    #os.system("DROP DATABASE databasename;")
    return {"status": "dump ok done"}


@app.get("/restart")
async def restart():
    os.system("sudo reboot")
    return {"status": "success"}
