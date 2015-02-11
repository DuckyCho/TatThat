from django.db import models
from pic.models import Pic,TagInPic
from django.utils import timezone
# Create your models here.


class StaffPicks(models.Model):
    path = models.CharField(
        max_length=100,
    )
    caption = models.CharField(
        max_length=40,
    )
    start = models.DateTimeField(default=timezone.now())
    end = models.DateTimeField(default=timezone.now()+timezone.timedelta(days=30))

    def __str__(self):
        return self.caption

class DailyTats(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    pic_id = models.ForeignKey(Pic)

    def __str__(self):
        return str(self.pic_id)+" / "+str(self.start)+" / "+str(self.end)
