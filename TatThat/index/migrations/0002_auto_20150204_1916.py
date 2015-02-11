# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffpicks',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 6, 19, 16, 23, 817596, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='staffpicks',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 4, 19, 16, 23, 817549, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
