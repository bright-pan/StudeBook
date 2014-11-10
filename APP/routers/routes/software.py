from django.conf.urls import patterns, url
from APP.views.SoftwareView import SoftwareView


urlpatterns = patterns('',
    url(r'^$', SoftwareView().index),
    url(r'^create/$', SoftwareView().create),
    url(r'^(?P<software_id>\d+)/$', SoftwareView().read),
    url(r'^(?P<software_id>\d+)/edit/$', SoftwareView().update),
    url(r'^(?P<software_id>\d+)/delete/$', SoftwareView().delete)
)
