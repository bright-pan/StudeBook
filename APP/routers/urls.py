#DJANGO
from django.conf.urls import patterns, url
#APP
from APP.views.APPView import APPView
from APP.views.LoginView import LoginView

urlpatterns = patterns('',
	url(r'^$', APPView.as_view(), name = 'APP'),
	url(r'^login$', LoginView.as_view(), name = 'Login'),
)