from django.db import models
from pic.models import Pic
from user.models import User
# Create your models here.

class Scrap(models.Model):
    pic_id = models.ForeignKey(Pic)
    user_id = models.ForeignKey(User)

    class Meta:
        unique_together = ('pic_id','user_id')