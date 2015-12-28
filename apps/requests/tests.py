# -*- coding: utf-8 -*-

"""
    This module contains functional tests for the
    requests application.
"""
from datetime import datetime

from django.core.urlresolvers import reverse
from django.test import TestCase

from apps.requests.models import WebRequest


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


class WebRequestTest(TestCase):
    """ This is a set of tests for the WebRequest model """
    def setUp():
        """ Prvide initial testing data """
        WebRequest.objects.create(
            path='www.test.com/test/',
            date=datetime.now(),
            method='GET'
        )

    def test_string_representation(self):
        """ Test that the string representation match the standard """
        self.assertEqual(
            self.webrequest.__unicode__(),
            "%s %s" % (
                self.webrequest.method,
                self.webrequest.path
            )
        )
