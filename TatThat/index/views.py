from django.views.generic import ListView
from models import DailyTats, StaffPicks
from pic.models import TagInPic
from pic.models import Pic
from django.utils import timezone
from django.template.loader import render_to_string
from PIL import Image

# Create your views here.

class IndexView(ListView):
    template_name = 'index_page.html'

    def get_queryset(self):
        return None

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        #Get Staff Pick HTML
        staff_pick_obj = StaffPicks.objects.all()
        object_list = []
        for obj in staff_pick_obj:
             if(obj.start <= timezone.now() <= obj.end):
                 object_list.append(obj)
        context["staff_pick_contents"] = render_to_string("staff_pick.html",{'object_list':object_list})

        #Get Daily Tats HTML
        daily_tat_pics = DailyTats.objects.all()
        allInfo = []
        for dtp in daily_tat_pics:
            if dtp.start <= timezone.now() <= dtp.end:
                picInfo = {}
                picInfo["tags"] = TagInPic.objects.filter(pic_id = dtp.pic_id)
                picObj = Pic.objects.filter(id = dtp.pic_id_id)
                picInfo["id"] = picObj[0].id
                picInfo["url"] = picObj[0].url
                allInfo.append(picInfo)
        context["daily_tat_contents"] = render_to_string("daily_tats.html",{'picInfos':allInfo})

        return context


