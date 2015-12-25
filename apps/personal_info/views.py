# -*- coding: utf-8 -*-

"""
This file contains views for the personal_info app
"""
from datetime import datetime

from django.views.generic import TemplateView


class Home(TemplateView):
    """
    The class-based view for the landing(Home) page
    """
    template_name = 'personal_info/landing.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Home, self).get_context_data(*args, **kwargs)
        context['object'] = {
            'first_name': 'Paul',
            'last_name': 'Pukach',
            'birth_date': datetime(1996, 6, 25),
            'bio': 'My name is Paul and I am an applied mathematician.'
            ' My hobby is developing web-applications',
            'email': 'pavlopukach@gmail.com',
            'jabber': 'icebreaker454@khavr.com',
            'skype': 'shoker2506',
            'other_contacts': 'Phone: +380963699598'
        }
        return context
