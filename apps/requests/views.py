# -*- coding: utf-8 -*-

"""
This file contains views for the requests
application
"""
from django.views.generic import ListView

from apps.requests.models import WebRequest


class Requests(ListView):
    """ The requests class-based view """
    context_object_name = 'requests'
    template_name = 'requests/all.html'

    def get_queryset(self, *args, **kwargs):
        """ Return the queryset for the model """
        return WebRequest.objects.order_by('-time')[:10]
