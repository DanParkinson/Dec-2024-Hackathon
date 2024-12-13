from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse
from .models import Recipe


# Create your views here.

def recipes(request):
    "Render list of recipies to the recipies.html page"
    recipes_list = Recipe.objects.all()
    return render(request, 'christmas/recipes.html', {'recipes': recipes_list})

def recipe_detail(request, id):
    """Renders details of a single recipe to recipie_detail.html"""
    recipe = get_object_or_404(Recipe, id=id)
    context = {
        'recipe': recipe
    }

    return render(
        request,
        'christmas/recipe_detail.html',
        context
    )
