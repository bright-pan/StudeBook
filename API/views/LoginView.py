#PYTHON
import json
#PYTHON
from django.http import HttpResponse
from django.views.generic import View
#SB
from API.views.FacebookLoginView import FacebookLoginView
from API.views.GoogleLoginView import GoogleLoginView

"""
 @class LoginView
 @version 0.1
 @author M.Jansma
"""

class LoginView (View):
    
    #DEMO
    def get (self, request, provider) : 
        return self.response({ 'status' : 200, 'message' : 'External Account', 'provider' : provider });
    
    #Response 
    def response (self, data) :
        return HttpResponse(json.dumps(data), content_type = 'application/json');
    
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
    ### Facebook login request ###
    ##############################
    def facebookLogin (self, request, accessToken) :
        facebook = FacebookLoginView(accessToken);
        facebook.login();
        state = facebook.getLoginState();
        #Successfully signed in
        if(state['status'] == 200) : 
            request.session['logged_in'] = True;
            request.session['user_login_id'] = facebook.getUser().user_login_id;
        return state;
    
    ############################
    ### Google login request ###
    ############################
    def googleLogin (self, request, accessToken) :
        google = GoogleLoginView(accessToken);
        google.login();
        state = google.getLoginState();
        #Successfully signed in
        if(state['status'] == 200) : 
            request.session['logged_in'] = True;
            request.session['user_login_id'] = google.getUser().user_login_id;
        return state;
    