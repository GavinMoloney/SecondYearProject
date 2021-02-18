from django.urls import path
from .views import HomePageView, ContactPageView, AllProdCat

urlpatterns = [
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('', HomePageView.as_view(), name='home'),
    path('shop/', AllProdCat.as_view(), name = 'shop'),
]