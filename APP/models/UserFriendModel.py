from APP.models.UserModel import User

class UserFriend(models.Model):
    user = models.ForeignKey(User)
    friend_id = models.IntegerField()
    accepted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sb_user_friend'