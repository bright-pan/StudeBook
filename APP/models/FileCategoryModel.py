#DJANGO
from django.db import models

class FileCategory(models.Model) :
    
    file_category_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=45, blank=True)
    file_price = models.IntegerField(blank=True, null=True)

    def __str__ (self) :
        return self.category

    class Meta:
        managed = False
        db_table = 'sb_file_category'