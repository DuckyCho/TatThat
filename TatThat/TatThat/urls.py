from django.conf.urls import patterns, include, url
from django.contrib import admin
from index.views import Error400View ,Error403View, Error404View, Error500View

handler400 = 'index.views.Error400View'
handler403 = 'index.views.Error403View'
handler404 = 'index.views.Error404View'
handler500 = 'index.views.Error500View'

urlpatterns = patterns('',
    url(r'^$',include('index.urls')),
    url(r'^pic/',include('pic.urls')),
    url(r'^scrap/',include('scrap.urls')),
    url(r'^search/', include('search.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

