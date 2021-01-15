""" functional test"""

from django.contrib.auth import get_user_model
from skills.models import SkillMain, SkillCategory, SkillSubCategory, UserSkill
from .base import FunctionalTest
import time

class UserSkillAddTest(FunctionalTest):
    """ test user skill add test """

    def test_user_can_log_and_access_user_skill_add(self):
        """ create test user login and access user skill add """
        normal_user = get_user_model()
        user = normal_user.objects.create_user(username=self.correct_test_username,
                                               email=self.correct_test_useremail,
                                               password=self.correct_test_userpassword)
                                            
        self.assertEqual(user.username, self.correct_test_username)

        """ create and save user skill """
        self.skill_main = SkillMain.objects.create(skill_name='test_skill', skill_description='test_skill_description')
        self.skill_main.save()

        self.skill_cateogory = SkillCategory.objects.create(skill_category='test_category', skill_category_description='test_category_description')
        self.skill_cateogory.save()

        self.skill_sub_cateogory = SkillSubCategory.objects.create(skill_sub_category='test_sub_category', skill_sub_category_description='test_sub_category_description')
        self.skill_sub_cateogory.save()
        
        self.user_skill = UserSkill.objects.create(author=user, user_skill=self.skill_main)
        self.user_skill.user_skill_category.add(self.skill_cateogory)
        self.user_skill.user_skill_sub_category.add(self.skill_sub_cateogory)
        self.user_skill.save()
        self.assertIn(self.user_skill, UserSkill.objects.all())


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

        user_skill_add_link = self.browser.find_element_by_link_text('User Skill Add')

        self.assertEqual(user_skill_add_link.text, "User Skill Add")

        user_skill_add_link.click()

        user_skill_page = self.browser.find_element_by_css_selector('h1')

        self.assertEqual(user_skill_page.text, 'User Skill List')

