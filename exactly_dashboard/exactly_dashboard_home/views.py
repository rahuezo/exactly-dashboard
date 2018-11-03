# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings


from utils.migration import operations_sheets_to_model
from dashboard.models import Dashboard, OperationsModule
from utils.deltas import get_delta_percent, delta_to_color
from utils.predict import operations_predict

from utils.modules import generate_modules

from utils.modulars import LeadsCard, DbCard
from utils.gsheets_connector import SheetsConnector


@login_required
def index_view(request): 
    if request.user.is_authenticated: 
        if request.method == 'GET' and request.GET.get('dashboard'):         
            dashboard_id = request.GET.get('dashboard')

            current_dashboard = Dashboard.objects.get(pk=dashboard_id)
        else:
            current_dashboard = Dashboard.objects.get(pk=1)

        # operations_sheets_to_model(OperationsModule, SPREADSHEET_ID, RANGE_NAME)

        
        leads_sheet = SheetsConnector()
        leads_sheet.get_rows(settings.SPREADSHEET_ID, settings.LEADS_RANGE_NAME)
        leads_modules = map(LeadsCard, leads_sheet.rows_to_modules())

        db_stats_sheet = SheetsConnector()
        db_stats_sheet.get_rows(settings.SPREADSHEET_ID, settings.DB_RANGE_NAME)
        db_stats_modules = generate_modules(map(DbCard, db_stats_sheet.rows_to_modules()))

        print db_stats_modules[0]
        context = {
            'leads_modules': leads_modules, #generate_modules(eval(current_dashboard.modules_set_name)), 
            'db_stats_modules': db_stats_modules, #generate_modules(eval(current_dashboard.modules_set_name)), 
            'current_dashboard': {'name':current_dashboard.name, 'highlights':current_dashboard.highlights_name},
            'dashboards': Dashboard.objects.all()
        }
        return render(request, 'exactly_dashboard_home/index.html', context)
    return redirect("accounts:login")