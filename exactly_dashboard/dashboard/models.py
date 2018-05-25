# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Dashboard(models.Model): 
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255, default='<i class="fas fa-cogs"></i>')
    modules_set_name = models.CharField(max_length=255)
    highlights_name = models.CharField(max_length=255, default="Highlights Name")
    
    def __str__(self): 
        return '{}'.format(self.name.lower())


class OperationsModule(models.Model): 
    dashboard = models.ForeignKey(Dashboard, related_name='modules_set', default=0)
    date = models.DateField()
    db_size_profiles_archive = models.IntegerField(default=0)
    db_size_profiles_frontend = models.IntegerField(default=0)
    db_size_individual = models.IntegerField(default=0)
    db_size_location_raw = models.IntegerField(default=0)
    db_size_location_parsed = models.IntegerField(default=0)
    db_size_emails = models.IntegerField(default=0)
    db_size_search_engine = models.IntegerField(default=0)
    db_size_corporations = models.IntegerField(default=0)
    db_size_technology = models.IntegerField(default=0)
    db_size_websites_processed = models.IntegerField(default=0)
    db_size_appended = models.IntegerField(default=0)
    db_size_email_campaign = models.IntegerField(default=0)
    db_size_email_campaign_marketing = models.IntegerField(default=0)
    db_size_email_campaign_csuite = models.IntegerField(default=0)

    def __str__(self): 
        return '{}'.format(self.date)

