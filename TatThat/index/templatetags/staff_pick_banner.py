#!/usr/bin/python
# -*- coding: UTF8 -*-
from django import template
from index.models import StaffPicks
from django.utils import timezone

register = template.Library()
@register.inclusion_tag('staff_pick_banner.html')
def staff_pick_banner():
    context = {}
    staff_pick = StaffPicks.objects.all()
    valid_list = []
    for pic in staff_pick:
         if pic.start <= timezone.now() <= pic.end:
             valid_list.append(pic)
    context['staff_picks'] = valid_list
    return context