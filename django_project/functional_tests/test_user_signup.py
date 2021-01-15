""" functional test"""

from .base import FunctionalTest


class UserSignupTest(FunctionalTest):
    """ test user registration """

    def test_user_can_sign_up(self):
        """ to user can successfully sign up """

        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        login_link = self.browser.find_element_by_link_text('Sign Up')
        self.assertEqual(login_link.text, "Sign Up")

        login_link.click()

        email = self.browser.find_element_by_id('id_email')

        email.click()

        email.send_keys(self.correct_test_useremail)

        username = self.browser.find_element_by_id('id_username')

        username.click()

        username.send_keys(self.correct_test_username)

        password_one = self.browser.find_element_by_id('id_password1')

        password_one.click()

        password_one.send_keys(self.correct_test_userpassword)

        password_two = self.browser.find_element_by_id('id_password2')

        password_two.click()

        password_two.send_keys(self.correct_test_userpassword)

        submit_buttom = self.browser.find_element_by_css_selector('button')

        submit_buttom.click()

        log_in_message = self.browser.find_element_by_css_selector('h1')

        self.assertEqual(log_in_message.text, 'Home')
