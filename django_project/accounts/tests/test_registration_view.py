from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve

class SignupPageTest(TestCase):

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_home_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_home_page_url_name(self):
        response = self.client.get(reverse('account_signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_page_uses_signup_templates(self):
        self.assertTemplateUsed(self.response, 'account/signup.html')


