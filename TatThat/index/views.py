from django.views.generic import TemplateView
from PIL import Image

class IndexView(TemplateView):
    template_name = 'index_page.html'


