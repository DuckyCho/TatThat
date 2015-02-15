from django.views.generic import DetailView
from pic.models import Pic
from django.core.urlresolvers import reverse


class PicDetailView(DetailView):
    model = Pic
    template_name = 'picDetailView.html'

    def get_context_data(self, **kwargs):
        context = super(PicDetailView, self).get_context_data(**kwargs)
        current_url = self.request.path_info
        if 'daily' in current_url:
            context['daily'] = True
        return context

    def get_success_url(self):
        return reverse('searchResult')




