from django.conf.urls import patterns, include, url

from API.views.UserView import UserView

urlpatterns = patterns('',
    url(r'^getInfo/accessToken:(?P<accessToken>\w{40})/$', UserView().getInfo, name = 'Get info'),
    url(r'^getFriends/accessToken:(?P<accessToken>\w{40})/$', UserView().getFriends, name = 'Get friends'),
)