from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
# from django.core.paginator import Paginator, EmptyPage, InvalidPage



# def allProdCat(request, category_id=None):
#     c_page = None
#     products_list = None

#     if category_id != None:
#         c_page = get_object_or_404(Category, id = category_id)
#         products_list = Product.objects.filter(category = c_page, available = True)
#     # else:
#     #     products_list = Product.objects.all().filter(available = True)
#     return render(request, 'shop.html', {'category':c_page, 'products':products_list})


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()
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
