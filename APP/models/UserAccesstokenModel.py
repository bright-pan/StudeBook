 #DJANGO
from django.db import models
#SB
from APP.models.UserModel import User

class UserAccessToken(models.Model):

    user = models.ForeignKey(User)
    access_token = models.TextField(max_length=100)

    class Meta:
        managed = False
        db_table = 'sb_user_access_token'
