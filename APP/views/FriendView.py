#Djano
from django.http import HttpResponse
from django.db.models import Q
import json

#SB
from APP.views.MainView import MainView
from APP.models.UserLoginModel import UserLogin
from APP.models.UserModel import User
from APP.models.UserFriendModel import UserFriend



"""
 @class FriendView
 @version 0.1
 @author StudeBook inc.
"""

class FriendView(MainView):
	def index (self, request) :
		userLogin = super(FriendView, self).getUserLogin(request)

		relationships = UserFriend.objects.filter(requester_id=userLogin.user.user_id, status=2).order_by('since')
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
			matches = User.objects.filter(Q(first_name__icontains=search) | Q(last_name__icontains=search)).distinct()
			for match in matches:
				relation = UserFriend.objects.filter(requester_id=userLogin.user.user_id, recipient_id=match.user_id)
				if relation:
					match.status = relation[0].status
		else:
			matches = ''

		return super(FriendView, self).render(request, 'friend/search.html', {
			'matches' : matches,
			'userLogin' : userLogin
		});

	def addFriend (self, request, userId) :
		userLogin = super(FriendView, self).getUserLogin(request)
		record = UserFriend.objects.filter(requester_id = userLogin.user.user_id, recipient_id = userId)
		if not record:
			record = UserFriend(requester_id = userLogin.user.user_id, recipient_id = userId, status = 1)
			record.save()
		else:
			record[0].status = 1
			record[0].save()
		response_data = {}
		response_data['result'] = '200'
		response_data['message'] = 'Succes'
		return HttpResponse(json.dumps(response_data), content_type="application/json")

	def block (self, request, userId) :
		userLogin = super(FriendView, self).getUserLogin(request)
		record = UserFriend.objects.filter(requester_id = userLogin.user.user_id, recipient_id = userId)
		if not record:
			record = UserFriend(requester_id = userLogin.user.user_id, recipient_id = userId, status = 4)
			record.save()
		else:
			record[0].status = 4
			record[0].save()
		response_data = {}
		response_data['result'] = '200'
		response_data['message'] = 'Succes block'
		return HttpResponse(json.dumps(response_data), content_type="application/json")

	def unblock (self, request, userId) :
		userLogin = super(FriendView, self).getUserLogin(request)
		record = UserFriend.objects.filter(requester_id = userLogin.user.user_id, recipient_id = userId)
		# Should only return one record
		if record:
			record[0].delete()
		response_data = {}
		response_data['result'] = '200'
		response_data['message'] = 'Succes unblock'
		return HttpResponse(json.dumps(response_data), content_type="application/json")

	def cancelRequest (self, request, userId) :
		userLogin = super(FriendView, self).getUserLogin(request)
		record = UserFriend.objects.filter(requester_id = userLogin.user.user_id, recipient_id = userId, status = 1)
		# Should only return one record
		if record:
			record[0].delete()
		response_data = {}
		response_data['result'] = '200'
		response_data['message'] = 'Succes'
		return HttpResponse(json.dumps(response_data), content_type="application/json")

	def removeFriend (self, request, userId) :
		userLogin = super(FriendView, self).getUserLogin(request)
		try:
			record = UserFriend.objects.filter(requester_id = userLogin.user.user_id, recipient_id = userId, status = 2)
			# Should only return one record
			if record:
				record[0].delete()
			record = UserFriend.objects.filter(requester_id = userId, recipient_id = userLogin.user.user_id, status = 2)
			# Should only return one record
			if record:
				record[0].delete()
		except Exception as e:
			response_data = {}
			response_data['result'] = '404'
			response_data['message'] = 'You messed up'
			return HttpResponse(json.dumps(response_data), content_type="application/json")
		response_data = {}
		response_data['result'] = '200'
		response_data['message'] = 'Succes'
		return HttpResponse(json.dumps(response_data), content_type="application/json")

	
