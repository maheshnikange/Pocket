from django.contrib.auth.models import auth
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from admin_panel.models import Category, Images
from admin_panel.forms import CategoryForm, ImagesForm
from vendor_panel.models import ShopCategory
from pocket_service.decorators import admin_required


@admin_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'admin/dashboard/list-category.html', {'categories': categories, "user" :request.user})

@admin_required
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'category_detail.html', {'category': category})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        image_form = ImagesForm(request.POST, request.FILES)
        if form.is_valid() and image_form.is_valid():
            image_instance = image_form.save()
            category_instance = form.save(commit=False)
            category_instance.image = image_instance
            category_instance.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'admin/dashboard/new-category.html', {'form': form})

@admin_required
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        image = get_object_or_404(Images, pk=category.image_id)
        form = CategoryForm(request.POST, instance=category)
        image_form = ImagesForm(request.POST, request.FILES, instance=image)
        if form.is_valid() and image_form.is_valid():
            image_instance = image_form.save()
            category_instance = form.save(commit=False)
            category_instance.image = image_instance
            category_instance.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'admin/dashboard/new-category.html', {'form': form, 'category': category})

@admin_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    associated_services = ShopCategory.objects.filter(category=category)
    associated_services.delete()
    category.delete()
    category.image.delete()
    return redirect('category_list')
