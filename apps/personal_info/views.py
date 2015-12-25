# -*- coding: utf-8 -*-

"""
This file contains views for the personal_info app
"""
from django.views.generic import TemplateView


class Home(TemplateView):
    """
    The class-based view for the landing(Home) page
    """
    template_name = 'personal_info/landing.html'
