""" unit tests """
from django.test import TestCase
from django.contrib.auth import get_user_model


# Create your tests here.


class FeedbackViewTest(TestCase):
    """ test view url """
    def setUp(self):
        """ create a test user """
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'testuser@email.com',
            password = 'testpass123',
        )

    def test_feedback_page_uses_template(self):
        """ test for correct template """
        response = self.client.login(email='testuser@email.com', password='testpass123')
        self.assertTrue(response)
        response = self.client.get('/feedback/')
        self.assertTemplateUsed(response, 'feedback/feedback_list.html')

    def test_feedback_page_reachable(self):
        """ check for 200 response """
        response = self.client.login(email='testuser@email.com', password='testpass123')
        self.assertTrue(response)
        response = self.client.get('/feedback/')
        self.assertEqual(response.status_code, 200)

