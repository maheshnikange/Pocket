from django.db import models
from vendor_panel.models import VendorService

class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    service = models.ForeignKey(VendorService, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"Enquiry: {self.name} - {self.mobile_number}"
