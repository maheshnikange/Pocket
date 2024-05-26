from django.urls import path
from .views import *
from django.contrib.auth.views import PasswordResetConfirmView

urlpatterns = [
    path('', index , name='index'),
    path('login/', login , name='login_page'),
    path('register/', register , name='register_page'),
    path('category-services/<int:cat_id>/', get_admin_category_services, name='get_admin_category_services'),
    path('service-shops/<int:service_id>/', get_service_shop, name='get_service_shop'),
    path('service-enquiry/<int:service_id>/', service_enquiry , name='service_enquiry'),
]
