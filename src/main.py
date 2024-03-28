from fastapi.responses import HTMLResponse, JSONResponse
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI


app = FastAPI(debug=True)
app.mount("/assets", StaticFiles(directory="src/assets"))
templates = Jinja2Templates(directory="src/templates")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.jinja2"
    )


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
