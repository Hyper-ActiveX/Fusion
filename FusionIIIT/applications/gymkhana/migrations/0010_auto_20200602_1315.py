# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-06-02 13:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gymkhana', '0009_auto_20200602_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='voting_polls',
            name='created_by',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='voting_polls',
            name='exp_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
