from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('recipes/', views.recipes, name='recipes'),
]