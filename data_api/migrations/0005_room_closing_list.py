# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-12 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_api', '0004_auto_20161112_0511'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='closing_list',
            field=models.ManyToManyField(to='data_api.Checklist_item'),
        ),
    ]
