from django.db import models
from django.utils import timezone
# Create your models here.
class School(models.Model):
    REGIONS = (
        ('Central', 'Central'),
        ('Eastern', 'Eastern'),
        ('Western', 'Western'),
        ('Northern', 'Northern')
    )
   
    name =  models.CharField(max_length=255)
    short_name =  models.CharField(max_length=255, null=True, blank=True)
    registration_no =  models.CharField(max_length=50, null=True, blank=True)
    city =  models.CharField(max_length=255, null=True, blank=True)
    address =  models.CharField(max_length=255, null=True, blank=True)
    country =  models.CharField(max_length=255, null=True, blank=True, default='Uganda')
    region =  models.CharField(max_length=255, null=True, blank=True, choices=REGIONS)
    date_added = models.DateTimeField(default = timezone.now)
    added_by = models.BigIntegerField(null=True, blank=True)
    status =  models.CharField(max_length=25, default='pending')
    email         = models.EmailField(max_length = 50, null=True, blank=True)
    phone_number  = models.CharField(max_length=15, null=True, blank=True)
    logo_url      = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name 