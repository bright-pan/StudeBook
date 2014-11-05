#DJANGO
from django.views.generic import View
#PYTHON
import urllib2
import json
#SB
from APP.models.UserLoginModel import UserLogin
from APP.models.UserModel import User

"""
 @class GoogleLoginView
 @version 0.1
 @author StudeBook inc.
"""

class GoogleView (View) :
    
    API_URI = 'https://www.googleapis.com/plus/v1/people/me';
    accessToken = None;
    userLogin = None;
    
    def __init__ (self, accessToken) :
        self.accessToken = accessToken;
        
    #Get user data from Google API by AccessToken
    def getUserByAccessToken (self) :
        try :
            URI = self.API_URI + '?access_token=' + self.accessToken;
            request = urllib2.urlopen(URI);
            return json.loads(request.read());
        except :
            return False;
    
    #Login with Google credentials
    def login (self) :
        #Get user data from Google API by AccessToken
        externalUser = self.getUserByAccessToken();
        if (externalUser is not False) :
            #Update user
            try :
                self.userLogin = self.updateUserLogin(externalUser);
            #Create user
            except :
                self.userLogin = self.createUserLogin(externalUser);
    
    #Create user
    def createUser (self, externalUser) :
        #UserModel 
        user = User();
        user.first_name = externalUser['name']['givenName'];
        user.last_name = externalUser['name']['familyName'];  
        user.email_address = externalUser['emails'][0]['value'];
        user.save();
        return user;
    
    #Update user 
    def updateUserLogin (self, externalUser) :
        userLogin = UserLogin.objects.get(provider = 'google', provider_id = externalUser['id']); 
        userLogin.access_token = self.accessToken;
        userLogin.save();
        return userLogin;
        
    def createUserLogin (self, externalUser) :
        #Get user
        try : 
            user = User.objects.get(email_address = externalUser['emails'][0]['value']);
        #Create user
        except :
            user = self.createUser(externalUser);
        #Create user login
        userLogin = UserLogin(user = user, access_token = self.accessToken);
        userLogin.provider = 'google';
        userLogin.provider_id = externalUser['id'];
        userLogin.save();
        return userLogin;
    
    #Get user login
    def getUserLogin (self) :
        return self.userLogin;
    
    #Get user login state
    def getLoginState (self) :
        if (self.userLogin is not None) :
            return { 'status' : 200, 'message' : 'Successfully signed in using Google+' };
        return { 'status' : 400, 'message' : 'Bad request' };
    
    
    