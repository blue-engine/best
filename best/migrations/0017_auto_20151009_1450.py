# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('best', '0016_auto_20150930_1434'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='report',
            options={'verbose_name': 'Record', 'verbose_name_plural': 'Records', 'permissions': (('export_report', 'Export Report for Apricot'),)},
        ),
        migrations.AlterField(
            model_name='report',
            name='learning_target',
            field=models.ForeignKey(to='best.LearningTarget', null=True),
        ),
        migrations.AlterField(
            model_name='reportstudent',
            name='homework_accuracy',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=1, blank=True),
        ),
        migrations.AlterField(
            model_name='reportstudent',
            name='minutes_late',
            field=models.IntegerField(null=True, verbose_name=b'Minutes out of class', blank=True),
        ),
    ]
