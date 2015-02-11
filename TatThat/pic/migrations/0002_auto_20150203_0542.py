# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pic', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailytat',
            name='pic_id',
        ),
        migrations.DeleteModel(
            name='DailyTat',
        ),
    ]
