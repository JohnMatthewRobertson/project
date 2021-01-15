""" functional test"""

from django.contrib.auth import get_user_model
from skills.models import SkillMain, SkillCategory, SkillSubCategory, UserSkill
from .base import FunctionalTest
import time

class TeamSkillTest(FunctionalTest):
    """ test user login in and team skill search"""

    def test_user_can_log_in_and_leave_feedback(self):
        """ test user for login in and team skill search """
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

        team_skill_link = self.browser.find_element_by_link_text('Team Skill')
        self.assertEqual(team_skill_link.text, "Team Skill")

        team_skill_link.click()

        team_skill_page = self.browser.find_element_by_css_selector('h1')

        self.assertEqual(team_skill_page.text, 'Team Skill')



