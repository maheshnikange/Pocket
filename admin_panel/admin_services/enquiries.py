from django.shortcuts import render, redirect
from main.models import Enquiry
from django.db.models import Q
from vendor_panel.models import VendorService, Shop
from pocket_service.decorators import admin_required
import pytz


@admin_required
def get_enquiries_for_admin(request):
    enquiries = Enquiry.objects.all().order_by('-created_at')
    return render(request, 'admin/dashboard/enquiries.html', {'enquiries': enquiries})

def get_enquiries_for_admin(request):
    query = request.GET.get('query')
    field = request.GET.get('field')
    enquiries = Enquiry.objects.all()

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
        elif field == 'vendor':
            enquiries = enquiries.filter(Q(service__shop__user__first_name__icontains=query) | Q(service__shop__user__last_name__icontains=query))

    # Convert `created_at` to IST
    ist = pytz.timezone('Asia/Kolkata')
    for enquiry in enquiries:
        enquiry.created_at_ist = enquiry.created_at.astimezone(ist).strftime("%d-%m-%Y %H:%M %p") if enquiry.created_at else None

    return render(request, 'admin/dashboard/enquiries.html', {'enquiries': enquiries, 'query': query, 'field': field})

