# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-24 23:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('data_api', '0009_auto_20161124_2331'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
        migrations.DeleteModel(
            name='list_items',
        ),
    ]
