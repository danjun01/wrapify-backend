from ninja import Router, Schema
from backend.routers.token_router import router as token_router
from decouple import config
import base64
import requests

SPOTIFY_CLIENT_SECRET = config('SPOTIFY_CLIENT_SECRET')
SPOTIFY_CLIENT_ID = config('SPOTIFY_CLIENT_ID')

router = Router()

router.add_router('/token', token_router)

class UserData(Schema):
    user_id: str
    profile_image_url: str
    display_name: str

