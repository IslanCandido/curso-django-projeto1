# Generated by Django 4.0.3 on 2022-04-03 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_alter_recipe_author_delete_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='preparetion_time',
            new_name='preparation_time',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='preparetion_time_unit',
            new_name='preparation_time_unit',
        ),
    ]