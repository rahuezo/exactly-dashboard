# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-30 22:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_auto_20181030_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operationsmodule',
            name='dashboard',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='modules_set', to='dashboard.Dashboard'),
        ),
    ]
