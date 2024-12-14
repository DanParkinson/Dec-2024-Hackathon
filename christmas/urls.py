from . import views
from django.urls import path

urlpatterns = [
    path('', views.recipes, name='recipes'),
    path('recipe/<int:id>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/add/', views.add_recipe, name='add_recipe'),
    path('recipe/edit/<int:id>/', views.edit_recipe, name='edit_recipe'),
    path('recipe/delete/<int:id>/', views.delete_recipe, name='delete_recipe'),
    path('recipe/favourite/<int:id>/', views.toggle_favourite, name='toggle_favourite'),
]