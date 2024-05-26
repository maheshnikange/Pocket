from django.contrib.auth.models import auth
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Category
from pocket_service.decorators import admin_required

# ============ Navigations ======================
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password =password  )
        if user is not None:
            auth.login(request , user)
            return redirect('dashboard')
        else:
            messages.info(request, 'invalid username or password')
            return render(request,'admin/login.html')
    else:
        return render(request,'admin/login.html')

def logout(request):
    auth.logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')

@admin_required
def dashboard(request):
    categories = Category.objects.all()
    return render(request, 'admin/dashboard/list-category.html', {'categories': categories})
