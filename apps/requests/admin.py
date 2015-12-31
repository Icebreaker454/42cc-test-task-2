# -*- coding: utf-8 -*-

"""
This module cnontains models registration for the requests app
on the admin site
"""

from django.contrib import admin

from apps.requests.models import WebRequest


admin.site.register(WebRequest)
