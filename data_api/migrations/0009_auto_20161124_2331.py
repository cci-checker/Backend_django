# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-24 23:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_api', '0008_auto_20161124_2331'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkoff_list',
            old_name='checkoff_itemID',
            new_name='checkoff_listID',
        ),
    ]
