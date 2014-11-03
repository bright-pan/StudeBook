#Django
from django.http import HttpResponse
from django.core import serializers
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

#SB
from APP.views.MainView import MainView
from APP.models.UserLoginModel import UserLogin
from APP.models.UserModel import User
from APP.models.CountryModel import Country

import json
import array

"""
 @class ProfileView
 @version 0.1
 @author StudeBook inc.
"""

class ProfileView(MainView):
    def show (self, request) :
        userLogin = super(ProfileView, self).getUserLogin(request)
        currentCountry = Country.objects.get(country_id=userLogin.user.country)

        countries = Country.objects.all()
        countryList = '['
        for country in countries:
            countryList += '{value: ' + str(country.country_id) + ', text : "' + country.name + '"},'
        countryList[:-1]
        countryList += ']'

        return super(ProfileView, self).render(request, 'profile/profile.html', {
            'countries' : countryList,
            'currentCountry' : currentCountry
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

    def getCountries(self, request):
        countries = Country.objects.all()
        countryList = '['
        for country in countries:
            countryList += '{value: ' + str(country.country_id) + ', text : "' + country.name + '"},'
        countryList[:-1]
        countryList += ']' 

        return HttpResponse("Hoi")

