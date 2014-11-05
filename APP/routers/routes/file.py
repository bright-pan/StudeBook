from django.conf.urls import patterns, include, url

from APP.views.FileView import FileView

urlpatterns = patterns('',
    url(r'^(?P<categoryId>\d+)/$', FileView().index),
    url(r'^show/(?P<id>\d+)/$', FileView().show),
    url(r'^create/$', FileView().create),
    url(r'^addRating/$', FileView().addRating),
)