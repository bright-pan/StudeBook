from django.conf.urls import patterns, include, url

from APP.views.EventView import EventView

urlpatterns = patterns('',
    url(r'^$', EventView().index),
    url(r'^(?P<page>\d+)/$', EventView().index),
    url(r'^show/(?P<eventID>\d+)/$', EventView().show),
    url(r'^show/(?P<eventID>\d+)/edit/', EventView().updateEvent),
    url(r'^show/(?P<eventID>\d+)/unsubscribe/', EventView().unsubscribe),
    url(r'^show/(?P<eventID>\d+)/subscribe/', EventView().subscribe),
    url(r'^show/(?P<eventID>\d+)/delete/', EventView().deleteEvent),
    url(r'^update/$', EventView().update, name="event_update"),
    url(r'^create/$', EventView().create),
)