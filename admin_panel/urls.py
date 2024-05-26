from django.contrib import admin
from django.urls import path ,include
from .views import *
from .admin_services import category, services, advertisements, enquiries

urlpatterns = [
    path('login/',login, name ="login"),
    path('logout/',logout, name ="logout"),
    path('dashboard/',dashboard, name ="dashboard"),
    path('categories/', category.category_list, name='category_list'),
    path('categories/<int:pk>/', category.category_detail, name='category_detail'),
    path('categories/create/', category.category_create, name='category_create'),
    path('categories/<int:pk>/update/', category.category_update, name='category_update'),
    path('categories/<int:pk>/delete/', category.category_delete, name='category_delete'),
    path('services/',services.service_list, name='service_list'),
    path('services/<int:pk>/',services.service_detail, name='service_detail'),
    path('services/create/',services.service_create, name='service_create'),
    path('services/<int:pk>/update/',services.service_update, name='service_update'),
    path('services/<int:pk>/delete/',services.service_delete, name='service_delete'),
    path('advertises/', advertisements.advertise_list, name='advertise_list'),
    path('advertises/<int:pk>/', advertisements.advertise_detail, name='advertise_detail'),
    path('advertises/create/', advertisements.advertise_create, name='advertise_create'),
    path('advertises/<int:pk>/update/', advertisements.advertise_update, name='advertise_update'),
    path('advertises/<int:pk>/delete/', advertisements.advertise_delete, name='advertise_delete'),
    path('enquiries/', enquiries.get_enquiries_for_admin, name='get_enquiries_for_admin'),
    ]
