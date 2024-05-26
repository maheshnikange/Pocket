from django.contrib import admin
from .models import Category, Service, Advertise


@admin.register(Category)
class adminCategory(admin.ModelAdmin):
    list_display = ('id','name', 'description')

@admin.register(Service)
class adminService(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'get_category_name')

@admin.register(Advertise)
class adminAdvertise(admin.ModelAdmin):
    list_display = ('id', 'image', 'image_type')
