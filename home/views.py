from django.shortcuts import render

# Create your views here.


def index(request):
    """
    A view to return the home page
    """
    return render(request, 'home/index.html')


def about(request):
    """
    A view to return the about page
    """
    return render(request, 'christmas/about.html')
