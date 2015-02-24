# -*- coding: utf-8 -*-
from django import template
from pic.models import TagInPic, Pic
from scrap.models import Scrap
from index.models import DailyTats
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
                tags.append(tag_dtp)
        context['isDailyTats'] = 'daily'
    #태그 검색
    elif title == 'tag_search':
        if args.count is not 0:
            result = TagInPic.objects.filter(tag_id_id__in=args)
            for result_obj in result:
                pic_objs = Pic.objects.filter(id=result_obj.pic_id_id)
                for pic_obj in pic_objs:
                    if pic_obj not in pics:
                        pics.append(pic_obj)
                    tag_list = TagInPic.objects.filter(pic_id_id=pic_obj.id)[:2]
                    tags.append(tag_list)
    #스크랩북
    elif title == 'my_scrap_book':
        if args:
            result = Scrap.objects.filter(user_id=args)
            for result_obj in result:
                pic_objs = Pic.objects.filter(id=result_obj.pic_id_id)
                for pic_obj in pic_objs:
                    if pic_obj not in pics:
                        pics.append(pic_obj)
                    tag_list = TagInPic.objects.filter(pic_id_id=pic_obj.id)[:2]
                    tags.append(tag_list)
    else:
        daily_tat = DailyTats.objects.all()
        for dtp in daily_tat:
            if dtp.start <= timezone.now() <= dtp.end:
                pics.append(dtp.pic_id)
                tag_dtp = TagInPic.objects.filter(pic_id=dtp.pic_id.id)[:2]
                tags.append(tag_dtp)
        context['isDailyTats'] = 'daily'



    #문자열 검색

    if len(pics) is 0:
        if title == 'my_scrap_book':
            context['isScrapEmpty'] = True
        else:
            context['isResultEmpty'] = True
    else:
        context['pics'] = zip(pics, tags)
    return context