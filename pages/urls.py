from django.urls import path
from .views import HomePageView, ContactPageView, shop_page, GalleryPageView, ManagementView
urlpatterns = [
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('', HomePageView.as_view(), name='home'),
    path('shop/', shop_page, name = 'shop'),
    path('', GalleryPageView.as_view(), name = 'gallery'),
    path('', ManagementView.as_view(), name = 'management'),
]