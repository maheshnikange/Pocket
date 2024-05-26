from django.urls import path
from . import views
from .vendor_service import vendor_shop, vendor_service, service_enqueries
urlpatterns = [
    path('dashboard/', views.dashboard, name ="vendor_dashboard"),
    path('shops/', vendor_shop.shop_list, name='shop_list'),
    path('shops/detail/<int:pk>/', vendor_shop.shop_detail, name='shop_detail'),
    path('shops/create/', vendor_shop.shop_create, name='shop_create'),
    path('shops/update/<int:pk>/', vendor_shop.shop_update, name='shop_update'),
    path('shops/delete/<int:pk>/', vendor_shop.shop_delete, name='shop_delete'),
    path('vendor_services/', vendor_service.vendor_service_list, name='vendor_service_list'),
    path('vendor_services/create/', vendor_service.vendor_service_create, name='vendor_service_create'),
    path('vendor_services/<int:pk>/update/', vendor_service.vendor_service_update, name='vendor_service_update'),
    path('vendor_services/<int:pk>/delete/', vendor_service.vendor_service_delete, name='vendor_service_delete'),
    path('get-shop-categories/<int:shop_id>/', views.get_shop_categories, name='get_shop_categories'),
    path('get-category-services/<int:category_id>/', views.get_category_services, name='get_category_services'),
    path('get-service-price/<int:service_id>/', views.get_service_price, name='get_service_price'),
    path('get-service-enqueries/', service_enqueries.get_enquiries_for_user, name='get_enquiries_for_user'),
    path('search-vendor-enqueries/', service_enqueries.search_vendor_enqueries, name='search_vendor_enqueries'),
]
