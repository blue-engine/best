# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('best', '0010_learningtarget_standard'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='report',
            options={'permissions': (('export_report', 'Export Report for Apricot'),)},
        ),
    ]
