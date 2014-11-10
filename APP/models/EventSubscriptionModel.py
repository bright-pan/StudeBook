from django.db import models
from APP.models.UserModel import User
from APP.models.EventModel import Event

class EventSubscription(models.Model):

    event = models.ForeignKey(Event, blank=True, null=True)
    user = models.ForeignKey(User, blank=True, null=True)

    def __str__ (self) :
        return self.title

    class Meta:
        managed = False
        db_table = 'sb_event_subscription'