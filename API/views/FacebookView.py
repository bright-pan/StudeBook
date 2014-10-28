#DJANGO
from django.views.generic import View
#SB
from API.lib import facebook
from APP.models.UserLoginModel import UserLogin
from APP.models.UserModel import User

"""
 @class FacebookLoginView
 @version 0.1
 @author StudeBook inc.
"""

class FacebookView (View) :
    
    accessToken = None;
    user = None;
    
    def __init__ (self, accessToken) :
        self.accessToken = accessToken;
    
    #Get user data from FB API by AccessToken
    def getUserByAccessToken (self) :
        try :
            graph = facebook.GraphAPI(self.accessToken);
            return graph.get_object('me');
        except :
            return False;
    
    #Login with FB credentials
    def login (self) :
        #Get user data from FB API by AccessToken
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
        userLogin = UserLogin.objects.get(provider = 'facebook', provider_id = externalUser['id']); 
        userLogin.access_token = self.accessToken;
        userLogin.save();
        return userLogin;  
        
    #Create user
    #TODO -> User validation for multiple providers
    def createUser (self, externalUser) :
        #UserModel 
        user = User();
        user.first_name = externalUser['first_name'];
        user.last_name = externalUser['last_name'];  
        user.email_address = externalUser['email'];      
        user.save();
        #UserLoginModel
        userLogin = UserLogin(user = user, access_token = self.accessToken);
        userLogin.provider = 'facebook';
        userLogin.provider_id = externalUser['id'];
        userLogin.save();
        return userLogin;
    
    #Get user
    def getUser (self) :
        return self.user;
    
    #Get user login state
    def getLoginState (self) :
        if (self.user is not None) : 
            return { 'status' : 200, 'message' : 'Successfully signed in using Facebook' };
        return { 'status' : 400, 'message' : 'Bad request' };
    
    
    