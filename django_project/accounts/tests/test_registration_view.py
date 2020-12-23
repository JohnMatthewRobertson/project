from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve
from accounts.forms import CustomUserCreationForm
from accounts.views import SignupPageView

class SignupPageTest(TestCase):

    def setUp(self):
        url = reverse('accounts:signup')
        self.response = self.client.get(url)

    def test_home_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_home_page_url_name(self):
        response = self.client.get(reverse('accounts:signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_page_uses_signup_templates(self):
        self.assertTemplateUsed(self.response, 'registration/signup.html')

    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_signup_view(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(view.func.__name__, SignupPageView.as_view().__name__)
