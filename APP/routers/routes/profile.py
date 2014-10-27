from django.conf.urls import patterns, include, url

from APP.views.ProfileView import ProfileView

urlpatterns = patterns('',
    url(r'^$', ProfileView().show),
    url(r'^update/$', ProfileView().update, name="profile_update"),
)