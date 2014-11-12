#StudeBook
from APP.views.MainView import MainView
from django.http import HttpResponse, HttpResponseRedirect

"""
 ### StudeBook main page ### 
 @class APPView
 @version 0.1
 @author StudeBook inc.
"""

class APPView (MainView):

    def get (self, request) :
        #TMP AUTHENTICATION FIX
        if (not super(APPView,self).isLoggedIn(request)) :
          return HttpResponseRedirect('/authentication/login/');
        return HttpResponseRedirect('/profile');