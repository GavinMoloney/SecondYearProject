from django.urls import path
from .views import ManagementView, UserListView, UserDetailView, UserCreateView, UserDeleteView, UserUpdateView


app_name='management'


urlpatterns = [
    path('', ManagementView.as_view(), name = 'management'),
    path('users/', UserListView.as_view(), name = 'users'),
    path('user_detail/<int:pk>', UserDetailView.as_view(), name = 'user_details'),
    path('user_add/', UserCreateView.as_view(), name = 'user_add'),
    path('user_delete/<int:pk>', UserDeleteView.as_view(), name = 'user_delete'),
    path('user_update/<int:pk>', UserUpdateView.as_view(), name = 'user_update'),
]