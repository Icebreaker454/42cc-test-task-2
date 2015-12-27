# -*- coding: utf-8 -*-

"""
    This module contains functional tests for the
    personal_info application.
"""
from datetime import datetime

from django.core.urlresolvers import reverse
from django.test import TestCase

from apps.personal_info.models import Person

# Create your tests here.


class LandingPageTest(TestCase):
    """
    This is a set of tests for the Home page
    """
    def setUp(self):
        """ Initialize testing data """
        self.url = reverse('home')
        self.person = Person.objects.all()[0]

    def test_response_status_code(self):
        """ Test whether the response status code is OK """
        resp = self.client.get(self.url)
        self.assertEqual(resp.status_code, 200)

    def test_personal_data_on_page(self):
        """ Test whether personal data is displayed on the page """
        resp = self.client.get(self.url)

        self.assertIn('object', resp.context)

        self.assertIn(self.person.first_name, resp.content)
        self.assertIn(self.person.last_name, resp.content)
        self.assertIn(
            datetime.strftime(self.person.birth_date, '%b %d, %Y'),
            resp.content
        )
        self.assertIn(self.person.bio, resp.content)

    def test_contact_data_on_page(self):
        """ Test whether the contact data is displayed on the page """
        resp = self.client.get(self.url)

        self.assertIn('object', resp.context)

        self.assertIn(self.person.email, resp.content)
        self.assertIn(self.person.jabber, resp.content)
        self.assertIn(self.person.skype, resp.content)
        self.assertIn(self.person.other_contacts, resp.content)

    def test_no_person_data(self):
        """ Test the behavior if the contact data got deleted """
        self.person.delete()

        resp = self.client.get(self.url)

        self.assertIn('object', resp.context)
        self.assertTrue(resp.context['object'] is None)

        self.assertIn(
            'Sorry, but the Person database record got deleted',
            resp.content
        )

    def test_two_person_records(self):
        """
        Test that whether there are more than 1 Person record, only
        the first one gets displayed
        """
        Person.objects.create(
            first_name='Evan',
            last_name='Dorms',
            birth_date=datetime(1990, 1, 1),
            bio='sample',
            email='sample@sample.com'
        )
        resp = self.client.get(self.url)

        self.assertIn(self.person.first_name, resp.content)
        self.assertIn(self.person.last_name, resp.content)
        self.assertIn(
            datetime.strftime(self.person.birth_date, '%b %d, %Y'),
            resp.content
        )
        self.assertIn(self.person.bio, resp.content)

        self.assertIn(self.person.email, resp.content)
        self.assertIn(self.person.jabber, resp.content)
        self.assertIn(self.person.skype, resp.content)
        self.assertIn(self.person.other_contacts, resp.content)


class PersonTest(TestCase):
    """
    This is a set of tests for the Person model
    """
    def setUp(self):
        """ Initialize testing data """
        self.person = Person.objects.create(
            first_name='Alex',
            last_name='Messer',
            birth_date=datetime(1996, 9, 5),
            bio='Cadet at Lviv Army Academy',
            email='messer1337@gmail.com',
            skype='messer1337'
        )

    def test_string_representation(self):
        """ Test whether the model's string representation is correct """
        self.assertEqual(self.person.__unicode__(), 'Alex Messer')
