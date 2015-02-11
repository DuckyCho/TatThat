from django.db import models
from tag.models import Tag


class Pic(models.Model):
    url = models.CharField(
        max_length=200,
    )

    def __str__(self):
        return str(self.id)+" / "+str(self.url)


class TagInPic(models.Model):
    pic_id = models.ForeignKey(Pic)
    tag_id = models.ForeignKey(Tag)

    def __str__(self):
        return str(self.tag_id)


