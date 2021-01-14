""" unit tests for skills view """

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve

# Create your tests here.


class SkillViewTest(TestCase):
    """ test view url """
    def setUp(self):
        """ create a test user """

        self.username = 'testuser'
        self.email = 'testuser@email.com'
        self.password = 'testpass123'

        self.user = get_user_model().objects.create_user(
            username = self.username,
            email = self.email,
            password = self.password,
        )

    def test_skill_list_uses_template(self):
        """ test for correct template """
        response = self.client.login(email=self.email, password=self.password)
        self.assertTrue(response)
        response = self.client.get(reverse('skills:skill_list'))
        self.assertTemplateUsed(response, 'skills/skill_list.html')

    def test_skill_list_page_reachable(self):
        """ check for 200 response """
        response = self.client.login(email=self.email, password=self.password)
        self.assertTrue(response)
        response = self.client.get(reverse('skills:skill_list'))
        self.assertEqual(response.status_code, 200)

    def test_skill_detail_uses_template(self):
        """ test for correct template """
        response = self.client.login(email=self.email, password=self.password)
        self.assertTrue(response)
        response = self.client.get(reverse('skills:skill_detail'))
        self.assertTemplateUsed(response, 'skills/skill_detail.html')

    def test_skill_detail_page_reachable(self):
        """ check for 200 response """
        response = self.client.login(email=self.email, password=self.password)
        self.assertTrue(response)
        response = self.client.get(reverse('skills:skill_detail'))
        self.assertEqual(response.status_code, 200)

    def test_skill_category_detail_uses_template(self):
        """ test for correct template """
        response = self.client.login(email=self.email, password=self.password)
        self.assertTrue(response)
        response = self.client.get(reverse('skills:skill_category_detail'))
        self.assertTemplateUsed(response, 'skills/skill_category_detail.html')

    def test_skill_category_detail_page_reachable(self):
        """ check for 200 response """
        response = self.client.login(email=self.email, password=self.password)
        self.assertTrue(response)
        response = self.client.get(reverse('skills:skill_category_detail'))
        self.assertEqual(response.status_code, 200)

    def test_skill_sub_category_detail_uses_template(self):
        """ test for correct template """
        response = self.client.login(email=self.email, password=self.password)
        self.assertTrue(response)
        response = self.client.get(reverse('skills:skill_sub_category_detail'))
        self.assertTemplateUsed(response, 'skills/skill_sub_category_detail.html')

    def test_skill_sub_category_detail_page_reachable(self):
        """ check for 200 response """
        response = self.client.login(email=self.email, password=self.password)
        self.assertTrue(response)
        response = self.client.get(reverse('skills:skill_sub_category_detail'))
        self.assertEqual(response.status_code, 200)

    def test_team_skill_uses_template(self):
        """ test for correct template """
        response = self.client.login(email=self.email, password=self.password)
        self.assertTrue(response)
        response = self.client.get(reverse('skills:team_skill'))
        self.assertTemplateUsed(response, 'skills/team_skill.html')

    def test_team_skill_page_reachable(self):
        """ check for 200 response """
        response = self.client.login(email=self.email, password=self.password)
        self.assertTrue(response)
        response = self.client.get(reverse('skills:team_skill'))
        self.assertEqual(response.status_code, 200)

    def test_user_skill_list_uses_template(self):
        """ test for correct template """
        response = self.client.login(email=self.email, password=self.password)
        self.assertTrue(response)
        response = self.client.get(reverse('skills:user_skill_list'))
        self.assertTemplateUsed(response, 'skills/user_skill_list.html')

    def test_user_skill_list_page_reachable(self):
        """ check for 200 response """
        response = self.client.login(email=self.email, password=self.password)
        self.assertTrue(response)
        response = self.client.get(reverse('skills:user_skill_list'))
        self.assertEqual(response.status_code, 200)

    def test_user_skill_add_uses_template(self):
        """ test for correct template """
        response = self.client.login(email=self.email, password=self.password)
        self.assertTrue(response)
        response = self.client.get(reverse('skills:user_skill_add'))
        self.assertTemplateUsed(response, 'skills/skill_create_user_skill.html')

    def test_user_skill_add_page_reachable(self):
        """ check for 200 response """
        response = self.client.login(email=self.email, password=self.password)
        self.assertTrue(response)
        response = self.client.get(reverse('skills:user_skill_add'))
        self.assertEqual(response.status_code, 200)

