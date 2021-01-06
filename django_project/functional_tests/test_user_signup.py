import unittest, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from webdriver_manager.firefox import GeckoDriverManager
from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from .base import FunctionalTest

class UserSignupTest(FunctionalTest):

    def test_user_can_sign_up(self):

        self.test_username = 'testusertwo'
        self.test_userpassword = 'testpass123'
        self.test_useremail = 'testusertwo@email.com'

        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        login_link = self.browser.find_element_by_link_text('Sign Up')
        self.assertEqual(login_link.text, "Sign Up")

        login_link.click()

        email = self.browser.find_element_by_id('id_email')

        email.click()

        email.send_keys(self.test_useremail)

        username = self.browser.find_element_by_id('id_username')
        
        username.click()

        username.send_keys(self.test_username)

        password_one = self.browser.find_element_by_id('id_password1')

        password_one.click()

        password_one.send_keys(self.test_userpassword)

        password_two = self.browser.find_element_by_id('id_password2')

        password_two.click()

        password_two.send_keys(self.test_userpassword)

        submit_buttom = self.browser.find_element_by_css_selector('button')

        submit_buttom.click()

        log_in_message = self.browser.find_element_by_css_selector('h2')

        self.assertEqual(log_in_message.text, 'Log In')

  

  
