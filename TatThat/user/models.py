from django.db import models
from django.contrib.auth.models import User

class SubscribeUser(models.Model):
    user_id = models.ForeignKey(User)
