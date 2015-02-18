from django.views.generic import FormView, TemplateView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse


class LoginView(TemplateView):
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.POST:
            email = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(username=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
            return render_to_response("login.html", {"isFail": True}, context_instance=RequestContext(request))
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)





class RegisterView(TemplateView):
    template_name = 'register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.POST:
            input_email = request.POST.get('username', '')
            input_password = request.POST.get('password', '')
            input_username = request.POST.get('email', '')
            if User.objects.filter(username=input_email):
                return render_to_response("register.html", {"isEmailError": input_email}, context_instance=RequestContext(request))
            else:
                user = User.objects.create_user(username=input_email,
                                            password=input_password,
                                            email=input_username)
                user.is_active = True
                user.save()
                user = authenticate(username=input_email, password=input_password)
                login(request, user)
                return HttpResponseRedirect('/')
        else:
            return super(RegisterView, self).dispatch(request, *args, **kwargs)


def LogoutView(request):
    logout(request)
    return HttpResponseRedirect("/")
