from ninja import Router, Schema
from decouple import config
from backend.models import User

router = Router()


class UserIn(Schema):
    access_token: str = ''
    

class UserOut(Schema):
    id: int
    display_name: str = ''
    spotify_id: str = ''
    profile_image_url: str = ''

@router.post('/', response=UserOut)
def create_user(request, data: UserIn):
    user = User()
    user.set_spotify_id(data.spotify_id)
    user.save()