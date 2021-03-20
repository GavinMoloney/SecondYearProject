from django import forms
from .models import Picture

class UserGalleryImageUpload(forms.Form):

    class Meta:
        model = Picture
        fields = ['title', 'location', 'description', 'date_created', 'image']