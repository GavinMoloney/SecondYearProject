from django.urls import path
from .views import UserManagementView, UserListView, UserDetailView, UserCreateView, UserDeleteView, UserUpdateView
from .views import ShopManagementView, CategoryListView, CategoryCreateView, CategoryDeleteView, CategoryUpdateView, CategoryDetailView




app_name='management'


urlpatterns = [
    path('', UserManagementView.as_view(), name = 'management'),
    path('user_management/', UserListView.as_view(), name = 'users'),
    path('user_detail/<int:pk>', UserDetailView.as_view(), name = 'user_details'),
    path('user_add/', UserCreateView.as_view(), name = 'user_add'),
    path('user_delete/<int:pk>', UserDeleteView.as_view(), name = 'user_delete'),
    path('user_update/<int:pk>', UserUpdateView.as_view(), name = 'user_update'),

    path('shop_management/', ShopManagementView.as_view(), name = 'manage_shop'),
    path('shop_management/categories/', CategoryListView.as_view(), name = 'cats'),
    path('shop_management/categories/<slug:slug>/', CategoryDetailView.as_view(), name = 'cat_details'),
    path('shop_management/categories/category_add', CategoryCreateView.as_view(), name = 'cat_add'),
    path('shop_management/categories/category_delete/<slug:slug>/', CategoryDeleteView.as_view(), name = 'cat_delete'),
    path('shop_management/categories/category_update/<slug:slug>/', CategoryUpdateView.as_view(), name = 'cat_update'),
]