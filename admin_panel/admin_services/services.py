from django.contrib.auth.models import auth
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from admin_panel.models import Category, Service, Images
from admin_panel.forms import ServiceForm, ImagesForm
from pocket_service.decorators import admin_required

@admin_required
def service_list(request):
    services = Service.objects.all()
    return render(request, 'admin/dashboard/list-service.html', {'services': services})

@admin_required
def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'service_detail.html', {'service': service})

@admin_required
def service_create(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        image_form = ImagesForm(request.POST, request.FILES)
        if form.is_valid() and image_form.is_valid():
            image_instance = image_form.save()
            category_instance = form.save(commit=False)
            category_instance.image = image_instance
            category_instance.save()
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'admin/dashboard/new-service.html', {'form': form, "categories": categories})

@admin_required
def service_update(request, pk):
    service = get_object_or_404(Service, pk=pk)
    categories = Category.objects.all()
    if request.method == 'POST':
        image = get_object_or_404(Images, pk=service.image_id)
        form = ServiceForm(request.POST, instance=service)
        image_form = ImagesForm(request.POST, request.FILES, instance=image)
        if form.is_valid() and image_form.is_valid():
            image_instance = image_form.save()
            category_instance = form.save(commit=False)
            category_instance.image = image_instance
            category_instance.save()
            return redirect('service_list')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'admin/dashboard/new-service.html', {'form': form, "categories": categories, "service": service})

@admin_required
def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    service_image = service.image
    service.delete()
    service_image.delete()
    return redirect('service_list')
