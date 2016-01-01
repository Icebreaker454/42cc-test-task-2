# -*- coding: utf-8 -*-

"""
This module contains forms for the personal_info app
"""
from django import forms

from apps.personal_info.models import Person


class PersonForm(forms.ModelForm):
    """
    This is the form for editing Person data
    """
    class Meta:
        model = Person
