from django.urls import path
from .views import signupView, signinView, signoutView, update_profile

urlpatterns = [
    path('create/', signupView, name = 'signup'),
    path('login/', signinView, name = 'signin'),
    path('logout/', signoutView, name = 'signout'),
    path('update_profile/', update_profile, name='update_profile')
]