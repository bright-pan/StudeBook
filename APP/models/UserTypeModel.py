class UserType(models.Model):
    user_type_id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'sb_user_type'