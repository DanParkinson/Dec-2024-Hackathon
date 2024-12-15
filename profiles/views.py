from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from christmas.models import Recipe


# Dan - users are sent to confirmation page when loging out
# then redirected to home page
@login_required
def logout_confirmation(request):
    if request.method == "POST":
        logout(request)
        return redirect('/')
    return render(request, 'account/logout.html')


# Dan - users can view own profile
@login_required
def profile_view(request):
    """render profile information """
    # get currently logged in user
    user = request.user
    # fetch recipes created by user
    recipes = Recipe.objects.filter(author=user)
    # fetch Recipes favourited by the user
    favourite_recipes = user.favourite_recipes.all()
    return render(request, 'profiles/profile.html', {
        'user': user,
        'recipes': recipes,
        'favourite_recipes': favourite_recipes, })
