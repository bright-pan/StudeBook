from APP.models.UserTypeModel import UserType

class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    email_address = models.CharField(max_length=80, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=100, blank=True)
    postalcode = models.CharField(max_length=12, blank=True)
    region = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    registration_date = models.DateTimeField(blank=True, null=True)
    user_type = models.ForeignKey(UserType, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sb_user'