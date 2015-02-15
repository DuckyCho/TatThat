from django.conf.urls import patterns, url
from pic import views

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', views.PicDetailView.as_view(), name='picDetail'),
    url(r'^(?P<pk>\d+)/(?P<back_page_url>)$', views.PicDetailView.as_view(), name='picDetail_daily'),
    url(r'^daily/(?P<pk>\d+)/$', views.PicDetailView.as_view(), name='picDetail_daily'),

)

