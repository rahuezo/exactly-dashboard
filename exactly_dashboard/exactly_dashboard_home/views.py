# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def index_view(request): 
    context = {}
    return render(request, 'exactly_dashboard_home/index.html', context)
    