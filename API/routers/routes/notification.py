from django.conf.urls import patterns, include, url

from API.views.NotificationView import NotificationView

urlpatterns = patterns('',
    url(r'^getCount/accessToken:(?P<accessToken>\w{40})/$', NotificationView().getCount, name = 'Get count'),
    url(r'^getInfo/accessToken:(?P<accessToken>\w{40})/$', NotificationView().getCount, name = 'Get into'),
    url(r'^create/accessToken:(?P<accessToken>\w{40})/$', NotificationView().create, name = 'Create info'),
    url(r'^update/accessToken:(?P<accessToken>\w{40})/$', NotificationView().update, name = 'Update notification'),
)