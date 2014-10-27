#SB
from APP.views.MainView import MainView
from APP.models.UserLoginModel import UserLogin
from APP.models.UserModel import User


"""
 @class ProfileView
 @version 0.1
 @author StudeBook inc.
"""

class ProfileView(MainView):
    def show (self, request) :
        return super(ProfileView, self).render(request, 'profile/profile.html', {
            
        });
        
    def update (self, request) :
        name = request.POST.get('name', '')
        value = request.POST.get('value', '')
        pk = request.POST.get('pk', '')

        record = User.objects.get(user_id = pk)
        record.__setattr__(name, value)
        record.save()

        return super(ProfileView, self).render(request, 'profile/profile.html', {
            
        });

