# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('best', '0011_auto_20150806_2023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructor',
            name='email',
        ),
        migrations.RemoveField(
            model_name='instructor',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='instructor',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='instructor',
            name='user',
            field=models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
