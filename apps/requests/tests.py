# -*- coding: utf-8 -*-

"""
    This module contains functional tests for the
    requests application.
"""
import json
from datetime import datetime

from django.core.urlresolvers import reverse
from django.test import TestCase

from apps.requests.models import WebRequest


class RequestsPageTest(TestCase):
    """ This is a set of tests for the Requests view """

    def setUp(self):
        """ Provide initial testing data """
        self.url = reverse('requests')

        self.request = WebRequest.objects.create(
            path='/test/',
            method='GET',
            user_agent='TEST AGENT',
            is_secure=True,
            is_ajax=False
        )

    def test_page_title(self):
        """ Test that page title is as follows: 42cc|<page> """
        resp = self.client.get(self.url)

        self.assertContains(resp, '42cc Test Assignment | Requests')

    def test_request_data_displaying(self):
        """ test that there is some data on the page """
        resp = self.client.get(self.url)
        self.assertIn('requests', resp.context)
        self.assertContains(resp, 'Last 10 HTTP requests')
        self.assertContains(resp, self.request.path)
        self.assertContains(resp, self.request.method)


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

    def test_ajax_notiication_ignored(self):
        """ Test that notification requests are ignored """
        self.assertEqual(WebRequest.objects.count(), 0)

        self.client.get(
            reverse(
                'rq_notifications',
                kwargs={'last_request': 0}
            ),
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )

        self.assertEqual(WebRequest.objects.count(), 0)

    def test_ajax_update_ignored(self):
        """ Test that AJAX updating the request table is ignored """
        self.assertEqual(WebRequest.objects.count(), 0)

        self.client.get(
            self.url2,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )

        self.assertEqual(WebRequest.objects.count(), 0)


class AJAXGetNotificationsTest(TestCase):
    """ This is a set of tests for the AJAX get_notifications view """
    def setUp(self):
        """ Initialize testing data """
        self.last_request = WebRequest.objects.create(
            path='www.test.com/test/',
            method='GET',
            user_agent='TEST AGENT',
            is_secure=True,
            is_ajax=False
        )
        self.kwargs = {'last_request': self.last_request.id}
        self.url = reverse(
            'rq_notifications',
            kwargs=self.kwargs
        )

    def test_ajax_required(self):
        """ Test that only AJAX requests are accepted """
        resp = self.client.get(self.url)

        self.assertEqual(resp.status_code, 400)
        self.assertIn('Direct HTTP request is not allowed', resp.content)

    def test_get_required(self):
        """ Test that only GET requests are accepted """
        resp = self.client.post(
            self.url,
            {
                'data': 'test'
            },
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )

        self.assertEqual(resp.status_code, 400)
        resp_data = json.loads(resp.content)

        self.assertEqual(resp_data['status'], 'error')
        self.assertEqual(
            resp_data['error_message'],
            'Only GET requests are allowed'
        )

    def test_base_unread_count(self):
        """ Test that unread count is 0 for the current request """
        resp = self.client.get(
            self.url,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )

        resp_data = json.loads(resp.content)

        self.assertEqual(resp_data['status'], 'success')
        self.assertEqual(resp_data['count'], 0)

    def test_new_request_notification(self):
        """ Test that new requests increase the notification count """
        WebRequest.objects.create(
            path='www.test.com/test/',
            method='GET',
            user_agent='TEST AGENT',
            is_secure=True,
            is_ajax=False
        )
        resp = self.client.get(
            self.url,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )

        resp_data = json.loads(resp.content)

        self.assertEqual(resp_data['status'], 'success')
        self.assertEqual(resp_data['count'], 1)
