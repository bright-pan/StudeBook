from django.conf.urls import patterns, url
from APP.views.SoftwareView import SoftwareView


urlpatterns = patterns('',
    url(r'^$', SoftwareView().index),
    url(r'^create/$', SoftwareView().create),
    url(r'^(?P<softwareID>\d+)/$', SoftwareView().read),
    url(r'^(?P<softwareID>\d+)/edit/$', SoftwareView().update),
    url(r'^(?P<softwareID>\d+)/delete/$', SoftwareView().delete)
)
