from django.views.generic import TemplateView
from store.models import Category
from django.shortcuts import render



class HomePageView(TemplateView):
    template_name = 'home.html'

class ContactPageView(TemplateView):
    template_name = 'contact.html'

class GalleryPageView(TemplateView):
    template_name = 'gallery.html'


def shop_page(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
        }

    return render(request, 'shop.html', context)