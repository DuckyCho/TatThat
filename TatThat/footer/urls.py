from django.conf.urls import patterns, url
from footer import views

urlpatterns = patterns('',
    url(r'^about', views.FooterAboutView.as_view(), name='footer_about'),
    url(r'^terms', views.FooterTermView.as_view(), name='footer_terms'),
    url(r'^privacy-policy', views.FooterPrivacyView.as_view(), name='footer_privacy'),
)




