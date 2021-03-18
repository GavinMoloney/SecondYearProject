import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

class UserSkyPicture(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=50, blank = True)
    description = models.TextField(max_length=100, blank = True)
    date_created = models.DateTimeField()
    image = models.ImageField(upload_to = 'gallery')
    author = models.ForeignKey(get_user_model(), on_delete = models.CASCADE,)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('gallery_detail', args=[str(self.id)])