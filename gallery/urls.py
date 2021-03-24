from django.urls import path
from . import views
from .views import GalleryUpdateView, GalleryCreateView, GalleryDeleteView, GalleryDetailView



urlpatterns = [
    path('delete/<uuid:pk>/', GalleryDeleteView.as_view(), name='gallery_delete'),
    path('edit/<uuid:pk>/', GalleryUpdateView.as_view(), name='gallery_edit'),
    path('upload_image/', GalleryCreateView.as_view(), name='gallery_upload'),
    path('<uuid:pk>/', GalleryDetailView.as_view(), name = 'gallery_detail'),
    path('', views.gallery_view, name = 'gallery'),
    path('downvote/<uuid:pk>', views.vote_remove, name='down_vote'),
    path('upvote/<uuid:pk>', views.vote_add, name='up_vote'),
    
]