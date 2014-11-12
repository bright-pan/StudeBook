#DJANGO
from django.db import models

class Update(models.Model):

    update_id = models.AutoField(primary_key = True)
    date = models.DateField(blank=True, null=True)
    table_name = models.CharField(max_length=40)
    row_id = models.IntegerField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'sb_update'

