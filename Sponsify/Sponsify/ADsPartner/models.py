from django.db import models
from django.contrib.auth.models import User


class BusinessProfile(models.Model):
    business = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True)
    photo = models.ImageField(upload_to='businessProfile/')
    industry = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=50, blank=True)
    contact_email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    website = models.URLField(blank=True)
    social_media_link = models.URLField(blank=True)


class Listup(models.Model):
    adlisting = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ImageField(upload_to='products/')
    description = models.TextField()
    specifications = models.TextField()
    price_offers = models.TextField()
    contact_info = models.IntegerField() 

        
