from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, PictureUploadForm
from .models import CustomUser, Profile
from django.contrib.auth.models import Group
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


def signupView(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            signup_user = CustomUser.objects.get(username = username)
            user= CustomUser.objects.get(username= signup_user)
            customer_group = Group.objects.get(name = 'Customer')
            customer_group.user_set.add(signup_user)
            profile = Profile.objects.create(user=user)
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form':form})


def signinView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username = username, password = password)
            messages.success(request, 'Welcome back '+ username  +'😊')
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('signup')
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'form':form})

def signoutView(request):
    logout(request)
    return redirect('home')

    
def profile(request):
    return render(request, 'profile.html')

def update_profile(request):    
    user = request.user.profile
    form = PictureUploadForm(instance = user)
    if request.method == 'POST':
        form = PictureUploadForm(request.POST, request.FILES, instance = user)
        if form.is_valid():
            messages.success(request, 'Your profile is updated successfully!')
            form.save()
            img_obj = form.instance
            return render(request, 'profile.html', {'form': form, 'img_obj': img_obj})
    else:
        form = PictureUploadForm()
    return render(request, 'update_profile.html', {'form': form})
