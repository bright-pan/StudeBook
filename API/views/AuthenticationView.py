#PYTHON
import json
import time
import hashlib
#PYTHON
from django.http import HttpResponse
from django.views.generic import View
#SB
from API.views.FacebookView import FacebookView
from API.views.GoogleView import GoogleView
from APP.models.UserAccessTokenModel import UserAccessToken

"""
 @class AuthenticationView
 @version 0.1
 @author M.Jansma
"""

class AuthenticationView (View):
    
    ###################################
    ####### User logout request #######
    ###################################
    
    def logout (self, request) :
        request.session.clear();
        return self.response({ 'status' : 200, 'message' : 'User succesfully logged out!' });
          
    ##############################
    ### Facebook auth request ###
    ##############################
    def facebookAuth (self, request) :
        if ('accessToken' in request.POST) :
            facebook = FacebookView(request.POST['accessToken']);
            facebook.login();
            state = facebook.getLoginState();
            #Successfully signed in
            if(state['status'] == 200) :
                state['data'] = { 'access_token' : self.setAccessToken(facebook.getUserLogin()) };
                request.session['logged_in'] = True;
                request.session['user_login_id'] = facebook.getUserLogin().user_login_id;
            return self.response(state);
    
    ############################
    ### Google auth request ###
    ############################
    def googleAuth (self, request) :
        if ('accessToken' in request.POST) :
            google = GoogleView(request.POST['accessToken']);
            google.login();
            state = google.getLoginState();
            #Successfully signed in
            if(state['status'] == 200) : 
                state['data'] = { 'access_token' : self.setAccessToken(google.getUserLogin()) };
                request.session['logged_in'] = True;
                request.session['user_login_id'] = google.getUserLogin().user_login_id;
            return self.response(state);

    #Set
    def setAccessToken(self, userLogin) :
        #TMP GEN ACCESS TOKEN
        accessToken = hashlib.sha1('#SB' + str(time.time()) + str(userLogin.user.user_id));
        userAccessToken = UserAccessToken(user = userLogin.user, access_token = accessToken.hexdigest());
        userAccessToken._save();
        return userAccessToken.access_token;
        #TMP GEN ACCESS TOKEN

    #Response 
    def response (self, data) :
        return HttpResponse(json.dumps(data), content_type = 'application/json');
    
    