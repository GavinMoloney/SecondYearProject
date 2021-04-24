from django.views.generic import TemplateView
from store.models import Category, Slider
from django.shortcuts import render



class HomePageView(TemplateView):
    template_name = 'home.html'

class ContactPageView(TemplateView):
    template_name = 'contact.html'

class GalleryPageView(TemplateView):
    template_name = 'gallery.html'

class ManagementView(TemplateView):
    template_name = "mgmt.html"


def shop_page(request):
    categories = Category.objects.all()
    slides = Slider.objects.all()
    context = {
        'categories': categories,
        'slides': slides
        }

    return render(request, 'shop.html', context)