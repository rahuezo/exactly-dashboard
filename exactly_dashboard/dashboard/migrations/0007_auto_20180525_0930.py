# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-25 16:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20180525_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operationsmodule',
            name='dashboard',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='modules_set', to='dashboard.Dashboard'),
        ),
    ]
