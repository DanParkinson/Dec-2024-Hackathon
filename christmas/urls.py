from . import views
from django.urls import path

urlpatterns = [
    path('recipes/', views.recipes, name='recipes'),
    path('detail/<int:id>/', views.recipe_detail, name='recipe-detail'),
]