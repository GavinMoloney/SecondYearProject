from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    can_upload_images = models.BooleanField(default= True)

