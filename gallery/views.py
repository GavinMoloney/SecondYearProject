from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Picture, Votes
from .forms import UserGalleryImageUpload
from django.http import HttpResponseRedirect
 



def gallery_view(request):
    pictures = Picture.objects.all()
    context = {
        'Gallery_Pictures': pictures
    }

    return render(request, 'gallery.html', context)


# class GalleryListView(ListView):
#     print("in gal view")
#     model = UserSkyPicture
#     context_object_name = 'gallery_items'
#     template_name = 'gallery.html'


class GalleryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Picture
    fields = ('title', 'location', 'description', 'date_created', 'image')
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
    fields = ('title', 'location', 'description', 'date_created', 'image')
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
        vote = Votes.objects.create(voted_by= request.user, voted_picture = picture) 
        if vote.voted_by != user:
            picture.add_total_vote()      

    return redirect('gallery')