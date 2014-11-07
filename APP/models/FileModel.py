#DJANGO
from django.db import models
#SB
from APP.models.UserModel import User
from APP.models.FileCategoryModel import FileCategory

class File(models.Model):
    file_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, blank=True, null=True)
    file_category = models.ForeignKey(FileCategory, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    upload_date = models.DateTimeField(blank=True, null=True)
    size = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    path = models.FileField()

    def __str__ (self) :
        return self.name

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        managed = False
        db_table = 'sb_file'