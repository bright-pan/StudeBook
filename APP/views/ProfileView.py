#SB
from APP.views.MainView import MainView
from APP.models.UserLoginModel import UserLogin


"""
 @class ProfileView
 @version 0.1
 @author StudeBook inc.
"""

class ProfileView(MainView):
    
    def get (self, request) :
    	# session = request.session.get('user_login_id', False)
    	# user = UserLogin.objects.get(user_login_id = session)
        return super(ProfileView, self).render(request, 'profile/profile.html', {
            'title'     : 'Ehh',
            'message'   : 'Nils, lelijke css.'
        });
        
    def test (self, request) :
    	# session = request.session.get('user_login_id', False)
    	# user = UserLogin.objects.get(user_login_id = session)
        return super(ProfileView, self).render(request, 'profile/profile.html', {
            'title'     : 'Ehh',
            'message'   : 'Matha Facka'
        });

