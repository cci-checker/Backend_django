# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-12 05:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('data_api', '0003_auto_20161112_0211'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkoff_list',
            name='sometext',
            field=models.CharField(default=datetime.datetime(2016, 11, 12, 5, 11, 35, 540270, tzinfo=utc), max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='checkoff_list',
            name='issueReport',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='checkoff_list',
            name='list_itemID',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='checkoff_list',
            name='roomID',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='checkoff_list',
            name='studentUID',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='issue_report',
            name='comment',
            field=models.CharField(max_length=1000),
        ),
        migrations.RemoveField(
            model_name='room',
            name='opening_list',
        ),
        migrations.AddField(
            model_name='room',
            name='opening_list',
            field=models.CharField(default=datetime.datetime(2016, 11, 12, 5, 11, 44, 906261, tzinfo=utc), max_length=1000),
            preserve_default=False,
        ),
    ]
