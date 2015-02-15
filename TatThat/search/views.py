# -*- coding: utf-8 -*-
from django.views.generic import ListView
from tag.models import TagCatag, Tag
from django.template.loader import render_to_string
import re
import urllib2


class SearchMainView(ListView):
    model = TagCatag
    template_name = "searchMain.html"

    def get_context_data(self, **kwargs):
        context = super(SearchMainView, self).get_context_data(**kwargs)
        catag_tag_list = []
        catag_list = TagCatag.objects.all()
        for category in catag_list:
            catag_tag_set = {}
            tags = Tag.objects.filter(catag = category)
            catag_tag_set["catag"] = category
            catag_tag_set["tag_list"] = tags
            catag_tag_list.append(catag_tag_set)
        context['tag_list_contents'] = render_to_string("tagListInCatag.html",{'catag_tag_list':catag_tag_list})
        return context


class TagSearchResultView(SearchMainView):
    model = TagCatag
    template_name = "search_result.html"

    def get_context_data(self, **kwargs):
        context = super(TagSearchResultView, self).get_context_data(**kwargs)
        current_url = self.request.path_info
        pattern = '^/search/tag/(.*)'
        args_str = re.match(pattern,current_url).group(1)
        args_list = args_str.split('+')
        args_list_decoded = []

        for arg in args_list:
            new_arg = urllib2.unquote(arg)
            args_list_decoded.append(new_arg)

        context['title'] = 'tag_search'
        context['args'] = args_list_decoded
        context['isTagSearchResult'] = True

        return context
