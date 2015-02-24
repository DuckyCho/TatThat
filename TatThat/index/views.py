from django.views.generic import TemplateView
from django.shortcuts import render_to_response
from django.template import RequestContext


class IndexView(TemplateView):
    template_name = 'index_page.html'


def Error400View(request):
    return render_to_response('400error.html',context_instance=RequestContext(request))


def Error403View(request):
    return render_to_response('403error.html',context_instance=RequestContext(request))


def Error404View(request):
    return render_to_response('404error.html',context_instance=RequestContext(request))


def Error500View(request):
    return render_to_response('500error.html',context_instance=RequestContext(request))
