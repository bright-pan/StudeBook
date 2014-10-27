from django.conf.urls import patterns, include, url

from APP.views.ProfileView import ProfileView

urlpatterns = patterns('',
    url(r'^$', ProfileView().get),
    url(r'^test/$', ProfileView().test),
)