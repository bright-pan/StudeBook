#DJANGO,PYTHON
import json
from django.http import HttpResponse
from django.views.generic import View
from django.db.models.loading import get_model

#SB
from APP.models.UpdateModel import Update
from APP.models.UserAccessTokenModel import UserAccessToken

"""
 @class UpdateView
 @version 0.1
 @author J. Plat
"""

class UpdateView (View):

    #Get updates
    def getUpdates (self, request) :
        try :
            #Get user by access token
            updates = Update.objects.all().order_by('-date');
            updateList = [];
            #Manipulate userFriend data
            for update in updates :
                type = update.table_name[3:];
                link = "/" + type + "/read/" + str(update.row_id);
                content = update.user.getFullName() + " added a " + type + ": " + update.title;

                updateList.append({'link' : link, 'content' : content});
            #Response
            return self.response({
                'status' : 200, 'data' : { 'updateList' : updateList }
            });
        except :
            return self.response({ 'status' : 500, 'message' : 'Bad request' });

    #Response 
    def response (self, data) :
        return HttpResponse(json.dumps(data), content_type = 'application/json');
    
    