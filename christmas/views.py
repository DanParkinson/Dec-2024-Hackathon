from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
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


@login_required
def add_recipe(request):
    """Add a recipe to the database"""
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            messages.success(request, 'Recipe added successfully!')
            return redirect('detail', id=recipe.id)
    else:
        form = RecipeForm()

    return render(request, 'christmas/add_recipe.html', {'form': form})


@login_required
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
            return redirect('detail', id=recipe.id)
    else:
        form = RecipeForm(instance=recipe)
    
    return render(request, 'christmas/edit_recipe.html', {
        'form': form,
        'recipe': recipe
    })


@login_required
def delete_recipe(request, id):
    """Delete a recipe from the database"""
    recipe = get_object_or_404(Recipe, id=id)
    
    if request.user != recipe.author:
        messages.error(request, "You can only delete your own recipes!")
        return redirect('recipe_detail', id=recipe.id)
    
    if request.method == 'POST':
        recipe.delete()
        messages.success(request, 'Recipe deleted successfully!')
        return redirect('recipe_detail', id=recipe.id)
    
    return render(request, 'christmas/delete_recipe.html', {'recipe': recipe})

# Dan - users can toggle favourites
@login_required
def toggle_favourite(request, id):
    """Toggle a recipe as a favourite for the logged-in user."""
    recipe = get_object_or_404(Recipe, id=id)
    if recipe.favourites.filter(id=request.user.id).exists():
        recipe.favourites.remove(request.user)
    else:
        recipe.favourites.add(request.user)
    # Redirect back to the previous page
    return redirect(request.META.get('HTTP_REFERER', '/'))