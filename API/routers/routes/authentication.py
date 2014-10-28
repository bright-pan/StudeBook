from django.conf.urls import patterns, include, url

from API.views.AuthenticationView import AuthenticationView

urlpatterns = patterns('',
    #url(r'^provider:(?P<provider>\w+)$', AuthenticationView.as_view(), name = 'Dynamic'),
    url(r'^provider:google/$', AuthenticationView().googleAuth, name = 'Google OAuth'),
    url(r'^provider:facebook/$', AuthenticationView().facebookAuth, name = 'Facebook OAuth'),
    url(r'^logout/$', AuthenticationView().logout, name = 'Logout'),
)