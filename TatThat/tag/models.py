from django.db import models

# Create your models here.


class TagCatag(models.Model):
    id = models.CharField(
        max_length=40,
        primary_key=True,
    )

    def __str__(self):
        return self.id.encode("UTF-8")

class Tag(models.Model):
    id = models.CharField(
        max_length=40,
        primary_key=True,
    )
    catag = models.ForeignKey(TagCatag)

    def __str__(self):
        return self.id.encode("UTF-8")

    class meta:
        ordering = ['catag']




