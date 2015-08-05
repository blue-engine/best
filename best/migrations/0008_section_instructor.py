# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('best', '0007_auto_20150723_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='instructor',
            field=models.ForeignKey(to='best.Instructor', null=True),
        ),
    ]
