import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

class Picture(models.Model):
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
    total_votes = models.IntegerField()
    votes_this_month = models.IntegerField()


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('gallery_detail', args=[str(self.id)])

    def add_total_vote(self):
        self.total_votes = self.total_votes + 1
        self.save()

    def sub_votes(self):
        self.total_votes = self.total_votes - 1
        self.save()


    class Meta:
        verbose_name = 'Gallery Picture'
        verbose_name_plural = 'Gallery Pictures'


class Votes(models.Model):
    voted_by = models.ForeignKey(get_user_model(), on_delete = models.CASCADE, related_name='voter')
    vote_date = models.DateField(auto_now_add = True)
    voted_picture = models.ForeignKey(Picture, on_delete = models.CASCADE, related_name='vote')

    class Meta:
        verbose_name = 'Votes'
        verbose_name_plural = 'Votes'

    def getVoter(self):
        return self.voted_by


class PictureOfTheMonth(models.Model):
    pic_of_the_month = models.ForeignKey(Picture, on_delete = models.CASCADE, related_name='pic_of_month')