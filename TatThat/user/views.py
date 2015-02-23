from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from models import SubscribeUser
from allauth.socialaccount.models import SocialAccount, SocialApp
import requests
import json


class LoginView(TemplateView):
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.POST:
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
            return render_to_response("login.html", {"isFail": True}, context_instance=RequestContext(request))
        else:
            if request.user. is_authenticated():
                return HttpResponseRedirect('/')
            else:
                return super(LoginView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        if self.request.GET.get('next', ''):
            context['redirect_field_name'] = 'next'
            context['redirect_field_value'] = self.request.GET.get('next', '')
        return context




class RegisterView(TemplateView):
    template_name = 'register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.POST:
            input_username = request.POST.get('username', '')
            input_password = request.POST.get('password', '')
            input_email = request.POST.get('email', '')
            subscribe = request.POST.get('subscribe', '')
            try:
                check_username_duplication = User.objects.get(username=input_username)
            except User.DoesNotExist:
                check_username_duplication = None
            if check_username_duplication:
                return render_to_response("register.html", {"isUsernameError": input_username}, context_instance=RequestContext(request))
            try:
                check_email_duplication = User.objects.get(email=input_email)
            except User.DoesNotExist:
                check_email_duplication = None
            if check_email_duplication:
                return render_to_response("register.html", {"isEmailError": input_email}, context_instance=RequestContext(request))
            else:
                user = User.objects.create_user(username=input_username,
                                            password=input_password,
                                            email=input_email)
                user.is_active = True
                user.save()
                user = authenticate(username=input_username, password=input_password)
                login(request, user)
                if subscribe:
                    subscriber = SubscribeUser(user_id=user)
                    subscriber.save()
                return HttpResponseRedirect('/')
        else:
            return super(RegisterView, self).dispatch(request, *args, **kwargs)


def LogoutView(request):
    logout(request)
    return HttpResponseRedirect("/")

#kakao login
def KaKaoLogin(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        client_id = SocialApp.objects.get(provider='kakao').client_id
        args={'client_id': client_id,
              'redirect_uri': 'http://localhost:8000/accounts/kakao/kakao_oauth/',
              'response_type': 'code'
        }
        url = 'https://kauth.kakao.com/oauth/authorize?client_id=%s&redirect_uri=%s&response_type=%s' % (args['client_id'], args['redirect_uri'],args['response_type'])
        return HttpResponseRedirect(url)

def GetKakaoUserInfo(access_token):
    request_url = "https://kapi.kakao.com/v1/user/me"
    headers = {"Authorization": "Bearer "+access_token,
               "Content-type": "application/x-www-form-urlencoded;charset=utf-8"}
    user_info = requests.post(request_url,headers=headers)
    user_info = user_info.json()
    if 'first_name' not in user_info['properties'] or 'last_name' not in user_info['properties'] or 'nickname' not in user_info['properties']:
        return None
    else:
        return user_info

def LoginKakaoUser(request, user_id):
    social_user = SocialAccount.objects.get(uid=user_id)
    user = User.objects.get(id=social_user.user_id)
    user.backend = "allauth.account.auth_backends.AuthenticationBackend"
    login(request, user)
    return HttpResponseRedirect('/')

def GetKakaoUserToken(request, code):
    client_id = SocialApp.objects.get(provider='kakao').client_id
    request_url = 'https://kauth.kakao.com/oauth/token'
    args = {'grant_type': 'authorization_code',
            'client_id': client_id,
            'redirect_uri': 'http://localhost:8000/accounts/kakao/kakao_oauth/',
            'code': code}
    tokens = requests.post(request_url, params=args)
    tokens = tokens.json()
    request.session['_access_token'] = tokens['access_token']
    request.session['_refresh_token'] = tokens['refresh_token']
    return tokens

def UnlinkKaKaoUser(request):
    request_url = 'https://kapi.kakao.com/v1/user/unlink'
    headers = {"Authorization": "Bearer "+request.session['_access_token']}
    unlinked_user_id = requests.post(request_url,headers=headers)
    unlinked_user_id = unlinked_user_id.json()
    social_user = SocialAccount.objects.get(uid=unlinked_user_id['id'])
    user = User.objects.get(id=social_user.user_id)
    social_user.delete()
    user.delete()
    request.session.clear()
    return HttpResponseRedirect('/')

def KaKaoOAuth(request):
    code = request.GET.get('code','')
    if code is None:
        error_url = reverse('500error')
        return HttpResponseRedirect(error_url)
    tokens = GetKakaoUserToken(request, code)
    user_info = GetKakaoUserInfo(tokens['access_token'])
    if user_info is None:
        redirect_url = reverse('kakao_email_input')
        return HttpResponseRedirect(redirect_url)
    else:
        return LoginKakaoUser(request, user_info['id'])

def UpdateKakaoUser(access_token, properties):
    request_url = "https://kapi.kakao.com/v1/user/update_profile"
    headers = {'Authorization': 'Bearer '+access_token,
                'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'}
    args = {'properties': properties}
    json_user_id = requests.post(request_url, params=args, headers=headers)
    if json_user_id.status_code is 200:
        return json_user_id
    else:
        return None

class KaKaoEmailInput(TemplateView):
    template_name = 'kakao_email_input.html'

    def dispatch(self, request, *args, **kwargs):
        if request.POST:
            input_email = request.POST.get('email', '')
            input_last_name = request.POST.get('last_name', '')
            input_first_name = request.POST.get('first_name', '')
            input_nickname = request.POST.get('username', '')
            subscribe = request.POST.get('subscribe', '')

            try:
                check_username_duplication = User.objects.get(username=input_nickname)
            except User.DoesNotExist:
                check_username_duplication = None
            if check_username_duplication:
                return render_to_response("kakao_email_input.html", {"isUsernameError": input_nickname}, context_instance=RequestContext(request))
            try:
                check_email_duplication = User.objects.get(email=input_email)
            except User.DoesNotExist:
                check_email_duplication = None
            if check_email_duplication:
                return render_to_response("kakao_email_input.html", {"isEmailError": input_email}, context_instance=RequestContext(request))
            else:
                properties= json.dumps({'email': input_email, 'last_name': input_last_name, 'first_name': input_first_name, 'nickname': input_nickname})
                json_user_id = UpdateKakaoUser(request.session['_access_token'],properties)
                if json_user_id is None:
                    error_url = reverse('500error')
                    return HttpResponseRedirect(error_url)
                user_info = GetKakaoUserInfo(request.session['_access_token'])
                username = user_info['properties']['nickname']
                new_user = User.objects.create(username=username, email=input_email, first_name=input_first_name, last_name=input_last_name,)
                User.set_unusable_password(new_user)
                new_user.save()
                new_user = User.objects.get(username=username)

                user_info['access_token'] = request.session['_access_token']
                user_info['refresh_token'] = request.session['_refresh_token']
                new_social_user = SocialAccount.objects.create(provider='kakao', uid=user_info['id'], extra_data=user_info, user_id=new_user.id)
                new_social_user.save()

                if subscribe:
                    subscriber = SubscribeUser(user_id=new_user)
                    subscriber.save()

                return LoginKakaoUser(request, user_info['id'])
        else:
            return super(KaKaoEmailInput, self).dispatch(request, *args, **kwargs)


