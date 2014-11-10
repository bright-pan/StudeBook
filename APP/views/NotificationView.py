#Django
from django.http import HttpResponse
from django.core import serializers
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

#SB
from APP.views.MainView import MainView

import json
import array

"""
 @class ProfileView
 @version 0.1
 @author StudeBook inc.
"""

class NotificationView(MainView):
    def show (self, request) :
        userLogin = super(NotificationView, self).getUserLogin(request)
       
        return super(NotificationView, self).render(request, 'notification/notification.html', {
        });
        
    def getNotification (self, request) :
        
        data = json.dumps({ 'status' : 200 });
        return HttpResponse(data,content_type='application/json');