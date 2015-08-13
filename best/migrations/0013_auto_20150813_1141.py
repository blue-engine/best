# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('best', '0012_auto_20150806_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='alt_learning_target',
            field=models.CharField(help_text=b'Only use when not selecting a pre-defined learning target', max_length=256, null=True, verbose_name=b'Alt Learning Target', blank=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='learning_target',
            field=models.ForeignKey(blank=True, to='best.LearningTarget', null=True),
        ),
    ]
