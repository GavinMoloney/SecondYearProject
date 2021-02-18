from django.urls import path
from .views import HomePageView, ContactPageView

urlpatterns = [
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('', HomePageView.as_view(), name='home'),
]