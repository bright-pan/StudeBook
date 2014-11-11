from django.conf.urls import patterns, url
from APP.views.SoftwareView import SoftwareView


urlpatterns = patterns('',
    url(r'^$', SoftwareView().index),
    url(r'^(?P<page>\d+)/$', SoftwareView().index),
    url(r'^create/$', SoftwareView().create),
    url(r'^read/(?P<software_id>\d+)/$', SoftwareView().read),
    url(r'^update/(?P<software_id>\d+)/$', SoftwareView().update),
    url(r'^delete/(?P<software_id>\d+)/$', SoftwareView().delete)
)
