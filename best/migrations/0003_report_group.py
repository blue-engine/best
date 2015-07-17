# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('best', '0002_report_exported'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='group',
            field=models.ForeignKey(default=1, to='best.Group'),
            preserve_default=False,
        ),
    ]
