from django.contrib.auth.models import auth
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from admin_panel.models import Advertise, Images
from admin_panel.forms import AdvertiseForm, ImagesForm
from pocket_service.decorators import admin_required

@admin_required
def advertise_list(request):
    advertises = Advertise.objects.all()
    return render(request, 'admin/dashboard/list-advertise.html', {'advertises': advertises})

@admin_required
def advertise_detail(request, pk):
    advertise = get_object_or_404(Advertise, pk=pk)
    return render(request, 'advertise_detail.html', {'advertise': advertise})

@admin_required
def advertise_create(request):
    if request.method == 'POST':
        form = AdvertiseForm(request.POST)
        image_form = ImagesForm(request.POST, request.FILES)
        if form.is_valid() and image_form.is_valid():
            image_instance = image_form.save()
            category_instance = form.save(commit=False)
            category_instance.image = image_instance
            category_instance.save()
            return redirect('advertise_list')
    else:
        form = AdvertiseForm()
    return render(request, 'admin/dashboard/new-advertise.html', {'form': form})

@admin_required
def advertise_update(request, pk):
    advertise = get_object_or_404(Advertise, pk=pk)
    if request.method == 'POST':
        image = get_object_or_404(Images, pk=advertise.image_id)
        form = AdvertiseForm(request.POST)
        image_form = ImagesForm(request.POST, request.FILES, instance=image)
        if form.is_valid() and image_form.is_valid():
            image_instance = image_form.save()
            category_instance = form.save(commit=False)
            category_instance.image = image_instance
            category_instance.save()
            return redirect('advertise_list')
    else:
        form = AdvertiseForm(instance=advertise)
    return render(request, 'admin/dashboard/new-advertise.html', {'form': form, "advertise": advertise})

@admin_required
def advertise_delete(request, pk):
    advertise = get_object_or_404(Advertise, pk=pk)
    ad_image = advertise.image
    advertise.delete()
    ad_image.delete()
    return redirect('advertise_list')
