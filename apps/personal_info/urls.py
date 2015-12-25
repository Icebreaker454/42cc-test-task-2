# -*- coding: utf-8 -*-

"""
This file contains url mappings for the personal_info app
"""
from django.conf.urls import patterns, url

from apps.personal_info.views import Home

urlpatterns = patterns(
    '',

    url(r'^$', Home.as_view(), name='home')
)
