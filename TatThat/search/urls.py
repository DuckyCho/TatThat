# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from search import views
urlpatterns = patterns('',
    url(r'^$', views.SearchMainView.as_view(), name='searchMain'),
    url(r'^tag/(?P<query>.+)/$', views.TagSearchResultView.as_view(), name='searchResult'),


)
