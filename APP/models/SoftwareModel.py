from django.db import models
from APP.models.UserModel import User


class Software(models.Model):

    software_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    name = models.CharField(max_length=200)
    description = models.TextField()
    url = models.CharField(max_length=200)
    date = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'sb_software'
