from django.shortcuts import render , redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import auth
from django.contrib import messages
from .forms import UserForm
from admin_panel.models import Advertise
from django.conf import settings

from django.contrib.auth.tokens import default_token_generator
from .models import CustomUser, OTP
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.views import View
import random

# Create your views here.



def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password =password  )
        if user is not None:
            auth.login(request , user)
            if user.role == 'vendor':
                return redirect('vendor_dashboard')  
            return redirect('/')
        else:
            messages.info(request, 'invalid username or password')
            return redirect("/")
    else:
        advertise_images = Advertise.objects.filter(location='dashboard')
        return render(request,'index.html', {"advertise_images": advertise_images})

def logout(request):
    auth.logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('user_login')


def register(request):
    form = UserForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('login_page')
    return redirect('register_page')

class PasswordResetRequestView(View):
    def get(self, request):
        return render(request, 'registration/password_reset_form.html')

    def post(self, request):
        try:
            email = request.POST["email"]
            try:
                user = CustomUser.objects.get(email=email)
            except:
                raise Exception("User not found")
            #Generate OTP for the password reset
            otp = str(random.randint(100000, 999999))
            existing_otps = OTP.objects.filter(user=user)
            if existing_otps:
                existing_otps.delete()
            otp = OTP.objects.create(user=user, otp=otp)
            otp.save()
            # Send an email with OTP to verify the user
            send_otp_email(email, otp.otp)
            return HttpResponseRedirect(f'/user/password_reset_otp?email={email}')
        except Exception as e:
            return render(request, 'registration/password_reset_error.html',{"error_message": e})
        

class VerifyOTP(View):

    def get(self, request):
        email = request.GET["email"]
        return render(request, 'registration/verify_otp.html', {"email": email})
    def post(self, request):
        try:
            otp = request.POST['OTP']
            email = request.POST["email"]
            user = CustomUser.objects.filter(email=email).first()
            if user is None:
                raise Exception(f"User with email {email} does not exist")
            otp_object = OTP.objects.filter(user=user, otp=otp).first()
            if otp_object and otp_object.otp == otp:
                otp_object.delete()
                return HttpResponseRedirect(f'/user/password_reset_confirm?email={email}')
            else:
                return render(request, 'registration/password_reset_error.html',{"error_message": "Invalid OTP"})
            
        except Exception as e:
            return render(request, 'registration/password_reset_error.html',{"error_message": e})

class ResetPassword(View):
    def get(self, request):
        email = request.GET["email"]
        return render(request, 'registration/password_reset_confirm.html', {"email": email})
    def post(self, request):
        try:
            email = request.POST['email']
            if email is None:
                raise Exception("Email is required")
            user = CustomUser.objects.filter(email=email).first()
            if user is None:
                raise Exception(f"User with email {email} does not exist")
            new_password = request.POST['password']

            user.set_password(new_password)
            user.save()
            return redirect('user_login')
        except Exception as e:
            return render(request, 'registration/password_reset_error.html',{"error_message": e})
def send_otp_email(email, otp):
    subject = 'Password Reset OTP'
    message = f'Your OTP for password reset is: {otp}'
    send_mail(subject, message, settings.EMAIL_HOST_USER, [email])