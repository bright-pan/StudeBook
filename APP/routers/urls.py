#DJANGO
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import ListView

#APP
from APP.views.APPView import APPView
from APP.views.PageView import PageView
from APP.views.FileView import FileView

# from APP.routers.routes.profile 

urlpatterns = patterns('',
	url(r'^$', APPView.as_view(), name = 'APP'),
	url(r'^login$', include('APP.routers.routes.login')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^profile/', include('APP.routers.routes.profile')),
	url(r'^page/$', include('APP.routers.routes.page')),
	url(r'^file/$', include('APP.routers.routes.file')),
)