#Django
from django.http import HttpResponse
from django.core import serializers
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404

#SB
from APP.views.MainView import MainView
from APP.models.UserLoginModel import UserLogin
from APP.models.UserModel import User
from APP.models.UserFriendModel import UserFriend
from APP.models.UserTypeModel import UserType
from APP.models.CountryModel import Country
from APP.models.MessageModel import Message

import json
import array

"""
 @class ProfileView
 @version 0.1
 @author StudeBook inc.
"""

class ProfileView(MainView):
    def show (self, request, userId=None) :
        userLogin = super(ProfileView, self).getUserLogin(request)
        if not userId:
            user = userLogin.user
            showAll = True
        elif int(userLogin.user.pk) == int(userId):
            user = userLogin.user
            showAll = True
        else: 
            user = get_object_or_404(User, pk=userId)
            if UserFriend.objects.filter(requester_id=userLogin.user.user_id, recipient_id=userId, status='accepted'):
                showAll = True
            else :
                showAll = False

        currentCountry = Country.objects.get(country_id=user.country)

        countries = Country.objects.all()
        countryList = '['
        for country in countries:
            countryList += '{value: ' + str(country.country_id) + ', text : "' + country.name + '"},'
        countryList[:-1]
        countryList += ']'

        messages = Message.objects.filter(recipient_id=user.user_id).order_by('-created_at')
        for message in messages:
            message.user = User.objects.get(user_id=message.creator_id)

        return super(ProfileView, self).render(request, 'profile/profile.html', {
            'countries' : countryList,
            'currentCountry' : currentCountry,
            'user' : user,
            'showAll' : showAll,
            'currentUserId' : userLogin.user.pk,
            'messages' : messages
        });
        
    def update (self, request) :
        name = request.POST.get('name', '')
        value = request.POST.get('value', '')
        pk = request.POST.get('pk', '')

        if name == 'email_address':
            try:
                validate_email( value )
            except ValidationError:
                data = json.dumps({ 'status' : 422, 'message' : 'Invalid email' });
                return HttpResponse(data,content_type='application/json');

        record = User.objects.get(user_id = pk)
        record.__setattr__(name, value)
        record.save()
        data = json.dumps({ 'status' : 200 });
        return HttpResponse(data,content_type='application/json');

    def settings (self, request) :
        userLogin = super(ProfileView, self).getUserLogin(request)
        currentCountry = Country.objects.get(country_id=userLogin.user.country)
        currentRole = UserType.objects.get(pk=userLogin.user.user_type_id)

        countries = Country.objects.all()
        countryList = '['
        for country in countries:
            countryList += '{value: ' + str(country.country_id) + ', text : "' + country.name + '"},'
        countryList[:-1]
        countryList += ']'

        roles = UserType.objects.all()
        rolesList = '['
        for role in roles:
            rolesList += '{value: ' + str(role.pk) + ', text : "' + role.type + '"},'
        rolesList[:-1]
        rolesList += ']'

        return super(ProfileView, self).render(request, 'profile/settings.html', {
            'countries' : countryList,
            'roles' : rolesList,
            'currentCountry' : currentCountry,
            'currentRole' : currentRole
        });

    def details (self, request, userId=None) :
        userLogin = super(ProfileView, self).getUserLogin(request)
        currentRole = UserType.objects.get(pk=userLogin.user.user_type_id)
        if not userId:
            user = userLogin.user
            showAll = True
        elif int(userLogin.user.pk) == int(userId):
            user = userLogin.user
            showAll = True
        else: 
            user = get_object_or_404(User, pk=userId)
            if UserFriend.objects.filter(requester_id=userLogin.user.user_id, recipient_id=userId, status='accepted'):
                showAll = True
            else :
                showAll = False

        currentCountry = Country.objects.get(country_id=user.country)

        return super(ProfileView, self).render(request, 'profile/details.html', {
            'currentRole': currentRole,
            'currentCountry' : currentCountry,
            'user' : user,
            'showAll' : showAll
        });

    def sendMessage (self, request) :
        message = Message(creator_id=request.POST['current_user'], recipient_id=request.POST['target_user'], message=request.POST['message'])
        message.save()

        data = json.dumps({ 'status' : 200, 'message' : 'Succes!!' });
        return HttpResponse(data,content_type='application/json');
