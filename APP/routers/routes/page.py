from django.conf.urls import patterns, include, url

from APP.views.PageView import PageView

urlpatterns = patterns('',
    url(r'^$', PageView().get),
    url(r'^test/$', PageView().test),
    url(r'^getPage/$', PageView().getPage),
    url(r'^getPages/$', PageView().getPages),
)