# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('best', '0006_auto_20150723_1743'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='quiz',
        ),
        migrations.AddField(
            model_name='reportstudent',
            name='quiz',
            field=models.DecimalField(null=True, max_digits=3, decimal_places=1, blank=True),
        ),
        migrations.AlterField(
            model_name='groupstudent',
            name='date_entered',
            field=models.DateField(null=True, verbose_name=b'Date Entered', blank=True),
        ),
        migrations.AlterField(
            model_name='groupstudent',
            name='date_left',
            field=models.DateField(null=True, verbose_name=b'Date Left', blank=True),
        ),
        migrations.AlterField(
            model_name='reportstudent',
            name='exit_ticket',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
