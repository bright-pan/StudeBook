#DJANGO
from django.db import models
#SB
from APP.models.FileModel import File
from APP.models.UserModel import User

class FileDownload (models.Model) :
    
    file_download_id = models.AutoField(primary_key=True)
    file = models.ForeignKey(File)  
    user = models.ForeignKey(User)  
    date = models.DateTimeField(blank=True, null=True)

    @staticmethod
    def getNumberOfDownloads (file) :
    	return FileDownload.objects.filter(file=file).count();

    class Meta:
        managed = False
        db_table = 'sb_file_download'