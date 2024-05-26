from django.urls import path
from . import views


urlpatterns = [
    path('', views.login , name='user_login'),
    path('register', views.register, name='register' ),
    path('logout', views.logout, name='user_logout' ),
    path('password_reset/', views.PasswordResetRequestView.as_view(), name='password_reset'),
    path('password_reset_otp', views.VerifyOTP.as_view(), name='password_reset_otp'),
    path('password_reset_confirm/', views.ResetPassword.as_view(), name='password_reset_confirm')
]
