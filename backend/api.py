from ninja import NinjaAPI
from backend.routers.spotify_router import router as spotify_router
from backend.routers.user_router import router as user_router

api = NinjaAPI()

api.add_router('/spotify', spotify_router)
api.add_router('/user', user_router)