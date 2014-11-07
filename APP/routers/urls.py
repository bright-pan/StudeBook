#DJANGO
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import ListView

#APP
from APP.views.APPView import APPView 

urlpatterns = patterns('',
	url(r'^$', APPView.as_view(), name = 'APP'),
	url(r'^authentication/', include('APP.routers.routes.authentication')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^profile/', include('APP.routers.routes.profile')),
	url(r'^page/', include('APP.routers.routes.page')),
	url(r'^software/', include('APP.routers.routes.software')),
	url(r'^file/', include('APP.routers.routes.file')),
	url(r'^friends/', include('APP.routers.routes.friend'))
)
