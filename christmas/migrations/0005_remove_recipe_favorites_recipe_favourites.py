# Generated by Django 4.2.17 on 2024-12-14 13:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('christmas', '0004_alter_recipe_options_recipe_favorites'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='favorites',
        ),
        migrations.AddField(
            model_name='recipe',
            name='favourites',
            field=models.ManyToManyField(blank=True, related_name='favourite_recipes', to=settings.AUTH_USER_MODEL),
        ),
    ]
