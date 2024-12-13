from . import views
from django.urls import path

urlpatterns = [
    path('', views.recipes, name='recipes'),
    path('detail/<int:id>/', views.recipe_detail, name='recipe-detail'),
    path('recipe/add/', views.add_recipe, name='add_recipe')
]