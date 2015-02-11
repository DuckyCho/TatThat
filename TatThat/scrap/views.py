from django.shortcuts import render
from django.views.generic import ListView
from models import Scrap
# Create your views here.

class ScrapCountView(ListView):
    model = Scrap
    template_name = "scrapCount.html"

    @classmethod
    def getScrapCount(cls, picId):
        objArr = Scrap.objects.filter(pic_id = picId)
        return len(objArr)

