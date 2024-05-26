from django.shortcuts import render, redirect
from main.models import Enquiry
from vendor_panel.models import VendorService, Shop
from pocket_service.decorators import login_required
from django.db.models import Q
import pytz

@login_required
def get_enquiries_for_user(request):
    user_shops = Shop.objects.filter(user=request.user)
    user_vendor_services = VendorService.objects.filter(shop__in=user_shops)
    enquiries = Enquiry.objects.filter(service__in=user_vendor_services).order_by('-created_at')
    ist = pytz.timezone('Asia/Kolkata')
    for enquiry in enquiries:
        enquiry.created_at_ist = enquiry.created_at.astimezone(ist) if enquiry.created_at else None
    return render(request, 'vendor/enquiries.html', {'enquiries': enquiries})
    
# def search_vendor_enqueries(request):
#     query = request.GET.get('query')
#     user_shops = Shop.objects.filter(user=request.user)
#     user_vendor_services = VendorService.objects.filter(shop__in=user_shops)
#     enquiries = Enquiry.objects.filter(service__in=user_vendor_services)

#     if query:
#         enquiries = enquiries.filter(
#             Q(name__icontains=query) |
#             Q(mobile_number__icontains=query) |
#             Q(created_at__icontains=query)
#         ).distinct()
    
#     # Convert `created_at` to IST
#     ist = pytz.timezone('Asia/Kolkata')
#     for enquiry in enquiries:
#         enquiry.created_at_ist = enquiry.created_at.astimezone(ist)

#     return render(request, 'vendor/enquiries.html', {'enquiries': enquiries})


def search_vendor_enqueries(request):
    query = request.GET.get('query')
    field = request.GET.get('field')
    user_shops = Shop.objects.filter(user=request.user)
    user_vendor_services = VendorService.objects.filter(shop__in=user_shops)
    enquiries = Enquiry.objects.filter(service__in=user_vendor_services)

    if query and field:
        if field == 'name':
            enquiries = enquiries.filter(Q(name__icontains=query))
        elif field == 'mobile_number':
            enquiries = enquiries.filter(Q(mobile_number__icontains=query))
        elif field == 'created_at':
            enquiries = enquiries.filter(Q(created_at__icontains=query))
        elif field == 'shop':
            enquiries = enquiries.filter(Q(service__shop__name__icontains=query))
        elif field == 'category':
            enquiries = enquiries.filter(Q(service__service__category__name__icontains=query))
        elif field == 'service':
            enquiries = enquiries.filter(Q(service__service__name__icontains=query))

    # Convert `created_at` to IST
    ist = pytz.timezone('Asia/Kolkata')
    for enquiry in enquiries:
        enquiry.created_at_ist = enquiry.created_at.astimezone(ist) if enquiry.created_at else None

    return render(request, 'vendor/enquiries.html', {'enquiries': enquiries})
