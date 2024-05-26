from django.db import models


class Images(models.Model):
    name = models.CharField(max_length=100)
    content = models.BinaryField(editable=True)

    def save_image(self, image_file):
        image_file.seek(0)
        self.content = image_file.read()
        self.save()

    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ForeignKey(Images, on_delete=models.CASCADE)

class Service(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(default=0)
    image = models.ForeignKey(Images, on_delete=models.CASCADE)

    def get_category_name(self):
        return self.category.name

class Advertise(models.Model):
    image = models.ForeignKey(Images, on_delete=models.CASCADE)
    image_type = models.CharField(max_length=100, default= 'static')
    location = models.CharField(max_length=100, null=True, default='main')
