from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Picture, PictureOfTheMonth
from .forms import UserGalleryImageUpload
from django.http import HttpResponseRedirect
 



def gallery_view(request):
    pictures = Picture.objects.all()
    context = {
        'Gallery_Pictures': pictures
    }

    return render(request, 'gallery.html', context)


def pic_of_the_month_gallery_view(request):
    pictures_of_the_month = PictureOfTheMonth.objects.all()
    context = {
        'Pictures_of_the_month': pictures_of_the_month
    }

    return render(request, 'gallery_of_the_month.html', context)


class GalleryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Picture
    fields = ('title', 'location', 'description', 'image')
    template_name = 'gallery_edit.html'


    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class GalleryDetailView(DetailView):
    model = Picture
    template_name = 'gallery_detail.html'


class GalleryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Picture
    template_name = 'gallery_delete.html'
    success_url = reverse_lazy('gallery')
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class GalleryCreateView(LoginRequiredMixin, CreateView):
    model = Picture
    fields = ('title', 'location', 'description', 'image')
    template_name = 'gallery_upload.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



def image_upload_view(request):
    if request.method == 'POST':
        form = UserGalleryImageUpload(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'gallery_detail.html', {'form': form, 'img_obj': img_obj})
    else:
        form = UserGalleryImageUpload()
    return render(request, 'gallery_detail.html', {'form': form})



def vote_add(request, pk):
    picture = get_object_or_404(Picture, id = pk)
    user = request.user        
    if request.method == "POST":
        v_e = Picture.objects.filter(id = pk, voted_by=user).exists()
        if v_e == False:
            picture.add_total_vote()  
            picture.voted_by.add(user)  
            picture.save()
    return redirect('gallery')



def vote_remove(request, pk):
    picture = get_object_or_404(Picture, id = pk)
    user = request.user        
    if request.method == "POST":
        picture.sub_votes()  
        picture.voted_by.remove(user)
        picture.save()
    return redirect('gallery')



def add_to_gallery_of_the_month(request):
    max_votes = 0
    
    # get pictures all and all pic of the month pictures 
    pictures = Picture.objects.all()
    pic_of_month_list = PictureOfTheMonth.objects.all()

    for i, pic in enumerate(pictures):              
        # if a picture is already in pic of the month galley               
        if PictureOfTheMonth.objects.filter(picture_of_month=pic).exists():    
            # remove it from query set
            pictures = Picture.objects.all().exclude(id = pic.id)
            # reset loop counter, because we just lost one element
            i = 0           
        elif pic.votes_this_month >= max_votes:
            max_votes = pic.votes_this_month
  
 
    # winner is selected from remaining pictures, based on votes last month
    # if two pictures had the same vote count, hard luck we choose first one we find
    most_voted = pictures.filter(votes_this_month=max_votes).first()

    # if max_votes == 0, it means that all pictures have been removed from querry set above, 
    # and there are no pictures left to be moved to gallery of the month
    if max_votes != 0:       
        PictureOfTheMonth.objects.create(picture_of_month = most_voted, votes= max_votes)

    # reset last month votes
    for pictrue in Picture.objects.all():
        pictrue.zero_month_votes()

    return redirect('gallery_of_the_month')