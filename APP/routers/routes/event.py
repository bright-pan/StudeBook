from django.conf.urls import patterns, include, url

from APP.views.EventView import EventView

urlpatterns = patterns('',
    url(r'^$', EventView().index),
    url(r'^(?P<page>\d+)/$', EventView().index),
    url(r'^read/(?P<eventID>\d+)/$', EventView().show),
    url(r'^read/(?P<eventID>\d+)/edit/', EventView().updateEvent),
    url(r'^read/(?P<eventID>\d+)/unsubscribe/', EventView().unsubscribe),
    url(r'^read/(?P<eventID>\d+)/subscribe/', EventView().subscribe),
    url(r'^read/(?P<eventID>\d+)/delete/', EventView().deleteEvent),
    url(r'^update/$', EventView().update, name="event_update"),
    url(r'^create/$', EventView().create),
)