from ninja import Router
from backend.spotify.token_router import router as token_router

router = Router()

router.add_router('/token', token_router)