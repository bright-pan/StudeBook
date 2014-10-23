class UserLogin(models.Model):
    user_login_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(SbUser, blank=True, null=True)
    provider = models.CharField(max_length=45, blank=True)
    provider_id = models.CharField(max_length=150, blank=True)
    access_token = models.CharField(max_length=150, blank=True)

    class Meta:
        managed = False
        db_table = 'sb_user_login'