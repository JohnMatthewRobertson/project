from django.contrib import admin
from skills.models import Skill, SkillCategory, SkillSubCategory, SkillMain, UserSkill

# Register your models here.

class SkillAdmin(admin.ModelAdmin):
    list_display = ("skill_name", "skill_description",)

class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ("skill_category", "skill_category_description",)


class SkillSubCategoryAdmin(admin.ModelAdmin):
    list_display = ("skill_sub_category", "skill_sub_category_description",)


class SkillMainAdmin(admin.ModelAdmin):
    list_display = ('skill_name', 'skill_description',)

class UserSkillAdmin(admin.ModelAdmin):
    list_display = ('author',)

admin.site.register(Skill, SkillAdmin)
admin.site.register(SkillCategory, SkillCategoryAdmin)
admin.site.register(SkillSubCategory, SkillSubCategoryAdmin)
admin.site.register(SkillMain, SkillAdmin)
admin.site.register(UserSkill, UserSkillAdmin)
