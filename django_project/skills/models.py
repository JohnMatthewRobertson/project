import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.

class PublishedSkillCategoryManager(models.Manager):

    def get_queryset(self):
        return super(PublishedSkillCategoryManager, self).get_queryset().filter()

class SkillCategory(models.Model):

    objects = models.Manager() # default manager
    publishedSkillCategory = PublishedSkillCategoryManager() # custom manager
    
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    skill_category = models.CharField(max_length=200, unique=True)
    skill_category_description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.skill_category


class PublishedSkillSubManager(models.Manager):

    def get_queryset(self):
        return super(PublishedSkillSubManager, self).get_queryset().filter()

class SkillSubCategory(models.Model):

    objects = models.Manager() # default manager
    publishedSkillSub = PublishedSkillSubManager() # custom manager

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    
    skill_sub_category = models.CharField(max_length=200, unique=True)
    skill_sub_category_description = models.CharField(max_length=200)

    def __str__(self):
        return self.skill_sub_category


class PublishedSkillManager(models.Manager):

    def get_queryset(self):
        return super(PublishedSkillManager, self).get_queryset().filter()


class SkillMain(models.Model):


    objects = models.Manager() # default manager
    publishedSkill = PublishedSkillManager() # custom manager

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    
    skill_name = models.CharField(max_length=200, unique=True)
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

    class Meta:
        ordering = ('-skill_name',)

    def __str__(self):
        return self.skill_name

    def get_absolute_url(self):
        return reverse('skills:skill_detail', args=[str(self.id)])

class PublishedUserSkillManager(models.Manager):

    def get_queryset(self):
        return super(PublishedUserSkillManager, self).get_queryset().filter()

class UserSkill(models.Model):

    
    objects = models.Manager() # default manager
    publishedUserSkill = PublishedUserSkillManager() # custom manager

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


    class Meta:
        ordering = ('-user_skill',)
        unique_together = ('author', 'user_skill',)

    def get_absolute_url(self):
        return reverse('skills:user_skill_list')