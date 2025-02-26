from django.db import models

class User(models.Model):
    spotify_id = models.CharField(max_length=50)
    spotify_user_id = models.CharField(max_length=50)
    display_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.display_name