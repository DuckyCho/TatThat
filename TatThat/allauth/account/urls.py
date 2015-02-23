from django.conf.urls import patterns, url
from django.views.generic import RedirectView
from user.views import LoginView,RegisterView
from django.conf.urls import url, patterns, include
from user import urls
from . import views

urlpatterns = patterns(
    "",
    url(r"^$", views.AccountIndexView.as_view(), name='account_index'),
    # url(r"^signup/$", views.signup, name="account_signup"),
    # url(r"^login/$", views.login, name="account_login"),
    url(r"^logout/$", views.logout, name="account_logout"),

    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^signup/$', RegisterView.as_view(), name='register'),
    # url(r'^fb_login/$', views.FBLoginView.as_view(), name='facebook_login'),
    url(r"^password/change/social/$", views.PasswordChangeSocial.as_view(), name='account_social_user_change_password'),
    url(r"^password/change/$", views.password_change, name="account_change_password"),
    url(r"^kakao/", include(urls)),
    url(r"^valid-check", views.valid_check, name="valid_check"),
    # url(r"^password/set/$", views.password_set, name="account_set_password"),
    #
    # url(r"^inactive/$", views.account_inactive, name="account_inactive"),
    #
    # # E-mail
    # url(r"^email/$", views.email, name="account_email"),
    # url(r"^confirm-email/$", views.email_verification_sent,
    #     name="account_email_verification_sent"),
    # url(r"^confirm-email/(?P<key>\w+)/$", views.confirm_email,
    #     name="account_confirm_email"),
    # # Handle old redirects
    # url(r"^confirm_email/(?P<key>\w+)/$",
    #     RedirectView.as_view(url='/accounts/confirm-email/%(key)s/',
    #                          permanent=True)),
    #
    # # password reset
    # url(r"^password/reset/$", views.password_reset,
    #     name="account_reset_password"),
    # url(r"^password/reset/done/$", views.password_reset_done,
    #     name="account_reset_password_done"),
    # url(r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
    #     views.password_reset_from_key,
    #     name="account_reset_password_from_key"),
    # url(r"^password/reset/key/done/$", views.password_reset_from_key_done,
    #     name="account_reset_password_from_key_done"),
)
