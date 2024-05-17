# api key -> 5b5786c9-f031-4d0d-908c-3af7a40fd9ab

from fastapi import FastAPI


from api import router


app = FastAPI(
    title='Crypto Currencies Scraper'
)


@app.get("/")
def main():
    return {"message": "OK"}


app.include_router(router)
