""" unit tests """
from django.test import TestCase
from django.contrib.auth import get_user_model
from feedback.forms import FeedbackForm
from feedback.models import Feedback

# Create your tests here.


class FeedbackFormTest(TestCase):
    """ test creating a feedback message """
    def setUp(self):
        """ create a test user """
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'testuser@email.com',
            password = 'testpass123',
        )

    def test_empty_feedback_message_fail_is_valid_form(self):
        """ test empty message fails """
        form = FeedbackForm(data={'message': ''})
        self.assertFalse(form.is_valid())

    def test_feedback_message_save(self):
        """ create and save an exampe message using form """
        form = FeedbackForm(data={'message' : 'test message'})
        form.instance.author = self.user
        self.assertTrue(form.is_valid())
        new_message = form.save()
        self.assertIn(new_message, Feedback.objects.all())
