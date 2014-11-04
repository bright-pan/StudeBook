#DJANGO
from django.db import models
#SB
from APP.models.UserModel import User

class UserFriend(models.Model):

    user_friend_id = models.AutoField(primary_key=True)
    requester = models.ForeignKey(User)
    recipient = models.ForeignKey(User)
    status = models.CharField(blank=True)
    since = models.DateTimeField(auto_now=True)

    @staticmethod
    def getUserFriendByUser (user) :
        return UserFriend.objects.filter(requester = user, status = 'accepted');

    def __str__(self) :
        return self.recipient.__str__();

    class Meta:
        managed = False
        db_table = 'sb_user_friend'
        