from django.contrib import admin
from .models import Recipe
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    list_display = ('author',
                    'status',
                    'title',)
    search_fields = ['author', 'status']
    list_filter = ('author', 'status')
    filter_horizontal = ('favorites',)  # Dan - Allow easy management of favorites in the admin

