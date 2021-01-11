""" unit tests """
from django.test import TestCase
from django.contrib.auth import get_user_model
from feedback.models import Feedback

# Create your tests here.


class FeedbackModelTest(TestCase):
    """ test creating a feedback message """
    def setUp(self):
        """ create a test user """
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'testuser@email.com',
            password = 'testpass123',
        )

    def test_create_and_save_feedback_message(self):
        """ create and save an exampe message"""
        self.message = Feedback.objects.create(author=self.user, message="test message")    
        self.message.save()
        self.assertIn(self.message, Feedback.objects.all())


