from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Recipe
from .forms import RecipeForm


def recipes(request):
    "Render list of recipies to the recipies.html page"
    recipes_list = Recipe.objects.all()
    return render(
        request,
        'christmas/recipes.html',
        {'recipes': recipes_list}
    )

def recipe_detail(request, id):
    """Renders details of a single recipe to recipie_detail.html"""
    recipe = get_object_or_404(Recipe, id=id)
    recipes_list = Recipe.objects.all()
    context = {
        'recipe': recipe,
        'recipes_list': recipes_list
    }

    return render(
        request,
        'christmas/recipe_detail.html',
        context
    )


def add_recipe(request):
    """Add a recipe to the database"""
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            messages.success(request, 'Recipe added successfully!')
            # change the redirect to 'recipe_detail', id=recipe.id when the page ready
            return redirect('recipes')
    else:
        form = RecipeForm()

    return render(request, 'christmas/add_recipe.html', {'form': form})


def edit_recipe(request, id):
    """Edit a recipe in the database"""
    recipe = get_object_or_404(Recipe, id=id)
    
    if request.user != recipe.author:
        messages.error(request, "You can only edit your own recipes!")
        return redirect('recipe_detail', id=recipe.id)
    
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            messages.success(request, 'Recipe updated successfully!')
            # change the redirect to 'recipe_detail', id=recipe.id when the page ready
            return redirect('recipes')
    else:
        form = RecipeForm(instance=recipe)
    
    return render(request, 'christmas/edit_recipe.html', {
        'form': form,
        'recipe': recipe
    })


def delete_recipe(request, id):
    """Delete a recipe from the database"""
    recipe = get_object_or_404(Recipe, id=id)
    
    if request.user != recipe.author:
        messages.error(request, "You can only delete your own recipes!")
        return redirect('recipe_detail', id=recipe.id)
    
    if request.method == 'POST':
        recipe.delete()
        messages.success(request, 'Recipe deleted successfully!')
        return redirect('recipes')
    
    return render(request, 'christmas/delete_recipe.html', {'recipe': recipe})