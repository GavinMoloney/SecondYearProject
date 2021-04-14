from django.shortcuts import render
from store.models import Product, Category
from django.db.models import Q

def searchResult(request):
    products = None
    query = None
    if 'prod' in request.GET:
        query = request.GET.get('prod')
        products = Product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
    if 'cat' in request.GET:
        query = request.GET.get('cat')
        products = Product.objects.all().filter(Q(category__name__contains=query))
    return render(request, 'search.html', {'query':query, 'products':products}) 




