# -*- coding: utf-8 -*-

"""
This module cnontains models registration for the personal_info app
on the admin site
"""

from django.contrib import admin

from apps.personal_info.models import Person
# Register your models here.

admin.site.register(Person)
