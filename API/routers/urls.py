#DJANGO
from django.conf.urls import patterns, url
#APP
from API.views.APIView import APIView
from API.views.LoginView import LoginView

urlpatterns = patterns('',
	url(r'^/$', APIView.as_view(), name = 'API'),
	url(r'^/externalAccountLogin/provider:(?P<provider>\w+)$', LoginView.as_view(), name = 'Login'),
)