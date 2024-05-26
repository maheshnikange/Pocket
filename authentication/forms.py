from django import forms
from .models import CustomUser
from django.contrib.auth.forms import PasswordResetForm

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'first_name', 'last_name', 'company_name', 'role', 'password', 'phone_number']

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')
        user.set_password(password)  # Hash the password
        if commit:
            user.save()
        return user
class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label='Email', max_length=254)
