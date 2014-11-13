from django.conf.urls import patterns, include, url

from APP.views.ProfileView import ProfileView

urlpatterns = patterns('',
    url(r'^$', ProfileView().show),
    url(r'^update/$', ProfileView().update, name="profile_update"),
    url(r'^settings/$', ProfileView().settings),
    url(r'^details/$', ProfileView().details),
    url(r'^(?P<userId>\d+)/details/$', ProfileView().details),
    url(r'^(?P<userId>\d+)/$', ProfileView().show),
    url(r'^send_message/$', ProfileView().sendMessage),
)