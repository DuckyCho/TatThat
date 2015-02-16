# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0002_auto_20150205_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrap',
            name='user_id',
            field=models.ForeignKey(to='user.TatThatUser'),
            preserve_default=True,
        ),
    ]
