""" functional test"""

from django.contrib.auth import get_user_model
from .base import FunctionalTest
import time

class SkillListTest(FunctionalTest):
    """ test the skill list view and skill search """

    def test_user_can_log_and_access_skill_list(self):
        """ create test user login and access skill list link """
        normal_user = get_user_model()
        user = normal_user.objects.create_user(username=self.correct_test_username,
                                               email=self.correct_test_useremail,
                                               password=self.correct_test_userpassword)
                                            
        self.assertEqual(user.username, self.correct_test_username)

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

        loggedin_message = self.browser.find_element_by_css_selector('h1')

        self.assertEqual(loggedin_message.text, 'Home')

        skill_list_link = self.browser.find_element_by_link_text('Skill List')
        self.assertEqual(skill_list_link.text, "Skill List")

        skill_list_link.click()

        skill_list_page = self.browser.find_element_by_css_selector('h1')

        self.assertEqual(skill_list_page.text, 'Skill List')

    def test_user_can_log_and_access_skill_list_and_perform_search(self):
        """ create test user login and access skill list link and perform search """
        normal_user = get_user_model()
        user = normal_user.objects.create_user(username=self.correct_test_username,
                                               email=self.correct_test_useremail,
                                               password=self.correct_test_userpassword)
                                            
        self.assertEqual(user.username, self.correct_test_username)

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

        loggedin_message = self.browser.find_element_by_css_selector('h1')

        self.assertEqual(loggedin_message.text, 'Home')

        skill_list_link = self.browser.find_element_by_link_text('Skill List')
        self.assertEqual(skill_list_link.text, "Skill List")

        skill_list_link.click()

        skill_list_page = self.browser.find_element_by_css_selector('h1')

        self.assertEqual(skill_list_page.text, 'Skill List')

        search = self.browser.find_element_by_name('q')

        search.click()

        search.send_keys('Python')

        submit_search = self.browser.find_element_by_css_selector('.btn')

        submit_search.click()

        skill_search_results_page = self.browser.find_element_by_css_selector('h1')

        self.assertEqual(skill_search_results_page.text, 'Skill Search Results')





