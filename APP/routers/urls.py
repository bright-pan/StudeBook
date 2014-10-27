#DJANGO
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import ListView

#APP
from APP.views.APPView import APPView
from APP.views.LoginView import LoginView
from APP.views.ProfileView import ProfileView
from APP.views.PageView import PageView
from APP.views.FileView import FileView

urlpatterns = patterns('',
	url(r'^$', APPView.as_view(), name = 'APP'),
	url(r'^login$', LoginView.as_view(), name = 'Login'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^profile/', ProfileView.as_view()),
	url(r'^page/$', PageView.as_view()),
	url(r'^page/(?P<pageID>\w+)/$', PageView.as_view()),
	url(r'^file/$', FileView.as_view()),
)