from django import forms
from .models import UserSkyPicture

class UserGalleryImageUpload(forms.Form):

    class Meta:
        model = UserSkyPicture
        fields = ['title', 'location', 'description', 'date_created', 'image']