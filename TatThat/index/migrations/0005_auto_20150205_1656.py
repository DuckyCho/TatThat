# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20150205_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffpicks',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 7, 16, 56, 31, 99953, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='staffpicks',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 5, 16, 56, 31, 99920, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
