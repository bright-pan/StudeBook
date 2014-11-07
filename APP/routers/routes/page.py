from django.conf.urls import patterns, include, url

from APP.views.PageView import PageView

urlpatterns = patterns('',
    url(r'^$', PageView().index),
    url(r'^getPage/(?P<pageID>\d+)/$', PageView().show),
    url(r'^getPage/(?P<pageID>\d+)/edit/', PageView().updatePage),
    url(r'^getPage/(?P<pageID>\d+)/unsubscribe/', PageView().unsubscribe),
    url(r'^getPage/(?P<pageID>\d+)/subscribe/', PageView().subscribe),
    url(r'^getPage/(?P<pageID>\d+)/delete/', PageView().deletePage),
    url(r'^update/$', PageView().update, name="page_update"),
    url(r'^add/$', PageView().create),
)