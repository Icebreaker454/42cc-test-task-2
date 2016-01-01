# -*- coding: utf-8 -*-

"""
This file contains models for the personal_info app
"""
from django.db import models

from fortytwo_test_task.settings.common import MEDIA_ROOT


class Person(models.Model):
    """ The person model class """
    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'

    # personal data
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    birth_date = models.DateField()
    bio = models.TextField(blank=True, null=True)

    # contacts
    email = models.EmailField(max_length=128)
    jabber = models.EmailField(max_length=128, blank=True, null=True)
    skype = models.CharField(max_length=64, blank=True, null=True)
    other_contacts = models.TextField(blank=True, null=True)

    # picture
    photo = models.ImageField(upload_to=MEDIA_ROOT, blank=True, null=True)

    def __unicode__(self):
        """ String representarion of the model """
        return '%s %s' % (self.first_name, self.last_name)
