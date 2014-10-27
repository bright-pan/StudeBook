from django.conf.urls import patterns, include, url

from APP.views.FileView import FileView

urlpatterns = patterns('',
    url(r'^$', FileView().get),
)