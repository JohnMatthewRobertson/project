"""
    module created automatically
    when the following django command is run
    python manage.py startapp accounts
"""

from django.contrib import admin
from skills.models import SkillMain, SkillCategory, SkillSubCategory, UserSkill

# Register your models here.


@admin.register(SkillMain)
class SkillMainAdmin(admin.ModelAdmin):
    """ fields to display in admin """
    list_display = ('skill_name', 'skill_description', 'created', 'updated')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('skill_name',)


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    """ fields to display in admin """
    list_display = ('skill_category', 'skill_category_description', 'created', 'updated')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('skill_category',)


@admin.register(SkillSubCategory)
class SkillSubCategoryAdmin(admin.ModelAdmin):
    """ fields to display in admin """
    list_display = ('skill_sub_category', 'skill_sub_category_description', 'created', 'updated')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('skill_sub_category',)


@admin.register(UserSkill)
class UserSkillAdmin(admin.ModelAdmin):
    """" fields to display in admin """
    list_display = ('author', 'user_skill', 'created', 'updated', 'active', 'teach')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('author',)
