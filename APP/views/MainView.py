#DJANGO
from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponseRedirect
#SB
from APP.models.UserLoginModel import UserLogin
from APP.models.UserFriendModel import UserFriend


"""
 @class MainView
 @version 0.1
 @author StudeBook inc.
"""

class MainView(View) :

    #Get session data
    def getSessionValue (self, request, key, default = False) :
        return request.session.get(key, default);

    #Get user login state
    def isLoggedIn (self, request) :
        return self.getSessionValue(request, 'logged_in');

    #Get user friend by user
    def getUserFriend (self, request) :
        if (self.isLoggedIn(request)) :
            return UserFriend.getUserFriendByUser(self.getUserLogin(request).user);

    #Get user login instance
    def getUserLogin (self, request) :
        if (self.isLoggedIn(request)) :
            return UserLogin.objects.get(user_login_id = self.getSessionValue(request, 'user_login_id'));
        return False;

    #Render template
    def render (self, request, template, params) :
        #TMP AUTHENTICATION FIX
        if (not self.isLoggedIn(request) and request.get_full_path() != '/authentication/login/') :
          return HttpResponseRedirect('/authentication/login/');
        #Manipulate params
        params.update({
            'logged_in'   : self.isLoggedIn(request),
            'user_login'  : self.getUserLogin(request),
            'user_friend' : self.getUserFriend(request),
            'request_uri' : request.get_full_path()
        });
        #Render view
        return render(request, template, params);
