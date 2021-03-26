from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.contrib.auth import settings


class CustomUser(AbstractUser):
    can_upload_images = models.BooleanField(default= True)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.TextField(default = 'Customer', blank=True)
    mobile = models.IntegerField(blank=True, null=True)
    image = models.ImageField(default = 'default.png', upload_to = 'profile_pics', blank=True)


    def __str__(self):
        return f'{self.user.username} Profile'
