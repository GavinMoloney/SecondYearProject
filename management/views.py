from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect

from accounts.models import CustomUser, Profile
from store.models import Category, Product
from voucher.models import Voucher
from newsletter.models import Subscriber, Newsletter
from gallery.models import Picture, PictureOfTheMonth



class UserManagementView(TemplateView):
    template_name = 'mgmt.html'


class UserListView(ListView):
    model = CustomUser
    context_object_name = 'user_list'
    template_name = 'users.html'

class UserDetailView(DetailView):
    model = CustomUser
    template_name = 'user_details.html'


class UserUpdateView(UpdateView):
    model = CustomUser
    fields = ('username', 'password', 'first_name', 'last_name', 'email', 'is_staff','can_upload_images','groups',)
    template_name = 'user_edit.html'
    success_url = reverse_lazy('management:users')


class UserDeleteView(DeleteView):
    model = CustomUser
    template_name = 'user_delete.html'
    success_url = reverse_lazy('management:users')
    

class UserCreateView(CreateView):
    model = CustomUser
    fields = ('username', 'password', 'first_name', 'last_name', 'email', 'is_staff','can_upload_images','groups',)
    template_name = 'user_add.html'
    success_url = reverse_lazy('management:users')


class ProfileListView(ListView):
    model = Profile
    context_object_name = 'profile_list'
    template_name = 'profiles.html'

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile_details.html'


class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ('user', 'role', 'mobile', 'image',)
    template_name = 'profile_edit.html'
    success_url = reverse_lazy('management:profiles')


class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'profile_delete.html'
    success_url = reverse_lazy('management:profiles')
    

class ProfileCreateView(CreateView):
    model = Profile
    fields = ('user', 'role', 'mobile', 'image',)
    template_name = 'profile_add.html'
    success_url = reverse_lazy('management:profiles')


class ShopManagementView(TemplateView):
    template_name = 'shop_management.html'



class CategoryListView(ListView):
    model = Category
    context_object_name = 'category_list'
    template_name = 'categories.html'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_details.html'


class CategoryUpdateView(UpdateView):
    model = Category
    fields = ('slug', 'name', 'description', 'image', 'image_secondary',)
    template_name = 'category_edit.html'
    success_url = reverse_lazy('management:cats')


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_delete.html'
    success_url = reverse_lazy('management:cats')
    

class CategoryCreateView(CreateView):
    model = Category
    fields = ('slug', 'name', 'description', 'image', 'image_secondary',)
    template_name = 'category_add.html'
    success_url = reverse_lazy('management:cats')


class ProductListView(ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'products.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_details.html'


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('slug', 'name', 'make', 'model', 'description', 'category', 'price', 'stock', 'available', 'image',)
    template_name = 'product_edit.html'
    success_url = reverse_lazy('management:products')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('management:products')
    

class ProductCreateView(CreateView):
    model = Product
    fields = ('slug', 'name', 'make', 'model', 'description', 'category', 'price', 'stock', 'available', 'image',)
    template_name = 'product_add.html'
    success_url = reverse_lazy('management:products')



class VoucherListView(ListView):
    model = Voucher
    context_object_name = 'voucher_list'
    template_name = 'vouchers.html'

class VoucherDetailView(DetailView):
    model = Voucher
    template_name = 'voucher_details.html'


class VoucherUpdateView(UpdateView):
    model = Voucher
    fields = ('code', 'valid_from', 'valid_to', 'discount', 'active',)
    template_name = 'voucher_edit.html'
    success_url = reverse_lazy('management:vouchers')


class VoucherDeleteView(DeleteView):
    model = Voucher
    template_name = 'voucher_delete.html'
    success_url = reverse_lazy('management:vouchers')
    

class VoucherCreateView(CreateView):
    model = Voucher
    fields = ('code', 'valid_from', 'valid_to', 'discount', 'active',)
    template_name = 'voucher_add.html'
    success_url = reverse_lazy('management:vouchers')



class SubscriberListView(ListView):
    model = Subscriber
    context_object_name = 'subscriber_list'
    template_name = 'subscribers.html'

class SubscriberDetailView(DetailView):
    model = Subscriber
    template_name = 'subscriber_details.html'


class SubscriberUpdateView(UpdateView):
    model = Subscriber
    fields = ('email', 'confirmed',)
    template_name = 'subscriber_edit.html'
    success_url = reverse_lazy('management:subscribers')


class SubscriberDeleteView(DeleteView):
    model = Subscriber
    template_name = 'subscriber_delete.html'
    success_url = reverse_lazy('management:subscribers')
    

class SubscriberCreateView(CreateView):
    model = Subscriber
    fields = ('email', 'confirmed',)
    template_name = 'subscriber_add.html'
    success_url = reverse_lazy('management:subscribers')


class NewsletterListView(ListView):
    model = Newsletter
    context_object_name = 'newsletter_list'
    template_name = 'newsletters.html'

class NewsletterDetailView(DetailView):
    model = Newsletter
    template_name = 'newsletter_details.html'


class NewsletterUpdateView(UpdateView):
    model = Newsletter
    fields = ('subject', 'contents',)
    template_name = 'newsletter_edit.html'
    success_url = reverse_lazy('management:newsletters')


class NewsletterDeleteView(DeleteView):
    model = Newsletter
    template_name = 'newsletter_delete.html'
    success_url = reverse_lazy('management:newsletters')
    

class NewsletterCreateView(CreateView):
    model = Newsletter
    fields = ('subject', 'contents',)
    template_name = 'newsletter_add.html'
    success_url = reverse_lazy('management:newsletters')


class PictureListView(ListView):
    model = Picture
    context_object_name = 'picture_list'
    template_name = 'newsletters.html'

class PictureDetailView(DetailView):
    model = Picture
    template_name = 'newsletter_details.html'


class PictureUpdateView(UpdateView):
    model = Picture
    fields = ('subject', 'contents',)
    template_name = 'newsletter_edit.html'
    success_url = reverse_lazy('management:newsletters')


class PictureDeleteView(DeleteView):
    model = Picture
    template_name = 'newsletter_delete.html'
    success_url = reverse_lazy('management:newsletters')
    

class PictureCreateView(CreateView):
    model = Picture
    fields = ('subject', 'contents',)
    template_name = 'newsletter_add.html'
    success_url = reverse_lazy('management:newsletters')


