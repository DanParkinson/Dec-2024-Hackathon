from django.contrib import admin
from .models import Recipe
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    list_display = ('author',
                    'status',
                    'title',
                    'category',
                    'recommended',
                    'servings',)
    list_editable = ('recommended',)
    search_fields = ['author', 'status']
    list_filter = ('author', 'status', 'category', 'recommended')
    filter_horizontal = ('favourites',)
