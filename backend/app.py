import os
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

current_dir = os.path.dirname(__file__)
client_dir = os.path.join(current_dir, "..", "client")

app.mount("/static", StaticFiles(directory=client_dir), name="static")

@app.get("/", response_class=FileResponse)
async def read_index():
    return FileResponse(os.path.join(client_dir, "index.html"), media_type="text/html")
