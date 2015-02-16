# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0010_auto_20150216_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffpicks',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 18, 15, 44, 54, 394828, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='staffpicks',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 16, 15, 44, 54, 394796, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
