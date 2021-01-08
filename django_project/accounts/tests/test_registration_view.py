""" module unit test """

from django.test import TestCase
from django.urls import reverse


class SignupPageTest(TestCase):
    """ test sign up page """

    def setUp(self):
        """ setup url route """
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_home_page_status_code(self):
        """ check url is rechable """
        self.assertEqual(self.response.status_code, 200)

    def test_home_page_url_name(self):
        """ check url reachable """
        response = self.client.get(reverse('account_signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_page_uses_signup_templates(self):
        """ check tempate is used """
        self.assertTemplateUsed(self.response, 'account/signup.html')
