from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^$',include('index.urls')),
    url(r'^pic/',include('pic.urls')),
    url(r'^search/', include('search.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

handler404 = 'index.views.Error500View'
handler500 = 'index.views.Error500View'
