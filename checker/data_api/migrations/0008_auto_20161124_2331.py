# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-24 23:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_api', '0007_auto_20161124_2258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkoff_list',
            name='completed_bool',
        ),
        migrations.RemoveField(
            model_name='checkoff_list',
            name='list_itemID',
        ),
        migrations.AddField(
            model_name='checkoff_list',
            name='task_completedlist',
            field=models.ManyToManyField(related_name='task_completed_list', to='data_api.Checklist_item'),
        ),
        migrations.AddField(
            model_name='checkoff_list',
            name='task_list',
            field=models.ManyToManyField(related_name='task_list', to='data_api.Checklist_item'),
        ),
        migrations.AlterField(
            model_name='checkoff_list',
            name='issueReport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_api.Issue_report', verbose_name='issueid'),
        ),
        migrations.AlterField(
            model_name='checkoff_list',
            name='roomID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_api.Room', verbose_name='roomid'),
        ),
        migrations.AlterField(
            model_name='issue_report',
            name='issueID',
            field=models.IntegerField(verbose_name='issueid'),
        ),
        migrations.AlterField(
            model_name='room',
            name='roomID',
            field=models.IntegerField(verbose_name='roomid'),
        ),
    ]
