# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-12 21:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_api', '0016_auto_20170212_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkoff_list',
            name='instance_name',
            field=models.CharField(max_length=100),
        ),
    ]
