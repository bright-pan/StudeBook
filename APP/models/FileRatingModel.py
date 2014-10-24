#DJANGO
from django.db import models
#SB
from APP.models.UserModel import User
from APP.models.FileModel import File

class FileRating(models.Model):
    file_rating_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, blank=True, null=True)
    file = models.ForeignKey(File, blank=True, null=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sb_file_rating'