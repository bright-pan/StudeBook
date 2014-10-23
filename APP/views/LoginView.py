#StudeBook
from APP.views.MainView import MainView

"""
 ### StudeBook login page ### 
 @class APPView
 @version 0.1
 @author StudeBook inc.
"""

class LoginView (MainView):

    def get (self, request) :
        
        return super(LoginView, self).render(request, 'login.html', {
            'title'   : 'Login',
            'message' : 'OAuth login.'
        });