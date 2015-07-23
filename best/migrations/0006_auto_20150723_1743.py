# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('best', '0005_instructor_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=256)),
                ('dosage', models.IntegerField()),
                ('exit_ticket_denominator', models.IntegerField()),
                ('homework_denominator', models.IntegerField()),
                ('quiz', models.BooleanField()),
                ('course', models.ForeignKey(to='best.Course')),
                ('instructor', models.ForeignKey(to='best.Instructor')),
                ('learning_target', models.ForeignKey(to='best.LearningTarget')),
            ],
        ),
        migrations.RemoveField(
            model_name='report',
            name='dosage',
        ),
        migrations.RemoveField(
            model_name='report',
            name='exit_ticket_denominator',
        ),
        migrations.RemoveField(
            model_name='report',
            name='homework_denominator',
        ),
        migrations.RemoveField(
            model_name='report',
            name='learning_target',
        ),
        migrations.RemoveField(
            model_name='report',
            name='quiz',
        ),
        migrations.AddField(
            model_name='report',
            name='plan',
            field=models.ForeignKey(to='best.Plan', null=True),
        ),
    ]
