from ninja import Router, Schema
from decouple import config
import requests
import base64

router = Router()


class AccessToken(Schema):
    access_token: str = ''

@router.get('/')
def getUserProfile(request, access_token: str = ''):
    currentUserEndpoint = 'https://api.spotify.com/v1/me'
    # print(data)
    if access_token:
        # post to spotify/api/token
        headers = {
            'Authorization': f'Bearer {access_token}',
        }
        res = requests.get(currentUserEndpoint, headers=headers)
        res_data = res.json()
        print(res_data)
        return {
            'message': 'GET current user profile SUCCESS',
            'spotify_id': res_data['id'],
            'profile_image_url': res_data['images'][0]['url'],
            'spotify_display_name': res_data['display_name'],
        }
    else:
        # return error
        return {'error': 'FAILED to grab current user profile: access token missing or invalid'}
