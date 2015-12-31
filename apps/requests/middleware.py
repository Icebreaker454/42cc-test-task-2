# -*- coding: utf-8 -*-

"""
    This module contains middleware for the purposes
    of the requests application
"""
from django.core.urlresolvers import reverse

from apps.requests.models import WebRequest


class RequestSavingMiddleware(object):
    """ This is the midleware class itself """
    def process_request(self, request):
        """ This is the overriden process_request method to save
            all incoming HTTP requests in WebRequest models """
        if '/xhr/get_notifications' in request.path:
            return
        if request.path == reverse('requests') and request.is_ajax():
            return
        WebRequest.objects.create(
            path=request.build_absolute_uri(),
            method=request.method,
            user_agent=request.META.copy().pop('HTTP_USER_AGENT', None),
            is_secure=request.is_secure(),
            is_ajax=request.is_ajax()
        )
