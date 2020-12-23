import unittest, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from webdriver_manager.firefox import GeckoDriverManager
from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth import get_user_model
from .base import FunctionalTest

class AuthenticationTest(FunctionalTest):

    def test_login_and_logout_successfully(self):

        self.test_username = 'testuserone'
        self.test_userpassword = 'testpass123'
        self.test_useremail = 'testuserone@email.com'

        User = get_user_model()
        user = User.objects.create_user(username=self.test_username, email=self.test_useremail, password=self.test_userpassword)

        self.assertEqual(user.username, self.test_username)
        self.assertEqual(user.email, self.test_useremail)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        login_link = self.browser.find_element_by_link_text('Log In')
        self.assertEqual(login_link.text, "Log In")

        login_link.click()

        username = self.browser.find_element_by_id('id_login')
        
        username.click()

        username.send_keys(self.test_useremail)

        password = self.browser.find_element_by_id('id_password')

        password.click()

        password.send_keys(self.test_userpassword)

        submit_buttom = self.browser.find_element_by_css_selector('button')

        submit_buttom.click()

        loggedin_message = self.browser.find_element_by_css_selector('h2')

        self.assertEqual(loggedin_message.text, 'Hi testuserone@email.com')

        logout_link = self.browser.find_element_by_link_text('Log Out')
        self.assertEqual(logout_link.text, "Log Out")

        logout_link.click()

        submit_buttom = self.browser.find_element_by_css_selector('button')

        submit_buttom.click()

        loggedout_message = self.browser.find_element_by_css_selector('h2')

        self.assertEqual(loggedout_message.text, 'You are not logged in')

    def test_unsuccessfull_login(self):

        self.test_username = 'testwronguser'
        self.test_userpassword = 'testpwrongpassword'
        self.test_useremail = 'testwrongemail@email.com'

        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        login_link = self.browser.find_element_by_link_text('Log In')
        self.assertEqual(login_link.text, "Log In")

        login_link.click()

        username = self.browser.find_element_by_id('id_login')
        
        username.click()

        username.send_keys(self.test_useremail)

        password = self.browser.find_element_by_id('id_password')

        password.click()

        password.send_keys(self.test_userpassword)

        submit_buttom = self.browser.find_element_by_css_selector('button')

        submit_buttom.click()

        html_list = self.browser.find_element_by_css_selector('div.alert.alert-block.alert-danger')
    
        self.assertEqual(html_list.text, 'The e-mail address and/or password you specified are not correct.')
       



