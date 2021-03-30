from django.contrib import admin
from .models import Picture, PictureOfTheMonth

class UserSkyPictureAdmin(admin.ModelAdmin):
    list_display = ['title', 'total_votes', 'votes_this_month', 'get_voter']
    list_per_page = 50


class PictureOfTheMonthAdmin(admin.ModelAdmin):
    list_display = ['picture_of_month', 'votes']



admin.site.register(Picture, UserSkyPictureAdmin)
admin.site.register(PictureOfTheMonth, PictureOfTheMonthAdmin)
