import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.

class SkillCategory(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    skill_category = models.CharField(max_length=200)
    skill_category_description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.skill_category

class SkillSubCategory(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    
    skill_sub_category = models.CharField(max_length=200)
    skill_sub_category_description = models.CharField(max_length=200)

    def __str__(self):
        return self.skill_sub_category

class SkillMain(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    
    skill_name = models.CharField(max_length=200)
    skill_description = models.CharField(max_length=300)

    def __str__(self):
        return self.skill_name

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

class UserSkill(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    #user_skill = models.ManyToManyField(SkillMain)
    user_skill = models.ForeignKey(SkillMain, on_delete=models.CASCADE)
    user_skill_category = models.ManyToManyField(SkillCategory)
    user_skill_sub_category = models.ManyToManyField(SkillSubCategory)

    def get_absolute_url(self):
        return reverse('skills:user_skill_list')