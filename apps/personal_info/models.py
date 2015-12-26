# -*- coding: utf-8 -*-

"""
This file contains models for the personal_info app
"""
import logging

from django.db import models

logger = logging.getLogger('personal_info')


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

    def __unicode__(self):
        """ String representarion of the model """
        return '%s %s' % (self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        """ Overriding save() not to store more than 1 record """
        if self.pk is None and Person.objects.count() == 1:
            logger.warn(
                'Cannot add more than 1 person into database.'
                ' Changes will not be saved.'
            )
            return
        super(Person, self).save(*args, **kwargs)
