# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


from utils.migration import operations_sheets_to_model
from dashboard.models import Dashboard, OperationsModule
from utils.deltas import get_delta_percent, delta_to_color, make_color_scale
from utils.predict import operations_predict

from utils.modules import generate_modules
from utils.operations_modules_templates import MODULES as operations_modules


SPREADSHEET_ID = '1zY9rsgQxIwEw0vluZ1kx0V5QnH3Nc5Cw631uVJhRJjQ'
RANGE_NAME = 'operations!A:O'


@login_required
def index_view(request): 
    if request.user.is_authenticated: 
        if request.method == 'GET' and request.GET.get('dashboard'): 
            dashboard_id = request.GET.get('dashboard')

            current_dashboard = Dashboard.objects.get(pk=dashboard_id)
        else:
            current_dashboard = Dashboard.objects.get(pk=1)

        operations_sheets_to_model(OperationsModule, SPREADSHEET_ID, RANGE_NAME)

        context = {
            'modules': generate_modules(eval(current_dashboard.modules_set_name)), 
            'current_dashboard': {'name':current_dashboard.name, 'highlights':current_dashboard.highlights_name},
            'dashboards': Dashboard.objects.all()
        }
        return render(request, 'exactly_dashboard_home/index.html', context)
    return redirect("accounts:login")