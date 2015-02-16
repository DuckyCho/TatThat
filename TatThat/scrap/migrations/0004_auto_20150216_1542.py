# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0003_auto_20150216_1536'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='scrap',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='scrap',
            name='user_id',
        ),
    ]
