from django.shortcuts import render
from store.models import Product, Category
from django.db.models import Q

def searchResult(request):
    products = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query) | Q(category__name__contains=query))
    return render(request, 'search.html', {'query':query, 'products':products}) 


