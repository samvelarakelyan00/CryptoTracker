from fastapi import APIRouter


from services import http_client
from core.config import settings


router = APIRouter(
    prefix='/cryptocurrencies',
    tags=['HTTP Client']
)


cmc_client = http_client.CMCHTTPClient(
    base_url="https://pro-api.coinmarketcap.com",
    api_key=settings.CMC_API_KEY
)


@router.get("")
async def get_cryptocurrencies():
    return await cmc_client.get_listings()


@router.get("/{currency_id}")
async def get_cryptocurrency(currency_id: int):
    return await cmc_client.get_currency(currency_id)
