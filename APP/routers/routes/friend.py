from django.conf.urls import patterns, include, url

from APP.views.FriendView import FriendView

urlpatterns = patterns('',
    url(r'^$', FriendView().index),
    url(r'search/$', FriendView().searchPeople),
    url(r'block/(?P<userId>\d+)$', FriendView().block),
    url(r'add/(?P<userId>\d+)$', FriendView().addFriend),
    url(r'remove/(?P<userId>\d+)$', FriendView().removeFriend),
    url(r'cancel/(?P<userId>\d+)$', FriendView().cancelRequest),
    url(r'undoBlock/(?P<userId>\d+)$', FriendView().unblock),
    url(r'request/$', FriendView().friendRequest),
)