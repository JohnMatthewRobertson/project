""" unit test """

from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.


class CustomUserTest(TestCase):
    """ test user """

    def test_create_user(self):
        """ test create user """
        normaluser = get_user_model()
        user = normaluser.objects.create_user(
            username='testuserone',
            email='testuserone@email.com',
            password='testpass123')

        self.assertEqual(user.username, 'testuserone')
        self.assertEqual(user.email, 'testuserone@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        """ test create superuser admin """
        adminuser = get_user_model()
        admin = adminuser.objects.create_superuser(
            username='testadminuserone',
            email='testadminuserone@email.com',
            password='testpass123')

        self.assertEqual(admin.username, 'testadminuserone')
        self.assertEqual(admin.email, 'testadminuserone@email.com')
        self.assertTrue(admin.is_active)
        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)
