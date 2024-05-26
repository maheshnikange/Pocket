from django.db import models
from admin_panel.models import Category, Service
from authentication.models import CustomUser
# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    pincode = models.IntegerField(default=0)
    image = models.ImageField(default='test.png' , upload_to='uploads/shop_images/')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    def categories(self):
        return Category.objects.filter(shopcategory__shop=self)

    def categories_name(self):
        categories =  Category.objects.filter(shopcategory__shop=self)
        category_names = [category.name for category in categories]
        return category_names

class ShopCategory(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('shop', 'category')

class VendorService(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, default= 1)

    def __str__(self):
        return self.service.name