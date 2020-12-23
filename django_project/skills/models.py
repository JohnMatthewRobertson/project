from django.db import models

# Create your models here.

class Skill(models.Model):
    skill_name = models.CharField(max_length=200)
    skill_description = models.CharField(max_length=300)


    def __str__(self):
        print("john model", self.skill_name)
        return self.skill_name
