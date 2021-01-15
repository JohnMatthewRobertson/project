""" better documents """
from django.test import TestCase
from django.contrib.auth import get_user_model
from skills.models import SkillMain, SkillCategory, SkillSubCategory, UserSkill


# Create your tests here.


class SkillModelTest(TestCase):
    """ test creating a skill """
    def setUp(self):
        """ create a test user """
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'testuser@email.com',
            password = 'testpass123',
        )

    def test_create_skill_category(self):
        """ create and save skill """
        self.skill_cateogory = SkillCategory.objects.create(skill_category='test_category', skill_category_description='test_category_description')
        self.skill_cateogory.save()
        self.assertIn(self.skill_cateogory, SkillCategory.objects.all())

    def test_create_skill_sub_category(self):
        """ create and save sub skill """
        self.skill_sub_cateogory = SkillSubCategory.objects.create(skill_sub_category='test_sub_category', skill_sub_category_description='test_sub_category_description')
        self.skill_sub_cateogory.save()
        self.assertIn(self.skill_sub_cateogory, SkillSubCategory.objects.all())

    def test_create_skill(self):
        """ create and save skill """
        self.skill_main = SkillMain.objects.create(skill_name='test_skill', skill_description='test_skill_description')
        self.skill_main.save()
        self.assertIn(self.skill_main, SkillMain.objects.all())

    def test_create_user_skill(self):
        """ create and save user skill """
        self.skill_main = SkillMain.objects.create(skill_name='test_skill', skill_description='test_skill_description')
        self.skill_main.save()

        self.skill_cateogory = SkillCategory.objects.create(skill_category='test_category', skill_category_description='test_category_description')
        self.skill_cateogory.save()

        self.skill_sub_cateogory = SkillSubCategory.objects.create(skill_sub_category='test_sub_category', skill_sub_category_description='test_sub_category_description')
        self.skill_sub_cateogory.save()
        
        self.user_skill = UserSkill.objects.create(author=self.user, user_skill=self.skill_main)
        self.user_skill.user_skill_category.add(self.skill_cateogory)
        self.user_skill.user_skill_sub_category.add(self.skill_sub_cateogory)
        self.user_skill.save()
        self.assertIn(self.user_skill, UserSkill.objects.all())




