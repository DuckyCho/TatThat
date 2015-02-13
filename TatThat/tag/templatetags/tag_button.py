from django import template
from pic.models import TagInPic


register = template.Library()
@register.inclusion_tag('tag_button.html')
def tag_button(picid):
    tags = {'tags':TagInPic.objects.filter(pic_id = picid)}
    return tags