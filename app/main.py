from fastapi import FastAPI
from .routers import bands, songs

app = FastAPI()

app.include_router(songs.router)
app.include_router(bands.router)