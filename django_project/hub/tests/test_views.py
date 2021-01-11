""" better comments """

from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from hub.views import HubHome


class HomePageTest(TestCase):
    """ better comments """

    def setUp(self):
        """ create a test user """
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'testuser@email.com',
            password = 'testpass123',
        )


    def test_home_page_status_code(self):
        """ better comments """
        response = self.client.login(email='testuser@email.com', password='testpass123')
        self.assertTrue(response)
        url = reverse('hub:hub_home')
        self.response = self.client.get(url)
        self.assertEqual(self.response.status_code, 200)

    def test_home_page_url_name(self):
        """ better comments """
        response = self.client.login(email='testuser@email.com', password='testpass123')
        self.assertTrue(response)
        response = self.client.get(reverse('hub:hub_home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_uses_home_template(self):
        """ better comments """
        response = self.client.login(email='testuser@email.com', password='testpass123')
        self.assertTrue(response)
        response = self.client.get(reverse('hub:hub_home'))
        self.assertTemplateUsed(response, 'hub/home.html')

    def test_home_page_url_resolves_home_page_view(self):
        """ better comments """
        response = self.client.login(email='testuser@email.com', password='testpass123')
        self.assertTrue(response)
        view = resolve('/')
        self.assertEqual(view.func.__name__, HubHome.as_view().__name__)
