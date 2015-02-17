from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$',include('index.urls')),
    url(r'^pic/',include('pic.urls')),
    url(r'^search/', include('search.urls')),
    url(r'^user/', include('user.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
