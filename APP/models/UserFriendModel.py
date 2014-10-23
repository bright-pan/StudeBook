class UserFriend(models.Model):
    user = models.ForeignKey(SbUser)
    friend_id = models.IntegerField()
    accepted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sb_user_friend'