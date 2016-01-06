# -*- coding: utf-8 -*-

"""
    This module contains functional tests for the
    personal_info application.
"""
import os
import json

from datetime import datetime
from PIL import Image
from StringIO import StringIO

from django.contrib.auth.models import User
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.urlresolvers import reverse
from django.test import TestCase

from apps.personal_info.models import Person
from fortytwo_test_task.settings.common import BASE_DIR

# Create your tests here.


class LandingPageTest(TestCase):
    """
    This is a set of tests for the Home page
    """
    def setUp(self):
        """ Initialize testing data """
        self.url = reverse('home')
        self.person = Person.objects.all()[0]

    def test_page_title(self):
        """ Test that page title is as follows: 42cc|<page> """
        resp = self.client.get(self.url)

        self.assertContains(resp, '42cc Test Assignment | Home')

    def test_personal_data_on_page(self):
        """ Test whether personal data is displayed on the page """
        resp = self.client.get(self.url)

        self.assertIn('object', resp.context)

        self.assertContains(resp, self.person.first_name)
        self.assertContains(resp, self.person.last_name)
        self.assertContains(
            resp,
            datetime.strftime(self.person.birth_date, '%b %d, %Y')
        )
        self.assertContains(resp, self.person.bio)

    def test_contact_data_on_page(self):
        """ Test whether the contact data is displayed on the page """
        resp = self.client.get(self.url)

        self.assertIn('object', resp.context)

        self.assertContains(resp, self.person.email)
        self.assertContains(resp, self.person.jabber)
        self.assertContains(resp, self.person.skype)
        self.assertContains(resp, self.person.other_contacts)

    def test_no_person_data(self):
        """ Test the behavior if the contact data got deleted """
        self.person.delete()

        resp = self.client.get(self.url)

        self.assertIn('object', resp.context)
        self.assertTrue(resp.context['object'] is None)

        self.assertContains(
            resp,
            'Sorry, but the Person database record got deleted'
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

        self.assertContains(resp, self.person.first_name)
        self.assertContains(resp, self.person.last_name)
        self.assertContains(
            resp,
            datetime.strftime(self.person.birth_date, '%b %d, %Y')
        )
        self.assertContains(resp, self.person.bio)

        self.assertContains(resp, self.person.email)
        self.assertContains(resp, self.person.jabber)
        self.assertContains(resp, self.person.skype)
        self.assertContains(resp, self.person.other_contacts)


class PersonEditPageTest(TestCase):
    """
    This is a set of tests for the Person Edit page
    """
    def setUp(self):
        """ Initialize testing data """
        Person.objects.all().delete()
        image = Image.open(
            StringIO(
                open(
                    os.path.join(
                        BASE_DIR,
                        'assets',
                        'img',
                        'test_large.jpg'
                    )
                ).read()
            ),
        )
        image_file = StringIO()
        image.save(image_file, format='JPEG', quality=90)
        self.uploaded_file = InMemoryUploadedFile(
            image_file,
            None,
            'test.jpg',
            'image/jpeg',
            image_file.len,
            None
        )
        self.person = Person.objects.create(
            first_name='Alex',
            last_name='Messer',
            birth_date=datetime(1996, 9, 5),
            bio='Cadet at Lviv Army Academy',
            email='messer1337@gmail.com',
            skype='messer1337',
            photo=self.uploaded_file
        )
        self.url = reverse('edit_person')
        user = User.objects.create_user(
            'Test', 'test@testl.com', 'test'
        )
        self.client.login(username=user.username, password='test')

    def test_login_required(self):
        """ Test that only authenticated users can edit the Person model """
        self.client.logout()
        resp = self.client.get(self.url)

        self.assertRedirects(
            resp,
            '%s?next=%s' % (reverse('login'), reverse('edit_person'))
        )

    def test_first_person_data_on_edit_page(self):
        """ Test that the first Person is shown on edit page """
        resp = self.client.get(self.url)

        self.assertContains(resp, self.person.first_name)
        self.assertContains(resp, self.person.last_name)
        self.assertContains(
            resp,
            datetime.strftime(self.person.birth_date, '%Y-%m-%d')
        )
        self.assertContains(resp, self.person.photo)
        self.assertContains(resp, self.person.bio)
        self.assertContains(resp, self.person.email)
        self.assertContains(resp, self.person.skype)

    def test_first_person_edited(self):
        """ Test that the view edits the first person """

        resp = self.client.post(
            self.url,
            {
                'first_name': 'Not Alex',
                'last_name': 'Not Messer',
                'birth_date': '1997-02-12',
                'email': 'messer1338@gmail.com'
            }
        )
        self.assertRedirects(
            resp,
            (
                '%s?status=Edited{0}successfully' % reverse('home')
            ).format(r'%20')
        )

        resp = self.client.get(reverse('home'))
        self.assertContains(resp, 'Not Alex')
        self.assertContains(resp, 'Not Messer')

        self.assertContains(resp, 'Feb 12, 1997')
        self.assertContains(resp, 'messer1338@gmail.com')

    def test_cancel_button(self):
        """ Test that cancel button does not make changes """
        resp = self.client.post(
            self.url,
            {
                'first_name': 'Not Alex',
                'last_name': 'Not Messer',
                'birth_date': '1997-02-12',
                'email': 'messer1337@gmail.com',
                'cancel_button': 'Not None'
            }
        )
        self.assertRedirects(
            resp,
            (
                '%s?status=Editing{0}cancelled' % reverse('home')
            ).format(r'%20')
        )

        self.assertEqual(self.person.first_name, 'Alex')
        self.assertEqual(self.person.last_name, 'Messer')

    def test_ajax_valid_editing(self):
        """ Test that AJAX post leads to successful json response """

        resp = self.client.post(
            self.url,
            {
                'first_name': 'Not Alex',
                'last_name': 'Not Messer',
                'birth_date': '1997-02-12',
                'email': 'messer1337@gmail.com'
            },
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )

        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.content)
        self.assertEqual(data['status'], 'success')
        self.assertEqual(data['message'], 'Edited successfully')

    def test_ajax_invalid_editing(self):
        """ Test that AJAX post with invalid data leads to form errors """

        resp = self.client.post(
            self.url,
            {
                'first_name': 'Not Alex',
                'last_name': 'Not Messer',
                'birth_date': '1997-02-12',
            },
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )

        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.content)
        self.assertEqual(data['status'], 'error')
        self.assertEqual(data['message'], 'Please, correct the form errors')

    def test_ajax_cancel_button(self):
        """ Test that AJAX post with cancel button leads to successful
            json response with message about cancelled editing """

        resp = self.client.post(
            self.url,
            {
                'first_name': 'Not Alex',
                'last_name': 'Not Messer',
                'birth_date': '1997-02-12',
                'email': 'messer1337@gmail.com',
                'cancel_button': 'Not None'
            },
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )

        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.content)
        self.assertEqual(data['status'], 'success')
        self.assertEqual(data['message'], 'Editing cancelled')


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
