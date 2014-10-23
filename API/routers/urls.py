#DJANGO
from django.conf.urls import patterns, url
#APP
from API.views.APIView import APIView

urlpatterns = patterns('',
	url(r'^/$', APIView.as_view(), name = 'API'),
)