#DJANGO,PYTHON
import json
from django.http import HttpResponse
from django.views.generic import View
#SB
from APP.models.UserFriendModel import UserFriend
from APP.models.UserAccessTokenModel import UserAccessToken
from APP.models.UserModel import User
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

    #Get notification info
    def getInfo (self, request, accessToken) :
        #TMP
        return self.response({ 'bla' : 202 });

    #Get count notifications
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

    #Create notification
    def create (self, request, accessToken) :
        try :
            #Get user by access token
            requester = UserAccessToken.objects.get(access_token = accessToken).user;
            recipient = User.objects.get(user_id = request.POST['recipient_id']);
            #Create notification
            Notification(
                requester    = requester,
                recipient    = recipient,
                notification = request.POST['notification'],
                category     = request.POST['category']
            ).save();
            #Response
            return self.response({
                'status'  : 200,
                'message' : 'Notification created'
            });
        except :
            return self.response({ 'status' : 500, 'message' : 'Bad request' });

    #Response 
    def response (self, data) :
        return HttpResponse(json.dumps(data), content_type = 'application/json');
    
    