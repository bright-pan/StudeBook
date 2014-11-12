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

		relationships = UserFriend.objects.filter(requester_id=userLogin.user.user_id, status='accepted').order_by('since')
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
		if record:
			if record[0].status == 'pending':
				record[0].status = 2
				record[0].save()
				record = UserFriend.objects.get(requester_id = userId, recipient_id = userLogin.user.user_id)
				record.status = 2
				record.save()
			else:
				record[0].status = 6
				record[0].save()
				newRecord = UserFriend.objects.get(requester_id = userId, recipient_id = userLogin.user.user_id)
				newRecord.status = 1
				newRecord.save()
		else:
			record = UserFriend(requester_id = userLogin.user.user_id, recipient_id = userId, status = 6)
			record.save()
			record = UserFriend(requester_id = userId, recipient_id = userLogin.user.user_id, status = 1)
			record.save()
		
		response_data = {}
		response_data['result'] = '200'
		response_data['message'] = 'derp'
		return HttpResponse(json.dumps(response_data), content_type="application/json")

	def block (self, request, userId) :
		userLogin = super(FriendView, self).getUserLogin(request)
		record = UserFriend.objects.filter(requester_id = userLogin.user.user_id, recipient_id = userId)
		if record:
			record[0].status = 5
			record[0].save()
			newRecord = UserFriend.objects.get(requester_id = userId, recipient_id = userLogin.user.user_id)
			newRecord.status = 4
			newRecord.save()
		else:
			record = UserFriend(requester_id = userLogin.user.user_id, recipient_id = userId, status = 5)
			record.save()
			record = UserFriend(requester_id = userId, recipient_id = userLogin.user.user_id, status = 4)
			record.save()
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
		record = UserFriend.objects.filter(requester_id = userId, recipient_id = userLogin.user.user_id)
		if record:
			record[0].delete()
		response_data = {}
		response_data['result'] = '200'
		response_data['message'] = 'Succes unblock'
		return HttpResponse(json.dumps(response_data), content_type="application/json")

	def cancelRequest (self, request, userId) :
		userLogin = super(FriendView, self).getUserLogin(request)
		record = UserFriend.objects.filter(requester_id = userLogin.user.user_id, recipient_id = userId, status = 'request')
		newRecord = UserFriend.objects.filter(requester_id = userId, recipient_id = userLogin.user.user_id, status = 'pending')
		# Should only return one record
		if record:
			record[0].delete()
		if newRecord:
			newRecord[0].delete()
		response_data = {}
		response_data['result'] = '200'
		response_data['message'] = 'Succes'
		return HttpResponse(json.dumps(response_data), content_type="application/json")

	def removeFriend (self, request, userId) :
		userLogin = super(FriendView, self).getUserLogin(request)
		try:
			record = UserFriend.objects.get(requester_id = userLogin.user.user_id, recipient_id = userId, status = 'accepted')
			# Should only return one record
			if record:
				record.delete()
			record = UserFriend.objects.get(requester_id = userId, recipient_id = userLogin.user.user_id, status ='accepted')
			# Should only return one record
			if record:
				record.delete()
		except Exception as e:
			response_data = {}
			response_data['result'] = '404'
			response_data['message'] = 'You messed up'
			return HttpResponse(json.dumps(response_data), content_type="application/json")
		response_data = {}
		response_data['result'] = '200'
		response_data['message'] = 'Succes'
		return HttpResponse(json.dumps(response_data), content_type="application/json")

	def friendRequest (self, request) :
		userLogin = super(FriendView, self).getUserLogin(request)
		friendRequests = UserFriend.objects.filter(requester_id = userLogin.user.user_id, status = 'pending')
		for friendRequest in friendRequests:
			user = User.objects.get(user_id=friendRequest.recipient_id)
			friendRequest.first_name = user.first_name
			friendRequest.last_name = user.last_name
	
		return super(FriendView, self).render(request, 'friend/requests.html', {
			'matches' : friendRequests
		});

	
