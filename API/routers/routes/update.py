from django.conf.urls import patterns, include, url

from API.views.UpdateView import UpdateView

urlpatterns = patterns('',
    url(r'^getUpdates/$', UpdateView().getUpdates, name = 'Get updates'),
)