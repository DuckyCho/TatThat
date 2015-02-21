from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from models import SubscribeUser
from allauth.socialaccount.models import SocialApp
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
            if User.objects.filter(username=input_username) or User.objects.filter(email=input_email):
                if User.objects.filter(username=input_username) and User.objects.filter(email=input_email):
                    return render_to_response("register.html", {"isUsernameError": input_username, "isEmailError": input_email}, context_instance=RequestContext(request))
                elif User.objects.filter(email=input_email):
                    return render_to_response("register.html", {"isEmailError": input_email}, context_instance=RequestContext(request))
                else:
                    return render_to_response("register.html", {"isUsernameError": input_username}, context_instance=RequestContext(request))
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
    # app_key = SocialApp.objects.get(provider='kakao').client_id
    app_key = '61f7ff15ef036a981b3dfcdf581df848'
    redirect_uri = ''
    args={'client_id': app_key,
          'redirect_uri': 'http://localhost:8000/accounts/kakao/kakao_oauth/',
          'response_type': 'code'
    }
    url = 'https://kauth.kakao.com/oauth/authorize?'
    # request_to_kakao = requests.get(url, params=args)
    url2 = 'https://kauth.kakao.com/oauth/authorize?client_id=61f7ff15ef036a981b3dfcdf581df848&redirect_uri=http://localhost:8000/accounts/kakao/kakao_oauth/&response_type=code'
    return HttpResponseRedirect(url2)

def KaKaoOAuth(request):
    #  client_id = SocialApp.objects.get(provider='kakao').client_id
    client_id = '61f7ff15ef036a981b3dfcdf581df848'
    if request.GET:
        code = request.GET.get('code','')

    url = 'https://kauth.kakao.com/oauth/token'
    args = {'grant_type': 'authorization_code',
            'client_id': client_id,
            'redirect_uri': 'http://localhost:8000/accounts/kakao/kakao_oauth/',
            'code': code}
    get_info = requests.post(url, params=args)
    json_info = get_info.json()
    request.session['_access_token'] = json_info['access_token']
    request.session['_refresh_token'] = json_info['refresh_token']
    redirect_url = reverse('kakao_email_input')
    return HttpResponseRedirect(redirect_url)


class KaKaoEmailInput(TemplateView):
    template_name = 'kakao_email_input.html'

    def dispatch(self, request, *args, **kwargs):
        if request.POST:
            input_email = request.POST.get('email', '')
            input_last_name = request.POST.get('last_name', '')
            input_first_name = request.POST.get('first_name', '')
            subscribe = request.POST.get('subscribe', '')
            if User.objects.filter(email=input_email):
                return render_to_response("kakao_email_input.html", {"isEmailError": input_email}, context_instance=RequestContext(request))
            else:
                url = "https://kapi.kakao.com/v1/user/update_profile"
                headers = {'Authorization': 'Bearer '+request.session['_access_token'],
                           'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'}
                args = {'properties':json.dumps({'email':input_email,'last_name':input_last_name,'first_name':input_first_name})}
                user_register = requests.post(url, params=args, headers=headers)
                if user_register.status_code is 200:
                    SocialApp

                return HttpResponse(user_register.json()['id'])
        else:
            return super(KaKaoEmailInput, self).dispatch(request, *args, **kwargs)