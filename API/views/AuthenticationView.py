#PYTHON
import json
#PYTHON
from django.http import HttpResponse
from django.views.generic import View
#SB
from API.views.FacebookView import FacebookView
from API.views.GoogleView import GoogleView

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
    
    ###################################
    ### User external account login ###
    ###################################
    def post (self, request, provider) :
        #POST params
        accessToken = request.POST['accessToken'];
        #Facebook OAuth
        if (provider == 'facebook') : 
            return self.response(self.facebookLogin(request, accessToken));
        #Google OAuth
        elif (provider == 'google') :
            return self.response(self.googleLogin(request, accessToken));
        #Bad request
        else :
            return self.response({ 'status' : 400, 'message' : 'Bad request' });
          
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
                request.session['logged_in'] = True;
                request.session['user_login_id'] = facebook.getUser().user_login_id;
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
                request.session['logged_in'] = True;
                request.session['user_login_id'] = google.getUser().user_login_id;
            return self.response(state);
        
    #Response 
    def response (self, data) :
        return HttpResponse(json.dumps(data), content_type = 'application/json');
    
    