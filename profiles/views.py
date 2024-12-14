from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

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
    user = request.user # get currently logged in user
    return render(request, 'profiles/profile.html', {'user':user})
