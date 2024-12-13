from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('recipes/', views.recipes, name='recipes'),
    path('detail/<int:id>/', views.recipe_detail, name='recipe-detail'),
]