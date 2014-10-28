from django.conf.urls import patterns, include, url

from APP.views.AuthenticationView import AuthenticationView

urlpatterns = patterns('',
    url(r'^$', AuthenticationView.as_view(), name = 'Authentication'),                   
    url(r'^login/$', AuthenticationView().login, name = 'Login'),
    url(r'^logout/$', AuthenticationView().logout, name = 'Logout'),
)