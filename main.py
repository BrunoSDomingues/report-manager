from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse
import random

app = FastAPI()


@app.get("/rand")
async def rand():
    return random.randint(0, 100)
