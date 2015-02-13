#!/usr/bin/python
# -*- coding: UTF8 -*-
from django import template
from scrap.models import Scrap


register = template.Library()
@register.inclusion_tag('scrap_count.html')
def scrap_count(pid):
    context = {}
    scraped = Scrap.objects.filter(pic_id_id=pid)
    count = len(scraped)
    context['scrap_count']=count
    return context