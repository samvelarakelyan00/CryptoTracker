# api key -> 5b5786c9-f031-4d0d-908c-3af7a40fd9ab

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from api import router


app = FastAPI(
    title='Crypto Currencies Scraper'
)


@app.get("/")
def main():
    return {"message": "OK"}


app.include_router(router)


origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)