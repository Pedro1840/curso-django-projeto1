# Generated by Django 4.2.1 on 2023-05-24 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_recipe_author_recipe_caregory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='caregory',
            new_name='category',
        ),
    ]
