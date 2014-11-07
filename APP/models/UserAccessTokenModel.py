 #DJANGO
from django.db import models
#SB
from APP.models.UserModel import User

class UserAccessToken(models.Model):

    user = models.ForeignKey(User, primary_key = True)
    access_token = models.TextField(max_length = 40, unique = True)

    #Create Django model or update if exists
    def _save(self) :
        #Update
        try :
            _user = UserAccessToken.objects.get(user = self.user);
            _user.access_token = self.access_token;
            _user.save();
        #Create
        except :
            super(UserAccessToken, self).save()

    class Meta:
        managed = False
        db_table = 'sb_user_access_token'