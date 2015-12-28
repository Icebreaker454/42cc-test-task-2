# -*- coding: utf-8 -*-

"""
This file contains views for the requests
application
"""
from datetime import datetime

from django.views.generic import ListView


class Requests(ListView):
    """ The requests class-based view """
    context_object_name = 'requests'
    template_name = 'requests/all.html'

    def get_queryset(self, *args, **kwargs):
        """ Return the queryset for the model """
        return [
            {
                'path': 'www.somesite.com/path-1',
                'date': datetime.now(),
                'method': 'GET'
            }
        ]
