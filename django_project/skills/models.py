""" better comment """

import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.


class PublishedSkillCategoryManager(models.Manager):
    """ better comment """

    def get_queryset(self):
        """ better comment """
        return super(PublishedSkillCategoryManager, self).get_queryset().filter()


class SkillCategory(models.Model):
    """ better comment """

    objects = models.Manager()  # default manager
    publishedSkillCategory = PublishedSkillCategoryManager()  # custom manager

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    skill_category = models.CharField(max_length=200, unique=True)
    skill_category_description = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        """ better comment """
        return self.skill_category


class PublishedSkillSubManager(models.Manager):
    """ better comment """

    def get_queryset(self):
        """ better comment """
        return super(PublishedSkillSubManager, self).get_queryset().filter()


class SkillSubCategory(models.Model):
    """ better comment """

    objects = models.Manager()  # default manager
    publishedSkillSub = PublishedSkillSubManager()  # custom manager

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    skill_sub_category = models.CharField(max_length=200, unique=True)
    skill_sub_category_description = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        """ better comment """
        return self.skill_sub_category


class PublishedSkillManager(models.Manager):
    """ better comment """

    def get_queryset(self):
        """ better comment """
        return super(PublishedSkillManager, self).get_queryset().filter()


class SkillMain(models.Model):
    """ better comment """
    objects = models.Manager()  # default manager
    publishedSkill = PublishedSkillManager()  # custom manager

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    skill_name = models.CharField(max_length=200, unique=True)
    skill_description = models.TextField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        """ better comment """
        return self.skill_name


class PublishedUserSkillManager(models.Manager):
    """ better comment """

    def get_queryset(self):
        """ better comment """
        return super(PublishedUserSkillManager, self).get_queryset().filter()


class UserSkill(models.Model):
    """ better comment """

    objects = models.Manager()  # default manager
    publishedUserSkill = PublishedUserSkillManager()  # custom manager

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    user_skill = models.ForeignKey(SkillMain, on_delete=models.CASCADE)
    user_skill_category = models.ManyToManyField(SkillCategory)
    user_skill_sub_category = models.ManyToManyField(SkillSubCategory)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    teach = models.BooleanField(default=False)

    class Meta:
        """ better comment """
        ordering = ('-user_skill',)
        unique_together = ('author', 'user_skill',)

    def get_absolute_url(self):
        """ better comment """
        return reverse('skills:user_skill_list')
