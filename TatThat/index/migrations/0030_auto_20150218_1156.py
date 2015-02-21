# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0029_auto_20150216_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffpicks',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 20, 11, 56, 38, 566747, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='staffpicks',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 18, 11, 56, 38, 566714, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
