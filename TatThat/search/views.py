from django.views.generic import ListView
from tag.models import TagCatag, Tag
from django.template.loader import render_to_string

class SearchMainView(ListView):
    model = TagCatag
    template_name = "searchMain.html"

    def get_context_data(self, **kwargs):
        catag_tag_list = []
        context = {}
        catag_list = TagCatag.objects.all()
        for category in catag_list:
            catag_tag_set = {}
            tags = Tag.objects.filter(catag = category)
            catag_tag_set["catag"] = category
            catag_tag_set["tag_list"] = tags
            catag_tag_list.append(catag_tag_set)
        context['tag_list_contents'] = render_to_string("tagListInCatag.html",{'catag_tag_list':catag_tag_list})
        return context

