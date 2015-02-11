from django.views.generic import DetailView
from pic.models import Pic, TagInPic
from scrap.views import ScrapCountView
class PicDetailView(DetailView):
    model = Pic
    template_name = 'picDetailView.html'

    def get_context_data(self, **kwargs):
        context = super(PicDetailView, self).get_context_data(**kwargs)
        pic_id_from_request = self.kwargs['pk']
        if 'daily':
            context['daily'] = True
        context['tags'] = TagInPic.objects.filter(pic_id = pic_id_from_request)
        context['scrap_count'] = ScrapCountView.getScrapCount(pic_id_from_request)
        return context





