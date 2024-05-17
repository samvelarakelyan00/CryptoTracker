from fastapi import APIRouter

from .endpoints.http_client import router as http_client_router


router = APIRouter()


router.include_router(http_client_router)
