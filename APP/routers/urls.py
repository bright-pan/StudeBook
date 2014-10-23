#DJANGO
from django.conf.urls import patterns, url
#APP
from APP.views.APPView import APPView

urlpatterns = patterns('',
	url(r'^$', APPView.as_view(), name = 'APP'),
)