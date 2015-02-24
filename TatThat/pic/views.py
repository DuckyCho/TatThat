from django.views.generic import DetailView
from pic.models import Pic
from scrap.models import Scrap


class PicDetailView(DetailView):
    model = Pic
    template_name = 'picDetailView.html'

    def get_context_data(self, **kwargs):
        context = super(PicDetailView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            try:
                isAlreadyScraped = Scrap.objects.get(user_id=self.request.user.id, pic_id=self.get_object())
            except Scrap.DoesNotExist:
                isAlreadyScraped = None
            except Scrap.MultipleObjectsReturned:
                isAlreadyScraped = True
            if isAlreadyScraped:
                context['isAlreadyScraped'] = True
        current_url = self.request.path_info
        if 'daily' in current_url:
            context['daily'] = True
        return context





