from ninja import NinjaAPI
from backend.spotify.spotify_router import router as spotify_router
api = NinjaAPI()

api.add_router('/spotify', spotify_router)