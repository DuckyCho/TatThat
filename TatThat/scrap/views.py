# -*- coding: utf-8 -*-
from django.http.response import HttpResponse
from models import Scrap
from django.contrib.auth.models import User
from pic.models import Pic
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView

def addScrap(request):

    if request.user.is_authenticated():
        user_id = request.user.id
        pic_id = request.GET.get('pic_id', '')
        try:
            pic = Pic.objects.get(id=pic_id)
        except Pic.DoesNotExist:
            pic = None
        try:
            user = User.objects.get(id=user_id)
        except:
            user = None
        new_scrap = Scrap(user_id=user, pic_id=pic)
        new_scrap.save()
        return HttpResponse(Scrap.objects.filter(pic_id=pic).count())
    else:
        return render_to_response('400error.html',context_instance=RequestContext(request))


def removeScrap(request):
    if request.user.is_authenticated():
        user_id = request.user.id
        pic_id = request.GET.get('pic_id', '')
        try:
            pic = Pic.objects.get(id=pic_id)
        except Pic.DoesNotExist:
            pic = None
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            user = None
        try:
            scrap = Scrap.objects.get(user_id=user, pic_id=pic)
        except Scrap.DoesNotExist:
            scrap = None
        if scrap:
            scrap.delete()
        return HttpResponse(Scrap.objects.filter(pic_id=pic).count())
    else:
        return render_to_response('400error.html',context_instance=RequestContext(request))


class MyScrapBookView(TemplateView):
    template_name = "my_scrap_book.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return super(MyScrapBookView, self).dispatch(request, *args, **kwargs)
        else:
            return render_to_response('400error.html',context_instance=RequestContext(request))

