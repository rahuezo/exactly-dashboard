# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from utils.migration import operations_sheets_to_model
from dashboard.models import OperationsModule
from utils.deltas import get_delta_percent, delta_to_color, make_color_scale
from utils.predict import operations_predict

from utils.modules import generate_modules


SPREADSHEET_ID = '1zY9rsgQxIwEw0vluZ1kx0V5QnH3Nc5Cw631uVJhRJjQ'
RANGE_NAME = 'test!A:O'


def index_view(request): 
    
    operations_sheets_to_model(OperationsModule, SPREADSHEET_ID, RANGE_NAME)
    current_record = OperationsModule.objects.last()
    last_record = OperationsModule.objects.get(pk=current_record.pk - 1).db_size_profiles_archive
    next_delta = operations_predict([om.db_size_profiles_archive for om in OperationsModule.objects.all()])

    context = {
        'modules': generate_modules(), 
        'scale': make_color_scale(), 
        'dashboards': sorted(['Operations', 'Sales', 'Marketing', 'Email Campaigns'])
    }
    return render(request, 'exactly_dashboard_home/index.html', context)
    