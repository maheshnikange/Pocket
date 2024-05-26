from django.shortcuts import render, redirect
from vendor_panel.forms import ShopForm
from vendor_panel.models import Shop, ShopCategory
from admin_panel.models import Category
from django.db import transaction
# Create your views here.
from pocket_service.decorators import login_required


@login_required
def shop_list(request):
    shops = Shop.objects.filter(user= request.user)
    return render(request, 'vendor/list-shop.html', {'shops': shops})

@login_required
def shop_detail(request, pk):
    category_names = [category.name for category in shop.categories()]
    shop = Shop.objects.get(pk=pk)
    return render(request, 'shop_detail.html', {'shop': shop})


@login_required
def shop_create(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        
        form = ShopForm(request.POST, request.FILES)
        if form.is_valid():
            shop = form.save(commit=False)  # Save the shop object without committing to the database
            shop.user_id = request.user.id
            shop.save()  # Save the shop object to generate an ID

            # Extract selected category IDs from the request
            category_ids = request.POST.getlist('categories')

            # Create ShopCategory objects to associate the shop with its categories
            for category_id in category_ids:
                category = Category.objects.get(pk=category_id)
                ShopCategory.objects.create(shop=shop, category=category)

            return redirect('shop_list')
    else:
        form = ShopForm()
    return render(request, 'vendor/new-shop.html', {'form': form, "categories": categories})

@login_required
def shop_update(request, pk):
    categories = Category.objects.all()
    shop = Shop.objects.get(pk=pk)
    if request.method == 'POST':
        form = ShopForm(request.POST, request.FILES, instance=shop)
        if form.is_valid():
            shop = form.save(commit=False)  # Save the shop object without committing to the database
            shop.save()  # Save the shop object to generate an ID

            # Extract selected category IDs from the request
            category_ids = request.POST.getlist('categories')

            # Create ShopCategory objects to associate the shop with its categories
            for category_id in category_ids:
                category = Category.objects.get(pk=category_id)
                ShopCategory.objects.create(shop=shop, category=category)

            return redirect('shop_list')
    else:
        form = ShopForm(instance=shop)
    return render(request, 'vendor/new-shop.html', {'form': form, "shop": shop, "categories": categories})
@login_required
def shop_delete(request, pk):
    shop = Shop.objects.get(pk=pk)
    shop.delete()
    return redirect('shop_list')