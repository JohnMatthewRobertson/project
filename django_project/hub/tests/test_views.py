from django.test import TestCase

class HomePageTest(TestCase):

    def test_home_page_uses_home_template(self):
        response = self.client.get('')
        self.assertTemplateUsed(response, 'hub/home.html')