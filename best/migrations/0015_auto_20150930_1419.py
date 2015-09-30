# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('best', '0014_auto_20150922_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportstudent',
            name='quiz',
        ),
        migrations.AddField(
            model_name='reportstudent',
            name='minutes_late',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='reportstudent',
            name='notes',
            field=models.CharField(max_length=512, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='reportstudent',
            name='homework_accuracy',
            field=models.DecimalField(null=True, max_digits=3, decimal_places=1, blank=True),
        ),
    ]
