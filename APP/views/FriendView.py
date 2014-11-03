#Djano
from django.http import HttpResponse
from django.forms.models import model_to_dict
#SB
from APP.views.MainView import MainView
from APP.models.UserLoginModel import UserLogin
from APP.models.UserModel import User
from APP.models.UserFriendModel import UserFriend
from itertools import chain



"""
 @class FriendView
 @version 0.1
 @author StudeBook inc.
"""

class FriendView(MainView):
    def index (self, request) :
    	userLogin = super(FriendView, self).getUserLogin(request)

    	relationships = UserFriend.objects.filter(requester_id=userLogin.user.user_id, status=2)
    	friends = []
    	for relationship in relationships:
    		friends.append(User.objects.get(user_id=relationship.recipient_id))
        return super(FriendView, self).render(request, 'friend/index.html', {
        	'friends' : friends
        });

    def searchPeople (self, request) :
    	userLogin = super(FriendView, self).getUserLogin(request)
    	search = request.POST.get('search', '')

    	if search:
	    	firstNameMatches = User.objects.filter(first_name__icontains=search)
	    	lastNameMatches = User.objects.filter(last_name__icontains=search)
	    	matches = list(chain(lastNameMatches, firstNameMatches))
	    	for match in matches:
	    		# Check if friend already
	    		if UserFriend.objects.filter(requester_id=userLogin.user.user_id, recipient_id=match.user_id, status=2):
	    			match.friend = True
    			else: 
    				match.friend = False
    			# Check if blocked both ways
    			if (UserFriend.objects.filter(requester_id=userLogin.user.user_id, recipient_id=match.user_id, status=4) or UserFriend.objects.filter(requester_id=match.user_id, recipient_id=userLogin.user.user_id, status=4)):
	    			match.hidden = True
    			else: 
    				match.hidden = False

    	else:
    		matches = ''

    	return super(FriendView, self).render(request, 'friend/search.html', {
        	'matches' : matches,
        	'userLogin' : userLogin
        });