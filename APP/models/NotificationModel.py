#DJANGO
from django.db import models
#SB
from APP.models.UserModel import User

class Notification(models.Model) :
    
    notification_id = models.AutoField(primary_key=True);
    requester = models.ForeignKey(User);
    recipient = models.ForeignKey(User);
    notification = models.TextField(max_length=250);
    datetime = models.DateTimeField();
    read = models.SmallIntegerField(max_length=1);

    class Meta :
        managed = False
        db_table = 'sb_notification'

