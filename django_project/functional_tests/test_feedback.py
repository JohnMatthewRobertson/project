""" functional test"""

from django.contrib.auth import get_user_model
from .base import FunctionalTest
import time

class FeedbackTest(FunctionalTest):
    """ better comment"""

    def test_user_can_log_in_and_leave_feedback(self):
        """ better comment """
        normal_user = get_user_model()
        user = normal_user.objects.create_user(username=self.correct_test_username,
                                               email=self.correct_test_useremail,
                                               password=self.correct_test_userpassword)


        self.browser.get(self.live_server_url)
        
        self.browser.set_window_size(1024, 768)

        login_link = self.browser.find_element_by_link_text('Log In')
        self.assertEqual(login_link.text, "Log In")

        login_link.click()

        username = self.browser.find_element_by_id('id_login')

        username.click()

        username.send_keys(self.correct_test_useremail)

        password = self.browser.find_element_by_id('id_password')

        password.click()

        password.send_keys(self.correct_test_userpassword)

        submit_buttom = self.browser.find_element_by_css_selector('button')

        submit_buttom.click()

        time.sleep(10)

        loggedin_message = self.browser.find_element_by_css_selector('h1')

        self.assertEqual(loggedin_message.text, 'Home')

        feedback_link = self.browser.find_element_by_link_text('Feedback')
        self.assertEqual(feedback_link.text, "Feedback")

        feedback_link.click()

        message = self.browser.find_element_by_id("id_message")
        
        message.click()

        message.send_keys("test message")

        submit_button = self.browser.find_element_by_css_selector(".btn")

        submit_button.click()

        display_message = self.browser.find_elements_by_class_name("card-text")

        print(display_message)

        time.sleep(10)

        self.assertEqual(display_message.text, "test message")

        logout_link = self.browser.find_element_by_link_text('Log Out')
        self.assertEqual(logout_link.text, "Log Out")

        logout_link.click()

        submit_buttom = self.browser.find_element_by_css_selector('button')

        submit_buttom.click()

        loggedout_message = self.browser.find_element_by_css_selector('h1')

        self.assertEqual(loggedout_message.text, 'Log In')


