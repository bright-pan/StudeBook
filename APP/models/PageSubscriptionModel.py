from django.db import models
from APP.models.UserModel import User
from APP.models.PageModel import Page

class PageSubscription(models.Model):

    page = models.ForeignKey(Page, blank=True, null=True)
    user = models.ForeignKey(User, blank=True, null=True)

    def __str__ (self) :
        return self.title

    class Meta:
        managed = False
        db_table = 'sb_page_subscription'