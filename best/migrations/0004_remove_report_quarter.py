# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('best', '0003_report_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='quarter',
        ),
    ]
