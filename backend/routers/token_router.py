from ninja import Router, Schema
from decouple import config
import requests
import base64

SPOTIFY_CLIENT_SECRET = config('SPOTIFY_CLIENT_SECRET')
SPOTIFY_CLIENT_ID = config('SPOTIFY_CLIENT_ID')
TOKEN_URL = 'https://accounts.spotify.com/api/token'
REDIRECT_URI = 'http://localhost:5173/auth/callback'

router = Router()

class RefreshToken(Schema):
    refresh_token: str = ''
    
class AuthCode(Schema):
    code: str = ''

@router.post('/refresh')
async def refresh_access_token(request, data: RefreshToken):
    if data.refresh_token:
        # post to spotify/api/token
        payload = {
            'grant_type': 'refresh_token',
            'refresh_token': data.refresh_token,
        }
        headers = {
            'Authorization': 'Basic ' + base64.b64encode(f'{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}'.encode('utf-8')).decode(),
            'content-type': 'application/x-www-form-urlencoded',
        }
        # print(payload)
        # print(headers)
        res = requests.post(TOKEN_URL, data=payload, headers=headers)
        res_data = res.json()
        # print(res_data)
        return {
            'message': 'access token refreshed',
            'access_token': res_data['access_token'],
            'refresh_token': res_data['refresh_token']
        }
    else:
        # return error
        return {'error': 'access token could not be refreshed'}


@router.post('/')
async def get_access_token(request, data: AuthCode):
    # print(data)
    if data.code:
        # post to spotify/api/token
        payload = {
            'grant_type': 'authorization_code',
            'code': data.code,
            'redirect_uri': REDIRECT_URI,
            'scope': 'user-top-read',
        }
        headers = {
            'Authorization': 'Basic ' + base64.b64encode(f'{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}'.encode('utf-8')).decode(),
            'content-type': 'application/x-www-form-urlencoded',
        }
        # print(payload)
        # print(headers)
        res = requests.post(TOKEN_URL, data=payload, headers=headers)
        res_data = res.json()
        # print(res_data)
        return {
            'message': 'access token granted',
            'access_token': res_data['access_token'],
            'refresh_token': res_data['refresh_token']
        }
    else:
        # return error
        return {'error': 'auth code invalid'}
