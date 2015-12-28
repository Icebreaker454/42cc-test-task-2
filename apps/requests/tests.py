# -*- coding: utf-8 -*-

"""
    This module contains functional tests for the
    requests application.
"""
from datetime import datetime

from django.core.urlresolvers import reverse
from django.test import TestCase

from apps.requests.models import WebRequest


class RequestsPageTest(TestCase):
    """ This is a set of tests for the Requests view """

    def setUp(self):
        """ Provide initial testing data """
        self.url = reverse('requests')

    def test_page_title(self):
        """ Test that page title is as follows: 42cc|<page> """
        resp = self.client.get(self.url)

        self.assertContains(resp, '42cc Test Assignment | Requests')

    def test_request_data_displaying(self):
        """ test that there is some data on the page """
        resp = self.client.get(self.url)
        self.assertIn('requests', resp.context)
        self.assertContains(resp, 'Last 10 HTTP requests')
        self.assertContains(resp, 'www.somesite.com/path-1')
        self.assertContains(resp, 'POST')


class WebRequestTest(TestCase):
    """ This is a set of tests for the WebRequest model """
    def setUp(self):
        """ Prvide initial testing data """
        self.webrequest = WebRequest.objects.create(
            path='www.test.com/test/',
            time=datetime.now(),
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


class RequestMiddlewareTest(TestCase):
    """ This is a set of tests that check the midddleware behaviour """
    def setUp(self):
        """ Initialize testing data """
        self.url1 = reverse('home')
        self.url2 = reverse('requests')

    def test_request_count_changes(self):
        """ Test that WebRequest entries are created upon page visiting """
        self.assertEqual(WebRequest.objects.count(), 0)

        self.client.get(self.url1)
        self.assertEqual(WebRequest.objects.count(), 1)
        wr = WebRequest.objects.first()
        self.assertIn(self.url1, wr.path)
        self.assertEqual(wr.method, 'GET')

        self.client.get(self.url2)
        self.assertEqual(WebRequest.objects.count(), 2)
        wr = WebRequest.objects.all()[1]
        self.assertIn(self.url2, wr.path)
        self.assertEqual(wr.method, 'GET')
