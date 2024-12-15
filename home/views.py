from django.shortcuts import render
from christmas.models import Recipe

# Create your views here.


def index(request):
    """
    A view to return the home page with recommended recipes
    """
    recommended_recipes = Recipe.objects.filter(recommended=True, status=1)[:7]  # noqa

    return render(
        request,
        'home/index.html',
        {'recommended_recipes': recommended_recipes}
    )


def about(request):
    """
    A view to return the about page
    """
    return render(request, 'home/about.html')
