# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from scrap import views
urlpatterns = patterns('',
    url(r'^addscrap/', views.addScrap, name='add_scrap'),
    url(r'^removescrap/', views.removeScrap, name='remove_scrap'),
    url(r'^myscrapbook/', views.MyScrapBookView.as_view(), name='my_scrap_book'),
)
