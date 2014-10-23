from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^', include('APP.routers.urls')),
    #url(r'^api', include('API.routers.urls')),
)
