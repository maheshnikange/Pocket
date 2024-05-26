from django import forms
from .models import Category, Service, Advertise, Images

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['category', 'name', 'description', 'price']

class AdvertiseForm(forms.ModelForm):
    class Meta:
        model = Advertise
        fields = ['image_type', 'location']
class ImagesForm(forms.ModelForm):
    content = forms.ImageField(required=False)

    class Meta:
        model = Images
        fields = ['name', 'content']

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.cleaned_data['content']:
            instance.save_image(self.cleaned_data['content'])
        if commit:
            instance.save()
        return instance