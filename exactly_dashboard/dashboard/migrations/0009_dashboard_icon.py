# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-25 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_dashboard_modules_set_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboard',
            name='icon',
            field=models.CharField(default='<i class="fas fa-cogs"></i>', max_length=255),
        ),
    ]
