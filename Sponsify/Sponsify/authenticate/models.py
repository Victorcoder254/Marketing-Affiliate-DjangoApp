from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField()
    user_image = models.ImageField(upload_to='profile_pic/')
    tt_account = models.CharField(max_length=50)
    yt_account = models.CharField(max_length=50)
    ig_account = models.CharField(max_length=50)
    fb_account = models.CharField(max_length=50)
