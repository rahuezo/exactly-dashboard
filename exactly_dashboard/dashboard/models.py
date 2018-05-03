# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models





class Dashboard(models.Model): 
    name = models.CharField(max_length=255)

    def __str__(self): 
        return self.name


class OperationsModule(models.Model): 
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

    def db_size_profiles_total(self): 
        return self.db_size_profiles_archive + self.db_size_profiles_frontend + self.db_size_individual


    def db_size_profiles_delta(self): 
        if OperationsModule.objects.count() >= 2: 
            last_record = OperationsModule.objects.filter(date__lt=self.date).last()

            print last_record.db_size_profiles_archive, last_record.date, last_record.pk
            
            return 'Delta: ', self.db_size_profiles_archive - last_record.db_size_profiles_archive
        return 0 


    def __str__(self): 
        return '{}'.format(self.date)

