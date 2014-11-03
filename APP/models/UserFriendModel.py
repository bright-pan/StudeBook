#DJANGO
from django.db import models
#SB
from APP.models.UserModel import User

class UserFriend(models.Model):
    id = models.AutoField(primary_key=True)
    requester = models.ForeignKey(User)
    recipient = models.ForeignKey(User)
    status = models.IntegerField(blank=True)
    since = models.DateTimeField(blank=True)

    class Meta:
        managed = False
        db_table = 'sb_user_friend'