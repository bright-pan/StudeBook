from django.conf.urls import patterns, include, url

from API.views.UserView import UserView

urlpatterns = patterns('',
    url(r'^getInfo/$', UserView().getInfo, name = 'Get info'),
    url(r'^getFriends/$', UserView().getFriends, name = 'Get friends'),
)