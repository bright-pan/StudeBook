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
    user = None;
    
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
                self.user = self.updateUser(externalUser);
            #Create user
            except :
                self.user = self.createUser(externalUser);
    
    #Update user 
    def updateUser (self, externalUser) :
        userLogin = UserLogin.objects.get(provider = 'google', provider_id = externalUser['id']); 
        userLogin.access_token = self.accessToken;
        userLogin.save();
        return userLogin;  
        
    #Create user
    #TODO -> User validation for multiple providers
    def createUser (self, externalUser) :
        #UserModel 
        user = User();
        user.first_name = externalUser['name']['givenName'];
        user.last_name = externalUser['name']['familyName'];    
        user.save();
        #UserLoginModel
        userLogin = UserLogin(user = user, access_token = self.accessToken);
        userLogin.provider = 'google';
        userLogin.provider_id = externalUser['id'];
        userLogin.save();
        return userLogin;
    
    #Get user
    def getUser (self) :
        return self.user;
    
    #Get user login state
    def getLoginState (self) :
        if (self.user is not None) : 
            return { 'status' : 200, 'message' : 'Successfully signed in using Google+' };
        return { 'status' : 400, 'message' : 'Bad request' };
    
    
    