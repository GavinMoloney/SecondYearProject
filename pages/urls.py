from django.urls import path
from .views import HomePageView, ContactPageView, shop_page
urlpatterns = [
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('', HomePageView.as_view(), name='home'),
    path('shop/', shop_page, name = 'shop'),
]