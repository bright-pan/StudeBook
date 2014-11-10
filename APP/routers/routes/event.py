from django.conf.urls import patterns, include, url

from APP.views.EventView import EventView

urlpatterns = patterns('',
    url(r'^$', EventView().index),
    url(r'^getEvent/(?P<eventID>\d+)/$', EventView().show),
    url(r'^getEvent/(?P<eventID>\d+)/edit/', EventView().updateEvent),
    url(r'^getEvent/(?P<eventID>\d+)/unsubscribe/', EventView().unsubscribe),
    url(r'^getEvent/(?P<eventID>\d+)/subscribe/', EventView().subscribe),
    url(r'^getEvent/(?P<eventID>\d+)/delete/', EventView().deleteEvent),
    url(r'^update/$', EventView().update, name="event_update"),
    url(r'^add/$', EventView().create),
)