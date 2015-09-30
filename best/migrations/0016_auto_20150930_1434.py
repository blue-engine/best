# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('best', '0015_auto_20150930_1419'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='course',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='instructor',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='learning_target',
        ),
        migrations.RemoveField(
            model_name='report',
            name='plan',
        ),
        migrations.AddField(
            model_name='report',
            name='learning_target',
            field=models.ForeignKey(blank=True, to='best.LearningTarget', null=True),
        ),
        migrations.AddField(
            model_name='section',
            name='section_length',
            field=models.IntegerField(default=30, verbose_name=b'Section Length (minutes)'),
        ),
        migrations.DeleteModel(
            name='Plan',
        ),
    ]
