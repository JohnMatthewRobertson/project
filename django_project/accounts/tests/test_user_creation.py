from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.

class CustomUserTest(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(username='testuserone', email='testuserone@email.com', password='testpass123')

        self.assertEqual(user.username, 'testuserone')
        self.assertEqual(user.email, 'testuserone@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)


    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(username = 'testadminuserone', email = 'testadminuserone@email.com', password = 'testpass123')

        self.assertEqual(admin_user.username, 'testadminuserone')
        self.assertEqual(admin_user.email, 'testadminuserone@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)