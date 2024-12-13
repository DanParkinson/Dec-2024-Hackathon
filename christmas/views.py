from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse
from .models import Recipe


# Create your views here.
def index(request):
    return render(request, 'christmas/index.html')

def about(request):
    return render(request, 'christmas/about.html')

def recipes(request):
    recipes_list = Recipe.objects.all()
    return render(request, 'christmas/recipes.html', {'recipes': recipes_list})

def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    context = {
        'recipe': recipe
    }

    return render(
        request,
        'christmas/recipe_detail.html',
        context
    )
