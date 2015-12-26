# -*- coding: utf-8 -*-

"""
This file contains url mappings for the requests app
"""
from django.conf.urls import patterns, url

from apps.requests.views import Requests

urlpatterns = patterns(
    '',
    url(r'^$', Requests.as_view(), name='requests')
)
