from django.conf.urls import patterns, include, url

from APP.views.LoginView import LoginView

urlpatterns = patterns('',
    url(r'^$', LoginView.as_view(), name = 'Login'),
)