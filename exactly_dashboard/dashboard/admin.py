# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import OperationsModule, Dashboard


admin.site.register(Dashboard)
admin.site.register(OperationsModule)


