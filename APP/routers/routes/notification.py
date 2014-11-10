from django.conf.urls import patterns, include, url

from APP.views.NotificationView import NotificationView

urlpatterns = patterns('',
    url(r'^$', NotificationView().show),
    url(r'^(?P<notificationId>\d+)$', NotificationView().getNotification),
)