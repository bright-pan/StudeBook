from django.conf.urls import patterns, include, url

from APP.views.PageView import PageView

urlpatterns = patterns('',
    url(r'^$', PageView().index),
    url(r'^(?P<page>\d+)/$', PageView().index),
    url(r'^show/(?P<pageID>\d+)/$', PageView().show),
    url(r'^show/(?P<pageID>\d+)/edit/', PageView().updatePage),
    url(r'^show/(?P<pageID>\d+)/unsubscribe/', PageView().unsubscribe),
    url(r'^show/(?P<pageID>\d+)/subscribe/', PageView().subscribe),
    url(r'^show/(?P<pageID>\d+)/delete/', PageView().deletePage),
    url(r'^update/$', PageView().update, name="page_update"),
    url(r'^create/$', PageView().create),
)