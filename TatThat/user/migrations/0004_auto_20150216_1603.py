# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20150216_1553'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Usertmp',
        ),
    ]
