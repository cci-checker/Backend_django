# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-12 21:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_api', '0015_remove_checkoff_list_checkoff_listid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkoff_list',
            old_name='sometext',
            new_name='instance_name',
        ),
    ]
