from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index_page.html'
    #
    # def get_context_data(self, **kwargs):
    #     context = super(IndexView, self).get_context_data(**kwargs)
    #     if self.request.user.is_authenticated():
    #         context['isAuthUser'] = True
    #     else:
    #         context['isAuthUser'] = False
    #
    #     return context



