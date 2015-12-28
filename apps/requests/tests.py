# -*- coding: utf-8 -*-

"""
    This module contains functional tests for the
    requests application.
"""

from django.core.urlresolvers import reverse
from django.test import TestCase


class RequestsTest(TestCase):
    """ This is a set of tests for the Requests view """

    def setUp(self):
        """ Provide initial testing data """
        self.url = reverse('requests')

    def test_request_data_displaying(self):
        """ test that there is some data on the page """
        resp = self.client.get(self.url)
        self.assertIn('requests', resp.context)
        self.assertContains(resp, 'Last 10 HTTP requests')
        self.assertContains(resp, 'www.somesite.com/path-1')
        self.assertContains(resp, 'POST')
