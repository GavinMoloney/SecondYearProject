import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from accounts.models import CustomUser


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
    total_votes = models.IntegerField(default = 0, blank = True, null = True)
    votes_this_month = models.IntegerField(default = 0, blank = True, null = True)
    voted_by = models.ManyToManyField(CustomUser, related_name='voter', blank = True)

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

    def add_month_votes(self):
        self.votes_this_month += 1
        self.save()

    def zero_month_votes(self):
        self.votes_this_month = 0
        self.save()

    def get_voter(self):
        return ",".join([str(v) for v in self.voted_by.all()])
        

    class Meta:
        verbose_name = 'Gallery Picture'
        verbose_name_plural = 'Gallery Pictures'



class PictureOfTheMonth(models.Model):
    picture_of_month = models.OneToOneField(Picture, on_delete= models.SET_NULL, null = True, related_name='picoftm')
    votes = models.IntegerField(default = 0, blank = True, null = True)

    
    class Meta:
        verbose_name = 'Picture of the month gallery'
        verbose_name_plural = 'Pictures of the month gallery'
