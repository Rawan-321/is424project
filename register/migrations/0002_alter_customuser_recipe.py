# Generated by Django 5.2 on 2025-04-24 18:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0008_remove_recipe_created_by_recipe_user'),
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='recipe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recipe.recipe'),
        ),
    ]
