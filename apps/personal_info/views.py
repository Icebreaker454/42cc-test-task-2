# -*- coding: utf-8 -*-

"""
This file contains views for the personal_info app
"""
import logging

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView

from apps.personal_info.models import Person
from apps.personal_info.forms import PersonForm

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
        logger.debug('Showing person: %s' % person)
        return context


class EditPerson(UpdateView):
    """
    The class-based view for editing Persons
    """
    form_class = PersonForm
    template_name = 'personal_info/person_edit.html'

    def get_object(self):
        """ View that gets the pbject to edit """
        return Person.objects.first()

    def post(self, request, *args, **kwargs):
        """ This method catches the cancel_button on a posted form """
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(
                reverse('home')
            )
        return super(EditPerson, self).post(request, *args, **kwargs)

    def get_success_url(self):
        """ URL to redirect to after success """
        return reverse('home')
