#DJANGO
from django.db import models
#SB
from APP.models.UserModel import User
from APP.models.FileCategoryModel import FileCategory
from APP.forms.RestrictedFileField import RestrictedFileField

class File(models.Model):
    file_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, blank=True, null=True)
    file_category = models.ForeignKey(FileCategory, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    upload_date = models.DateTimeField(blank=True, null=True)
    size = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    path = RestrictedFileField(upload_to='uploads/', content_types=['application/msword', 'application/pdf', 'application/vnd.ms-excel', 'application/zip', 'audio/mpeg', 'image/bmp', 'image/gif', 'image/jpeg', 'image/tiff', 'text/plain', 'video/mpeg', 'video/x-msvideo', 'video/quicktime', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', 'application/vnd.openxmlformats-officedocument.spreadsheetml.template', 'application/vnd.openxmlformats-officedocument.presentationml.presentation', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'application/x-rar-compressed', 'application/octet-stream'],max_upload_size=20971520,blank=True, null=True)
    
    def __str__ (self) :
        return self.name

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        managed = False
        db_table = 'sb_file'