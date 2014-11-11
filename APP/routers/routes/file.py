from django.conf.urls import patterns, include, url

from APP.views.FileView import FileView

urlpatterns = patterns('',
	url(r'^(?P<categoryId>\d+)/(?P<page>\d+)/$', FileView().index),
	url(r'^(?P<categoryId>\d+)/(?P<orderBy>\w+)/(?P<orderBySeq>\w+)/$', FileView().index),
	url(r'^(?P<categoryId>\d+)/(?P<page>\d+)/(?P<orderBy>\w+)/(?P<orderBySeq>\w+)/$', FileView().index),
    url(r'^(?P<categoryId>\d+)/$', FileView().index),
    
    url(r'^read/(?P<id>\d+)/$', FileView().read),
    url(r'^download/(?P<id>\d+)/$', FileView().download),
    url(r'^create/$', FileView().create),
    url(r'^update/(?P<id>\d+)/$', FileView().update),
    url(r'^addRating/$', FileView().addRating),
)