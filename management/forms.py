from django import forms 
from accounts.models import CustomUser
  
class UserForm(forms.ModelForm): 
  
    class Meta: 
        model = CustomUser
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'is_staff','can_upload_images','groups']
