from django.test import TestCase
from django.urls import reverse, resolve
from hub.views import HubHome

class HomePageTest(TestCase):

    def setUp(self):
        url = reverse('hub:hub_home')
        self.response = self.client.get(url)

    def test_home_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_home_page_url_name(self):
        response = self.client.get(reverse('hub:hub_home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_uses_home_template(self):
        self.assertTemplateUsed(self.response, 'hub/home.html')

    def test_home_page_url_resolves_home_page_view(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HubHome.as_view().__name__)