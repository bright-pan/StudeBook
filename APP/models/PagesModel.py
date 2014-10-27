#DJANGO
from django.db import models
#SB
from APP.models.UserModel import User

class Page(models.Model):

    user_page_id = models.AutoField(primary_key = True)
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, blank=True, null=True)
    body = models.TextField()
    created = models.DateTimeField()

    def __str__ (self) :
        return self.title

    class Meta:
        managed = False
        db_table = 'sb_user_pages'