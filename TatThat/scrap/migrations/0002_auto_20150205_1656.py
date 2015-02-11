# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='scrap',
            unique_together=set([('pic_id', 'user_id')]),
        ),
    ]
