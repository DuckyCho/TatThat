from django.views.generic import TemplateView
from django.shortcuts import render_to_response


class IndexView(TemplateView):
    template_name = 'index_page.html'


def Error500View(request):
    return render_to_response('500error.html')

