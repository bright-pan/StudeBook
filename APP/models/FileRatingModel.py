#DJANGO
from django.db import models
from django.db.models import Avg
#SB
from APP.models.UserModel import User
from APP.models.FileModel import File

class FileRating(models.Model):
    file_rating_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, blank=True, null=True)
    file = models.ForeignKey(File, blank=True, null=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)


    @staticmethod
    def getAverage (file) :

        avgRatings = FileRating.objects.values('file').filter(file=file).annotate(avg=Avg('rating'))   
        for r in avgRatings:
            a = r

        try:
            a
        except NameError:
            avgRating = 0.0
        else:
            avgRating = round(a["avg"])
        
        return avgRating;



    @staticmethod
    def getNumberOfRatings (file) :

    	return FileRating.objects.filter(file=file).count();  

    @staticmethod
    def fileRatedByUser(file, user) :
    	rating = FileRating.objects.filter(file=file, user=user);

    	return rating.count() > 0;

    class Meta:
        managed = False
        db_table = 'sb_file_rating'