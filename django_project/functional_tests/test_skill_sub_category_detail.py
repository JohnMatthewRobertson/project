""" functional test"""

from django.contrib.auth import get_user_model
from skills.models import SkillMain, SkillCategory, SkillSubCategory, UserSkill
from .base import FunctionalTest
import time

class SkillSubCategoryDetailTest(FunctionalTest):
    """ test the skill Sub Category detail view and skill Sub Category detail edit """

    def test_user_can_log_and_access_skill_sub_category_detail(self):
        """ create test user login and access skill Sub Category detail link """
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

        skill_sub_category_detail_link = self.browser.find_element_by_link_text('Skill Sub Category Detail')

        self.assertEqual(skill_sub_category_detail_link.text, "Skill Sub Category Detail")

        skill_sub_category_detail_link.click()

        skill_sub_category_detail_page = self.browser.find_element_by_css_selector('h1')

        self.assertEqual(skill_sub_category_detail_page.text, 'Skill Sub Category Detail')

    def test_user_can_log_and_access_skill_sub_category_detail_and_access_edit(self):
        """ create test user login and access skill Sub Category Detail link access edit """
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

        skill_sub_category_detail_link = self.browser.find_element_by_link_text('Skill Sub Category Detail')
        
        self.assertEqual(skill_sub_category_detail_link.text, "Skill Sub Category Detail")

        skill_sub_category_detail_link.click()

        skill_sub_category_detail_page = self.browser.find_element_by_css_selector('h1')

        self.assertEqual(skill_sub_category_detail_page.text, 'Skill Sub Category Detail')








