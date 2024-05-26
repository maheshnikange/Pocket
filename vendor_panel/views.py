from django.shortcuts import render, redirect
from .models import Shop
from admin_panel.models import Category, Service
from django.http import JsonResponse
from pocket_service.decorators import login_required
# Create your views here.

@login_required
def dashboard(request):
    return render(request,'vendor/list-shop.html') 

@login_required
def get_shop_categories(request, shop_id):
    shop = Shop.objects.get(pk=shop_id)
    categories = shop.categories().values('id', 'name')
    return JsonResponse(list(categories), safe=False)

@login_required
def get_category_services(request, category_id):
    category = Category.objects.get(pk=category_id)
    services = category.service_set.values('id', 'name')
    return JsonResponse(list(services), safe=False)

@login_required
def get_service_price(request, service_id):
    service = Service.objects.get(pk=service_id)
    price = service.price
    data = {
        'id': service.id,
        'price': price,
    }
    return JsonResponse(data)