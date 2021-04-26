from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 

from .models import CustomUser, Profile


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email',)



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields

class PictureUploadForm(forms.ModelForm): 
  
    class Meta: 
        model = Profile
        fields = ('mobile','image')
