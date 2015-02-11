# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pic', '0002_auto_20150203_0542'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scrap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pic_id', models.ForeignKey(to='pic.Pic')),
                ('user_id', models.ForeignKey(to='user.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
