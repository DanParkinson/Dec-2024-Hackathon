from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def logout_confirmation(request):
    if request.method == "POST":
        logout(request)
        return redirect('/')
    return render(request, 'account/logout.html') 
