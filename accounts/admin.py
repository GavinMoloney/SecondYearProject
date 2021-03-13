from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Profile

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'can_upload_images', 'is_staff',]
    fieldsets = UserAdmin.fieldsets + (
        ('Upload Permissions', {'fields': ('can_upload_images',)}),)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)

