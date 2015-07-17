# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContentArea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=256)),
                ('content_area', models.ForeignKey(to='best.ContentArea')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='GroupStudent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_entered', models.DateField(verbose_name=b'Date Entered')),
                ('date_left', models.DateField(null=True, verbose_name=b'Date Left')),
                ('group', models.ForeignKey(to='best.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='LearningTarget',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('quarter', models.IntegerField()),
                ('week', models.IntegerField()),
                ('dosage', models.IntegerField()),
                ('exit_ticket_denominator', models.IntegerField()),
                ('homework_denominator', models.IntegerField()),
                ('quiz', models.BooleanField()),
                ('learning_target', models.ForeignKey(to='best.LearningTarget')),
            ],
        ),
        migrations.CreateModel(
            name='ReportStudent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attendance', models.IntegerField(choices=[(0, b'Present'), (1, b'Absent'), (2, b'Tardy')])),
                ('exit_ticket', models.IntegerField(null=True)),
                ('homework_effort', models.IntegerField(choices=[(0, b'Excused/No HW'), (1, b'Yes'), (2, b'No')])),
                ('homework_accuracy', models.DecimalField(max_digits=3, decimal_places=1)),
                ('report', models.ForeignKey(to='best.Report')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=256)),
                ('year_code', models.CharField(max_length=32)),
                ('semester_code', models.CharField(max_length=32)),
                ('course', models.ForeignKey(to='best.Course')),
                ('school', models.ForeignKey(to='best.School')),
            ],
        ),
        migrations.CreateModel(
            name='Standard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=256)),
                ('course', models.ForeignKey(to='best.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('osis_number', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=128)),
                ('school', models.ForeignKey(to='best.School')),
            ],
        ),
        migrations.AddField(
            model_name='reportstudent',
            name='student',
            field=models.ForeignKey(to='best.Student'),
        ),
        migrations.AddField(
            model_name='instructor',
            name='school',
            field=models.ForeignKey(to='best.School'),
        ),
        migrations.AddField(
            model_name='groupstudent',
            name='student',
            field=models.ForeignKey(to='best.Student'),
        ),
        migrations.AddField(
            model_name='group',
            name='instructor',
            field=models.ForeignKey(to='best.Instructor'),
        ),
        migrations.AddField(
            model_name='group',
            name='section',
            field=models.ForeignKey(to='best.Section'),
        ),
    ]
