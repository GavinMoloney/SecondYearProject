from django.urls import path
from . import views
from .views import GalleryUpdateView, GalleryCreateView, GalleryDeleteView, GalleryListView, GalleryDetailView



urlpatterns = [
    path('/<uuid:pk>/delete/', GalleryDeleteView.as_view(), name='gallery_delete'),
    path('/<uuid:pk>/edit/', GalleryUpdateView.as_view(), name='gallery_edit'),
    path('/new/', GalleryCreateView.as_view(), name='gallery_upload'),
    path('/<uuid:pk>', GalleryDetailView.as_view(), name = 'gallery_detail'),
    path('', GalleryListView.as_view(), name = 'gallery'),
]