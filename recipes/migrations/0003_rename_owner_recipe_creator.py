# Generated by Django 4.1.7 on 2023-03-09 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_recipe_recipe_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='owner',
            new_name='creator',
        ),
    ]
