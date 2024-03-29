#DJANGO
from django.db import models
#SB
from APP.models.UserModel import User

class Notification(models.Model) :
    
    notification_id = models.AutoField(primary_key=True);
    requester = models.ForeignKey(User);
    recipient = models.ForeignKey(User);
    notification = models.TextField(max_length=150);
    datetime = models.DateTimeField(null=True,blank=True);
    read = models.SmallIntegerField(max_length=1,null=True,blank=True,default=0);
    category = models.CharField(max_length=50);
    goto_url = models.CharField(max_length=100);

    def getRead (self) :
        return 'unread' if self.read == 0 else 'read';

    def __str__ (self) :
        return self.notification;

    class Meta :
        managed = False
        db_table = 'sb_notification'

