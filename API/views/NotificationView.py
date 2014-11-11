#DJANGO,PYTHON
import json
from django.http import HttpResponse
from django.views.generic import View
#SB
from APP.models.UserFriendModel import UserFriend
from APP.models.UserAccessTokenModel import UserAccessToken
from APP.models.NotificationModel import Notification

"""
 @class NotificationView
 @version 0.1
 @author M.Jansma
"""

class NotificationView (View):
    
    ###################################
    ###### Get notification info ######
    ###################################

    def getInfo (self, request, accessToken) :
        #saddsadsa
        return self.response({ 'bla' : 202 });

    def getCount (self, request, accessToken) :
        try :
            #Get user by access token
            user = UserAccessToken.objects.get(access_token = accessToken).user;
            #Response
            return self.response({
                'status' : 200,
                'data'   : {
                    'total'  : len(Notification.objects.filter(recipient = user)),
                    'unread' : len(Notification.objects.filter(recipient = user, read = 0))
                }
            });
        except :
            return self.response({ 'status' : 500, 'message' : 'Bad request' });

    #Cast <UserModel> instance to dictionary
    def userToDictionary (self, user) :
        return {
            'pk'         : user.user_id,
            'first_name' : user.first_name,
            'last_name'  : user.last_name,
            'full_name'  : user.getFullName()
        };

    #Get user info
    def getInfo (self, request, accessToken) :
        try :
            #Get user by access token
            user = UserAccessToken.objects.get(access_token = accessToken).user;
            return self.response({
                'status' : 200,
                'data'   : {
                    'user' : self.userToDictionary(user)
                }
            });
        except :
            return self.response({ 'status' : 500, 'message' : 'Bad request' });

    #Get user friends
    def getFriends (self, request, accessToken) :
        try :
            #Get user by access token
            user = UserAccessToken.objects.get(access_token = accessToken).user;
            userFriend = UserFriend.getUserFriendByUser(user);
            friendList = [];
            #Manipulate userFriend data
            for friend in userFriend :
                friendList.append(self.userToDictionary(friend.recipient));
            #Response
            return self.response({
                'status' : 200, 'data' : { 'friendList' : friendList }
            });
        except :
            return self.response({ 'status' : 500, 'message' : 'Bad request' });

    #Response 
    def response (self, data) :
        return HttpResponse(json.dumps(data), content_type = 'application/json');
    
    