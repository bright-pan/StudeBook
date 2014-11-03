from django.conf.urls import patterns, include, url

from APP.views.FriendView import FriendView

urlpatterns = patterns('',
    url(r'^$', FriendView().index),
    url(r'searchPeople^$', FriendView().searchPeople),
)