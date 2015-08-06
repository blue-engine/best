# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('best', '0008_section_instructor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='content_area',
        ),
        migrations.AlterField(
            model_name='group',
            name='instructor',
            field=models.ForeignKey(verbose_name=b'BETA', to='best.Instructor'),
        ),
        migrations.AlterField(
            model_name='groupstudent',
            name='group',
            field=models.ForeignKey(related_name='group_students', to='best.Group'),
        ),
        migrations.DeleteModel(
            name='ContentArea',
        ),
    ]
