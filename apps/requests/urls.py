# -*- coding: utf-8 -*-

"""
This file contains url mappings for the requests app
"""
from django.conf.urls import patterns, url

from apps.requests.views import Requests

urlpatterns = patterns(
    'apps.requests.views',
    url(r'^$', Requests.as_view(), name='requests'),
    url(
        r'^xhr/get_notifications/(?P<last_request>\d+)',
        'get_request_notification',
        name='rq_notifications'
    )
)
