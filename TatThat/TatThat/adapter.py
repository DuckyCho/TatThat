from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter

class TatThatAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        return '/user/login'
    def get_logout_redirect_url(self, request):
        return '/user/logout'