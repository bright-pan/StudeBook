#DJANGO
from django.db import models
#SB
from APP.models.UserModel import User

class Page(models.Model):

    page_id = models.AutoField(primary_key = True)
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, blank=True, null=True)
    body = models.TextField()
    publiced = models.IntegerField()
    created = models.DateTimeField()

    def __str__ (self) :
        return self.title

    def getPubliced (self) :
        if (self.publiced) :
            return 'Publiced'
        return 'Not publiced'


    class Meta:
        managed = False
        db_table = 'sb_page'

