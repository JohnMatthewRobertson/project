import uuid
from django.db import models
from django.urls import reverse


# Create your models here.

class SkillCategory(models.Model):
    skill_category = models.CharField(max_length=200)
    skill_category_description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.skill_category

class SkillSubCategory(models.Model):
    skill_sub_category = models.CharField(max_length=200)
    skill_sub_category_description = models.CharField(max_length=200)

    def __str__(self):
        return self.skill_sub_category

class Skill(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    
    skill_name = models.CharField(max_length=200)
    skill_description = models.CharField(max_length=300)
    skill_category = models.ManyToManyField(SkillCategory)
    skill_sub_category = models.ManyToManyField(SkillSubCategory)


    def __str__(self):
        return self.skill_name

    def get_absolute_url(self):
        return reverse('skills:skill_detail', args=[str(self.id)])
