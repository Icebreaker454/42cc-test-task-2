# -*- coding: utf-8 -*-

"""
This file contains views for the personal_info app
"""
import json
import logging

from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView

from apps.core.views import LoginRequiredMixin
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


class EditPerson(LoginRequiredMixin, UpdateView):
    """
    The class-based view for editing Persons
    """
    form_class = PersonForm
    template_name = 'personal_info/person_edit.html'

    def get_object(self, *args, **kwargs):
        """ View that gets the object to edit """
        return Person.objects.first()

    def post(self, request, *args, **kwargs):
        """ This method catches the cancel_button on a posted form """
        logger.info(request)
        if request.POST.get('cancel_button'):
            if request.is_ajax():
                return HttpResponse(
                    json.dumps(
                        {
                            'status': 'success',
                            'message': 'Editing cancelled'
                        }
                    ),
                    content_type='application/json'
                )
            logger.info('Person Editing Cancelled')
            return HttpResponseRedirect(
                '%s?status=Editing cancelled' % reverse('home')
            )
        return super(EditPerson, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        """ This method adds AJAX form submitting support """
        logger.debug(form.data)
        response = super(EditPerson, self).form_valid(form)
        if self.request.is_ajax():
            return HttpResponse(
                json.dumps(
                    {
                        'status': 'success',
                        'message': 'Edited successfully'
                    }
                ),
                content_type='application/json'
            )
        return response

    def form_invalid(self, form):
        """ This method adds AJAX form submitting support on form errors """
        logger.debug(form.errors)
        response = super(EditPerson, self).form_invalid(form)
        if self.request.is_ajax():
            return HttpResponse(
                json.dumps(
                    {
                        'status': 'error',
                        'errors': form.errors,
                        'message': 'Please, correct the form errors'
                    }
                ),
                content_type='application/json'
            )
        return response

    def get_success_url(self):
        """ URL to redirect to after success """
        logger.info('Person Edited Successfully')
        return '%s?status=Edited successfully' % reverse('home')
