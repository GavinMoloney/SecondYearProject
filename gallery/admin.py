from django.contrib import admin
from .models import Picture, Votes


class UserSkyPictureAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_created', 'total_votes', 'votes_this_month']
    list_per_page = 50


class UserVote(admin.ModelAdmin):
    list_display = ['vote_date', 'voted_picture']
    list_per_page = 50


admin.site.register(Picture, UserSkyPictureAdmin)
admin.site.register(Votes, UserVote)