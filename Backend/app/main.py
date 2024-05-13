from fastapi import FastAPI


app = FastAPI(
    title='Crypto Currencies Scraper'
)


@app.get("/")
def main():
    return {"message": "OK"}
