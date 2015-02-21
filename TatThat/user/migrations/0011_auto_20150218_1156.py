# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0010_auto_20150216_1643'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscribeUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        # migrations.RemoveField(
        #     model_name='tatthatuser',
        #     name='user',
        # ),
        # migrations.DeleteModel(
        #     name='TatThatUser',
        # ),
    ]
