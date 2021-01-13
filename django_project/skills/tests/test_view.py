""" unit tests """
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve

# Create your tests here.


class SkillViewTest(TestCase):
    """ test view url """
    def setUp(self):
        """ create a test user """
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'testuser@email.com',
            password = 'testpass123',
        )

    def test_skill_list_uses_template(self):
        """ test for correct template """
        response = self.client.login(email='testuser@email.com', password='testpass123')
        self.assertTrue(response)
        response = self.client.get(reverse('skills:skill_list'))
        self.assertTemplateUsed(response, 'skills/skill_list.html')

    def test_skill_list_page_reachable(self):
        """ check for 200 response """
        response = self.client.login(email='testuser@email.com', password='testpass123')
        self.assertTrue(response)
        response = self.client.get(reverse('skills:skill_list'))
        self.assertEqual(response.status_code, 200)

