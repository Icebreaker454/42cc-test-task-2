# -*- coding: utf-8 -*-

"""
    This module contains functional tests for the
    personal_info application.
"""

from django.core.urlresolvers import reverse
from django.test import TestCase

# Create your tests here.


class LandingPageTest(TestCase):
    """
    This is a set of tests for the Home page
    """
    def setUp(self):
        """ Initialize testing data """
        self.url = reverse('home')

    def test_response_status_code(self):
        """ Test whether the response status code is OK """
        resp = self.client.get(self.url)
        self.assertEqual(resp.status_code, 200)

    def test_personal_data_on_page(self):
        """ Test whether personal data is displayed on the page """
        resp = self.client.get(self.url)

        self.assertIn('object', resp.context)

        self.assertIn('Paul', resp.content)
        self.assertIn('Pukach', resp.content)
        self.assertIn('Jun 25, 1996', resp.content)
        self.assertIn('applied mathematician', resp.content)

    def test_contact_data_on_page(self):
        """ Test whether the contact data is displayed on the page """
        resp = self.client.get(self.url)

        self.assertIn('object', resp.context)

        self.assertIn('pavlopukach@gmail.com', resp.content)
        self.assertIn('icebreaker454@khavr.com', resp.content)
        self.assertIn('shoker2506', resp.content)
        self.assertIn('+380963699598', resp.content)
