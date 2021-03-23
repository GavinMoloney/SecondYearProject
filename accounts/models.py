from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.contrib.auth import settings


class CustomUser(AbstractUser):
    can_upload_images = models.BooleanField(default= True)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Role = models.TextField(blank=True)
    number = models.IntegerField()
    image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')


    def __str__(self):
        return f'{self.user.username} Profile'
