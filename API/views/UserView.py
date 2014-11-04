#DJANGO,PYTHON
import json
from django.http import HttpResponse
from django.views.generic import View
from django.core import serializers
#SB
from APP.views.MainView import MainView
from APP.models.UserModel import User
from APP.models.UserFriendModel import UserFriend

"""
 @class UserView
 @version 0.1
 @author M.Jansma
"""

class UserView (MainView):
    
    ###################################
    ########## Get user info ##########
    ###################################

    #TMP
    def userToDictionary (self, user) :
        return {
            'pk'         : user.user_id,
            'first_name' : user.first_name,
            'last_name'  : user.last_name,
            'full_name'  : user.getFullName()
        };

    #Get user info
    def getInfo (self, request) :
        if (super(UserView, self).isLoggedIn(request)) :
            userLogin = super(UserView, self).getUserLogin(request);
            response = self.userToDictionary(userLogin.user);
            return self.response({ 'status' : 200, 'user' : response });
        return self.response({ 'status' : 500, 'message' : 'User not logged in' });

    #Get user friends
    def getFriends (self, request) :
        if (super(UserView, self).isLoggedIn(request)) :
            userLogin = super(UserView, self).getUserLogin(request);
            userFriend = UserFriend.getUserFriendByUser(userLogin.user);
            response = [];
            for friend in userFriend :
                response.append(self.userToDictionary(friend.recipient));
            return self.response({ 'status' : 200, 'friendList' : response });
        return self.response({ 'status' : 500, 'message' : 'User not logged in' });

    #Response 
    def response (self, data) :
        return HttpResponse(json.dumps(data), content_type = 'application/json');
    
    