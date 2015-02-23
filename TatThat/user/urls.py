from django.conf.urls import patterns, url
from user import views

#kakao url
urlpatterns = patterns('',
        url(r'^login/$', views.KaKaoLogin, name='kakao_login' ),
        url(r'^kakao_oauth/$', views.KaKaoOAuth, name='kakao_OAuth' ),
        url(r'^kakao_email/$', views.KaKaoEmailInput.as_view(), name='kakao_email_input'),
        url(r'^kakao_unlink/$', views.UnlinkKaKaoUser, name='kakao_unlink'),
)
