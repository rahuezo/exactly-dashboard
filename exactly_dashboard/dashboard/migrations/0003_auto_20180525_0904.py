# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-25 16:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_dashboard'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboard',
            name='highlights_name',
            field=models.CharField(default='Highlights Name', max_length=255),
        ),
        migrations.AddField(
            model_name='operationsmodule',
            name='dashboard',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Dashboard'),
        ),
        migrations.AlterField(
            model_name='operationsmodule',
            name='db_size_appended',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='operationsmodule',
            name='db_size_corporations',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='operationsmodule',
            name='db_size_email_campaign',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='operationsmodule',
            name='db_size_email_campaign_csuite',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='operationsmodule',
            name='db_size_email_campaign_marketing',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='operationsmodule',
            name='db_size_emails',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='operationsmodule',
            name='db_size_individual',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='operationsmodule',
            name='db_size_location_parsed',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='operationsmodule',
            name='db_size_location_raw',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='operationsmodule',
            name='db_size_profiles_archive',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='operationsmodule',
            name='db_size_profiles_frontend',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='operationsmodule',
            name='db_size_search_engine',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='operationsmodule',
            name='db_size_technology',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='operationsmodule',
            name='db_size_websites_processed',
            field=models.IntegerField(default=0),
        ),
    ]
