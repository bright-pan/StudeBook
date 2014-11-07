#DJANGO
from django.db import models
#SB
from APP.models.UserTypeModel import UserType

class User (models.Model) :
    
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    email_address = models.CharField(max_length=80, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=150, blank=True)
    houseno = models.CharField(max_length=5, null=True, blank=True)
    city = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=12, blank=True)
    region = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    registration_date = models.DateTimeField(blank=True, null=True)
    user_type = models.ForeignKey(UserType, blank=True, null=True)    
    credits = models.IntegerField(blank=True, null=True)

    def getFullName (self) :
        return self.first_name + ' ' + self.last_name;

    def __str__ (self) :
        return self.getFullName();

    class Meta:
        managed = False
        db_table = 'sb_user'