# -*- coding: utf-8 -*-

"""
This file contains views for the requests
application
"""
import json
import logging


from django.core import serializers
from django.views.generic import ListView
from django.http import HttpResponse
from django.http import HttpResponseBadRequest

from apps.requests.models import WebRequest

logger = logging.getLogger('requests')


class Requests(ListView):
    """ The requests class-based view """
    context_object_name = 'requests'
    template_name = 'requests/all.html'

    def get_queryset(self, *args, **kwargs):
        """ Return the queryset for the model """
        queryset = WebRequest.objects.order_by('-time')[:10]
        if not self.request.is_ajax():
            logger.info('Processing request: %s' % self.request)
            logger.debug('Queryset: %s' % queryset)
        return queryset


def get_request_notification(request, last_request):
    """ AJAX view to get the number of unread requests """
    if not request.is_ajax():
        logger.error('Direct HTTP request to an ajax view')
        return HttpResponseBadRequest(
            '<h1>Direct HTTP request is not allowed</h1>'
        )

    if request.method != 'GET':
        logger.error('The GET processing view got non-GET request')
        return HttpResponseBadRequest(
            json.dumps({
                'status': 'error',
                'error_message': 'Only GET requests are allowed'
            }),
            content_type='application/json'
        )

    count = WebRequest.objects.filter(
        id__gt=last_request
    ).count()

    queryset = WebRequest.objects.order_by('-time')[:10]

    logger.debug('AJAX requests notification count: %s' % count)
    return HttpResponse(
        json.dumps({
            'status': 'success',
            'count': count,
            'queryset': serializers.serialize('json', queryset)
        }),
        content_type='application/json'
    )
