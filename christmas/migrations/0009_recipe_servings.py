# Generated by Django 4.2.17 on 2024-12-15 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('christmas', '0008_recipe_recommended'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='servings',
            field=models.IntegerField(default=4, help_text='Number of servings'),
        ),
    ]
