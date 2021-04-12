from django.views.generic import TemplateView
from accounts.models import CustomUser
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from .forms import UserForm

class ManagementView(TemplateView):
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