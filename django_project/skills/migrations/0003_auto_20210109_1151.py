# Generated by Django 3.1.4 on 2021-01-09 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0002_auto_20210109_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skillcategory',
            name='skill_category_description',
            field=models.TextField(max_length=200),
        ),
    ]
