from django.views.generic import FormView, TemplateView
from django import forms
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse


class LoginView(TemplateView):
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.POST:
            email = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=email, password=password)
            if user is not None:
                if user.is_active:
                    return HttpResponse('is active')
            return render_to_response("login.html", {"isFail": True}, context_instance=RequestContext(request))
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)





class RegisterView(TemplateView):
    template_name = 'register.html'

    def get_success_url(self):
        return reverse('index')



# class LogoutView(TemplateView):
