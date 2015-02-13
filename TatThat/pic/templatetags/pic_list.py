#!/usr/bin/python
# -*- coding: UTF8 -*-
from django import template
from pic.models import Pic, TagInPic
from index.models import DailyTats
from tag.models import Tag
from django.utils import timezone

register = template.Library()
@register.inclusion_tag('pic_list.html')
def pic_list(title,args):
    context = {}
    pics = []
    tags = []
    if title == 'dailyTats':
        daily_tat = DailyTats.objects.all()
        for dtp in daily_tat:
            if dtp.start <= timezone.now() <= dtp.end:
                pics.append(dtp.pic_id)
                tag_dtp = TagInPic.objects.filter(pic_id=dtp.pic_id.id)[:2]
                for tag in tag_dtp:
                    tags.append(tag.tag_id)
        context['isDailyTats'] = 'daily'
    #태그 검색


    #문자열 검색

    context['pics'] = pics
    context['tags'] = tags
    return context