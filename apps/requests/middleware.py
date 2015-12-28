# -*- coding: utf-8 -*-

"""
    This module contains middleware for the purposes
    of the requests application
"""

from apps.requests.models import WebRequest


class RequestSavingMiddleware(object):
    """ This is the midleware class itself """
    def process_response(self, request, response):
        """ This is the overriden process_request method to save
            all incoming HTTP requests in WebRequest models """
        WebRequest.objects.create(
            path=request.build_absolute_uri(),
            method=request.method,
            status_code=response.status_code,
            user_agent=request.META.copy().pop('HTTP_USER_AGENT', None),
            is_secure=request.is_secure(),
            is_ajax=request.is_ajax()
        )
        return response
