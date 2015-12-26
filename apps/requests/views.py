# -*- coding: utf-8 -*-

"""
This file contains views for the requests
application
"""
from django.views.generic import ListView


class Requests(ListView):
    """ The requests class-based view """
    queryset = []
    template_name = 'requests/all.html'
    pass
