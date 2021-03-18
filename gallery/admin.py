from django.contrib import admin
from .models import UserSkyPicture


class UserSkyPictureAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_created']
    list_per_page = 50

admin.site.register(UserSkyPicture, UserSkyPictureAdmin)