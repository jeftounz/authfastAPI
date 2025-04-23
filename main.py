from typing import Union

from fastapi import FastAPI,Request
from starlette.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

templates=Jinja2Templates(directory="templates")

app=FastAPI()
app.mount("/static",StaticFiles(directory="static",html=True),name="static")

@app.get("/")
def home(request: Request):#tengo este error: Request" is not defined
    return templates.TemplateResponse("index.html",{"request": request})

@app.get("/about")
def home(request: Request):
    return templates.TemplateResponse("about.html",{"request":request})

@app.get("/user/signin")
def login(req:Request):
    return templates.TemplateResponse("/signin.html",{"request":req})

@app.get("/user/signup")
def login(req:Request):
    return templates.TemplateResponse("/signup.html",{"request":req})