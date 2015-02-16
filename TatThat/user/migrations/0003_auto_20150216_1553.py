# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20150216_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='TatThatUser',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.RemoveField(
            model_name='TatThatUser',
            name='id',
        ),
        migrations.AlterField(
            model_name='TatThatUser',
            name='user',
            field=models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
