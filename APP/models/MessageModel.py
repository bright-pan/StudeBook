#DJANGO
from django.db import models
#SB
from APP.models.UserModel import User

class Message(models.Model):

    id = models.AutoField(primary_key=True)
    creator = models.ForeignKey(User)
    recipient = models.ForeignKey(User)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.recipient.__str__();

    class Meta:
        managed = False
        db_table = 'sb_user_message'
        