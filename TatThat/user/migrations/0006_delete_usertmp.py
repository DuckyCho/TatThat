# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20150216_1620'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usertmp',
        ),
    ]
