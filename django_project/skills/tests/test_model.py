from django.test import TestCase
from django.urls import reverse
from skills.models import Skill

# Create your tests here.

class SkillTest(TestCase):

    def setUp(self):
        self.skill = Skill.objects.create(
            skill_name = 'Java',
            skill_description = 'Java is a class-based, object-oriented programming language that is designed to have as few implementation dependencies as possible. It is a general-purpose programming language intended to let application developers write once, run anywhere,'
        )
        

    def test_skill_listing(self):
        self.assertEqual(self.skill.skill_name, 'Java')
        self.assertEqual(self.skill.skill_description, 'Java is a class-based, object-oriented programming language that is designed to have as few implementation dependencies as possible. It is a general-purpose programming language intended to let application developers write once, run anywhere,')
        
    def test_skill_list_view(self):
        response = self.client.get(reverse('skills:skill_list'))
        self.assertEqual(response.status_code, 200)

    def test_skill_uses_skill_template(self):
        response = self.client.get(reverse('skills:skill_list'))
        self.assertTemplateUsed(response, 'skills/skill_list.html')

    def test_skill_detail_view(self):
        response = self.client.get(self.skill.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    
