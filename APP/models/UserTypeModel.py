#DJANGO
from django.db import models
#SB

class UserType(models.Model):
    
    user_type_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'sb_user_type'