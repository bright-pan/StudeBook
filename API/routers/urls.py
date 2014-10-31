#DJANGO
from django.conf.urls import patterns, url, include
#APP
from API.views.APIView import APIView

urlpatterns = patterns('',
	url(r'^/$', APIView.as_view(), name = 'API'),
	url(r'^/externalAccountLogin/', include('API.routers.routes.authentication')),
)