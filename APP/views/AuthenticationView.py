#DJANGO
from django.http import HttpResponseRedirect
#SB
from APP.views.MainView import MainView

"""
 ### StudeBook AuthenticationView ### 
 @class AuthenticationView
 @version 0.1
 @author StudeBook inc.
"""

class AuthenticationView (MainView) :

    #Authentication redirect
    def get (self, request) :
        #User already logged in
        if (super(AuthenticationView, self).isLoggedIn(request)) : 
            return HttpResponseRedirect('/authentication/logout');
        return HttpResponseRedirect('/authentication/login');

    #Authentication login page
    def login (self, request) :
        #User already logged in
        if (super(AuthenticationView, self).isLoggedIn(request)) : 
            return HttpResponseRedirect('/authentication/logout');
        #Render login page
        return super(AuthenticationView, self).render(request, 'authentication/login.html', {
            'title'     : 'StudeBook',
            'message'   : 'Authentication.'
        });
        
    #Authentication logout page
    def logout (self, request) :
        #User not logged in
        if (not super(AuthenticationView, self).isLoggedIn(request)) : 
            return HttpResponseRedirect('/authentication/login');
        
        #Render logout page
        return super(AuthenticationView, self).render(request, 'authentication/logout.html', {
            'title'     : 'StudeBook',
            'message'   : 'Authentication.'
        });