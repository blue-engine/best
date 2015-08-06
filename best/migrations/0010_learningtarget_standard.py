# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('best', '0009_auto_20150806_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='learningtarget',
            name='standard',
            field=models.ForeignKey(blank=True, to='best.Standard', null=True),
        ),
    ]
