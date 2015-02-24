# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0006_auto_20150216_1643'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='scrap',
            unique_together=set([('pic_id', 'user_id')]),
        ),
    ]
