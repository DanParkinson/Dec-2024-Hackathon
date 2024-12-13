from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home-index'),  # Root URL for the 'home' app
]