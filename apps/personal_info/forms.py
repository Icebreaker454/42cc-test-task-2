# -*- coding: utf-8 -*-

"""
This module contains forms for the personal_info app
"""
from django import forms
from django.core.urlresolvers import reverse

from crispy_forms.bootstrap import Div
from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.layout import Layout
from crispy_forms.layout import Fieldset

from apps.personal_info.models import Person
from apps.personal_info.widgets import ImagePreviewWidget


class PersonForm(forms.ModelForm):
    """
    This is the form for editing Person data
    """

    def __init__(self, *args, **kwargs):
        """ Init method for crispy_forms integration """
        super(PersonForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        self.helper.form_action = reverse('edit_person')
        self.helper.form_method = 'POST'
        self.helper.form_class = 'person-edit-form'

        self.helper.help_text_inline = True
        self.helper.html5_required = True

        self.helper.label_class = 'form-label'

        self.helper.layout = Layout(
            Div(
                Fieldset(
                    'Personal Info',
                    'first_name',
                    'last_name',
                    'birth_date',
                    'photo',
                ),
                css_class='col-sm-6'
            ),
            Div(
                Fieldset(
                    'Contacts',
                    'email',
                    'jabber',
                    'skype',
                    'other_contacts',
                    'bio'
                ),
                css_class='col-sm-6'
            ),
            Div(
                FormActions(
                    Submit(
                        'done_button',
                        'Save',
                        css_class='btn-link done-button'
                    ),
                    Submit(
                        'cancel_button',
                        'Cancel',
                        css_class='btn-link cancel-button'
                    ),
                ),
                css_class='bordered-row'
            )
        )

    class Meta:
        model = Person

        widgets = {'photo': ImagePreviewWidget}
