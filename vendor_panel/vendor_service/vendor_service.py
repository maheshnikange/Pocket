
from django.shortcuts import render, redirect
from vendor_panel.forms import VendorServiceForm
from vendor_panel.models import Shop, VendorService
# Create your views here.
def vendor_service_list(request):
    user_shops = Shop.objects.filter(user = request.user)
    vendor_services = VendorService.objects.filter(shop__in=user_shops)
    return render(request, 'vendor/list-vendor-service.html', {'vendor_services': vendor_services})

def vendor_service_create(request):
    shops = Shop.objects.filter(user=request.user)
    if request.method == 'POST':
        form = VendorServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vendor_service_list')
    else:
        form = VendorServiceForm()
    return render(request, 'vendor/new-vendor-service.html', {'form': form, "shops": shops})

def vendor_service_update(request, pk):
    vendor_service = VendorService.objects.get(pk=pk)
    if request.method == 'POST':
        form = VendorServiceForm(request.POST, instance=vendor_service)
        if form.is_valid():
            form.save()
            return redirect('vendor_service_list')
    else:
        form = VendorServiceForm(instance=vendor_service)
    return render(request, 'vendor_panel/vendor_service_form.html', {'form': form})

def vendor_service_delete(request, pk):
    vendor_service = VendorService.objects.get(pk=pk)
    vendor_service.delete()
    return redirect('vendor_service_list')
