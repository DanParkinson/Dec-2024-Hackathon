from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from .models import Recipe, CATEGORY_CHOICES
from .forms import RecipeForm
from django.db.models import Q, Count

def recipes(request):
    """Render list of recipes to the recipes.html page"""
    recipes_list = Recipe.objects.all().annotate(favourites_count=Count('favourites'))
    query = None
    category = None
    no_results = False

    if request.GET:
        # Search Query
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('recipes'))

            queries = Q(title__icontains=query) | Q(description__icontains=query)
            recipes_list = recipes_list.filter(queries)

        # Category filtering
        if 'category' in request.GET:
            category = request.GET['category']
            if category:
                recipes_list = recipes_list.filter(category=category)

    # If there is no result
    if not recipes_list.exists():
        no_results = True

    # Add the is_favorited flag to each recipe (only if user is authenticated)
    if request.user.is_authenticated:
        for recipe in recipes_list:
            recipe.is_favorited = recipe.favourites.filter(id=request.user.id).exists()
    else:
        # If the user is not authenticated, set `is_favorited` to False for all recipes
        for recipe in recipes_list:
            recipe.is_favorited = False

    context = {
        'recipes': recipes_list,
        'search_term': query,
        'current_category': category,
        'category_choices': CATEGORY_CHOICES,
        'no_results': no_results,
    }

    return render(request, 'christmas/recipes.html', context)

def recipe_detail(request, id):
    """Renders details of a single recipe to recipe_detail.html"""
    recipe = get_object_or_404(Recipe, id=id)
    is_favorited = False
    if request.user.is_authenticated:
        is_favorited = recipe.favourites.filter(id=request.user.id).exists()
    
    favourites_count = recipe.favourites.count()

    context = {
        'recipe': recipe,
        'is_favorited': is_favorited,
        'favourites_count': favourites_count,
    }

    return render(request, 'christmas/recipe_detail.html', context)


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
            return redirect('recipe_detail', id=recipe.id)
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
            return redirect('recipe_detail', id=recipe.id)
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
        return redirect('recipes')
    
    return render(request, 'christmas/delete_recipe.html', {'recipe': recipe})

# Dan - users can toggle favourites
@login_required
def toggle_favourite(request, id):
    """Toggle a recipe as a favourite for the logged-in user."""
    recipe = get_object_or_404(Recipe, id=id)
    is_favorited = recipe.favourites.filter(id=request.user.id).exists()

    if is_favorited:
        recipe.favourites.remove(request.user)
    else:
        recipe.favourites.add(request.user)

    # Redirect back to the previous page, passing the is_favorited flag
    return redirect(request.META.get('HTTP_REFERER', 'recipe-list') + f"?favorited={not is_favorited}")

