# -*- coding: utf-8 -*-

"""
This file contains views for the personal_info app
"""

from django.views.generic import TemplateView

from apps.personal_info.models import Person


class Home(TemplateView):
    """
    The class-based view for the landing(Home) page
    """
    template_name = 'personal_info/landing.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Home, self).get_context_data(*args, **kwargs)
        person = Person.objects.all()
        if person.exists():
            context['object'] = person[0]
        else:
            context['error_message'] = \
                'Sorry, but the Person database record got deleted'
        return context
