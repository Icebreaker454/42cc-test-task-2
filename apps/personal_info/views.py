# -*- coding: utf-8 -*-

"""
This file contains views for the personal_info app
"""
import logging

from django.views.generic import TemplateView

from apps.personal_info.models import Person

logger = logging.getLogger('personal_info')


class Home(TemplateView):
    """
    The class-based view for the landing(Home) page
    """
    template_name = 'personal_info/landing.html'

    def get_context_data(self, *args, **kwargs):
        """ Gets context data for the template """
        logger.info('Processing context data for Home view')
        logger.info('Request data: \n %s' % self.request)
        context = super(Home, self).get_context_data(*args, **kwargs)
        person = Person.objects.first()
        context['object'] = person
        if person is None:
            logger.warn(
                'Person database record has been deleted.'
            )
        return context
