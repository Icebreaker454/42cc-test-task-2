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

    def dispatch(self, request, *args, **kwargs):
        """ Logging the request path """
        logger.info('Request path: %s' % request.path)
        return super(Home, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        """ Gets context data for the template """
        logger.info('Processing context data for Home view')
        context = super(Home, self).get_context_data(*args, **kwargs)
        person = Person.objects.all()
        if person.exists():
            context['object'] = person[0]
            logger.debug('Data shown: %s' % person[0])
        else:
            context['error_message'] = \
                'Sorry, but the Person database record got deleted'
            logger.warn(
                'Person database record has been deleted.'
                ' Displaying error message'
            )
        return context
