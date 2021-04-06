from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from django.core.paginator import Paginator, EmptyPage, InvalidPage



def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()

    paginator = Paginator(products, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage,InvalidPage):
        products = paginator.page(paginator.num_pages)

    context = {
        'category': category,
        'products': products
    }

    return render(request, 'category_detail.html', context)


def product_detail(request, category_slug, slug):
    product = get_object_or_404(Product, slug=slug)

    context = {
        'product': product
    }

    return render(request, 'product.html', context)
