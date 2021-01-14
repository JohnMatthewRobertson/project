""" unit test for skill form """
from django.test import TestCase
from django.contrib.auth import get_user_model



# Create your tests here.


class SkillModelTest(TestCase):
    """ test creating a skill """
    def setUp(self):
        """ create a test user """
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'testuser@email.com',
            password = 'testpass123',
        )






