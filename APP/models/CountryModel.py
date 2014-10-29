#DJANGO
from django.db import models

class Country (models.Model) :
    
    country_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)

    class Meta:
        managed = False
        db_table = 'sb_country'