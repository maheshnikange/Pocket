from django.shortcuts import render, redirect
from admin_panel.models import Advertise, Category, Service
from vendor_panel.models import VendorService
from .forms import EnquiryForm


def index(request):
    categories = Category.objects.filter()
    slide_images = Advertise.objects.filter(location='dashboard', image_type='slider')
    static_images = Advertise.objects.filter(location='dashboard', image_type='static')
    
    return render(request,'index.html', {"slide_images": slide_images, "static_images": static_images, "categories": categories})

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')


def get_admin_category_services(request, cat_id):
    services = Service.objects.filter(category_id=cat_id)
    static_images = Advertise.objects.filter(location='category', image_type='static')
    if len(static_images)> 0:
        static_images = static_images[0]
    return render(request,'shop-catergory-page.html', {"admin_services": services, "cat_image": static_images}) 

def get_service_shop(request, service_id):
    vendor_services = VendorService.objects.filter(service_id=service_id)
    return render(request,'vendor-shop-lists.html', {"shop_list": vendor_services}) 

def service_enquiry(request, service_id):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index') 
        else:
            return render(request, 'get-appointment.html', {"service_id": service_id})
    else:
        return render(request, 'get-appointment.html', {"service_id": service_id})
