from django.urls import path
from .views import UserManagementView, UserListView, UserDetailView, UserDeleteView, UserUpdateView #, UserCreateView
from .views import ShopManagementView, CategoryListView, CategoryCreateView, CategoryDeleteView, CategoryUpdateView, CategoryDetailView
from .views import ProductListView, ProductCreateView, ProductDeleteView, ProductDetailView, ProductUpdateView
from .views import VoucherListView, VoucherCreateView, VoucherDeleteView, VoucherDetailView, VoucherUpdateView
from .views import ProfileListView, ProfileCreateView, ProfileDeleteView, ProfileDetailView, ProfileUpdateView
from .views import SubscriberListView, SubscriberCreateView, SubscriberDeleteView, SubscriberDetailView, SubscriberUpdateView
from .views import NewsletterListView, NewsletterCreateView, NewsletterDeleteView, NewsletterDetailView, NewsletterUpdateView
from .views import PictureListView, PictureCreateView, PictureDeleteView, PictureDetailView, PictureUpdateView
from .views import PictureOfTheMonthListView, PictureOfTheMonthDeleteView
from .views import SliderListView, SliderCreateView, SliderDeleteView
from accounts.views import signupView



app_name='management'


urlpatterns = [
    path('', UserManagementView.as_view(), name = 'management'),
    path('user_management/', UserListView.as_view(), name = 'users'),
    path('user_detail/<int:pk>/', UserDetailView.as_view(), name = 'user_details'),
    path('user_add/', signupView, name = 'user_add'),
    path('user_delete/<int:pk>/', UserDeleteView.as_view(), name = 'user_delete'),
    path('user_update/<int:pk>/', UserUpdateView.as_view(), name = 'user_update'),

    path('profiles/', ProfileListView.as_view(), name = 'profiles'),
    path('profile_detail/<int:pk>/', ProfileDetailView.as_view(), name = 'profile_details'),
    path('profile_add/', ProfileCreateView.as_view(), name = 'profile_add'),
    path('profile_delete/<int:pk>/', ProfileDeleteView.as_view(), name = 'profile_delete'),
    path('profile_update/<int:pk>/', ProfileUpdateView.as_view(), name = 'profile_update'),

    path('subscribers/', SubscriberListView.as_view(), name = 'subscribers'),
    path('subscriber_detail/<int:pk>/', SubscriberDetailView.as_view(), name = 'subscriber_details'),
    path('subscriber_add/', SubscriberCreateView.as_view(), name = 'subscriber_add'),
    path('subscriber_delete/<int:pk>/', SubscriberDeleteView.as_view(), name = 'subscriber_delete'),
    path('subscriber_update/<int:pk>/', SubscriberUpdateView.as_view(), name = 'subscriber_update'),

    path('newsletters/', NewsletterListView.as_view(), name = 'newsletters'),
    path('newsletter_detail/<int:pk>/', NewsletterDetailView.as_view(), name = 'newsletter_details'),
    path('newsletter_add/', NewsletterCreateView.as_view(), name = 'newsletter_add'),
    path('newsletter_delete/<int:pk>/', NewsletterDeleteView.as_view(), name = 'newsletter_delete'),
    path('newsletter_update/<int:pk>/', NewsletterUpdateView.as_view(), name = 'newsletter_update'),

    path('shop_management/', ShopManagementView.as_view(), name = 'manage_shop'),
    path('shop_management/categories/', CategoryListView.as_view(), name = 'cats'),
    path('shop_management/categories/<slug:slug>/', CategoryDetailView.as_view(), name = 'cat_details'),
    path('shop_management/categories/category_add', CategoryCreateView.as_view(), name = 'cat_add'),
    path('shop_management/categories/category_delete/<slug:slug>/', CategoryDeleteView.as_view(), name = 'cat_delete'),
    path('shop_management/categories/category_update/<slug:slug>/', CategoryUpdateView.as_view(), name = 'cat_update'),

    path('shop_management/products/', ProductListView.as_view(), name = 'products'),
    path('shop_management/products/<slug:slug>/', ProductDetailView.as_view(), name = 'prod_details'),
    path('shop_management/products/product_add', ProductCreateView.as_view(), name = 'prod_add'),
    path('shop_management/products/product_delete/<slug:slug>/', ProductDeleteView.as_view(), name = 'prod_delete'),
    path('shop_management/products/product_update/<slug:slug>/', ProductUpdateView.as_view(), name = 'prod_update'),

    path('shop_management/sliders/', SliderListView.as_view(), name = 'sliders'),
    path('shop_management/products/slider_add', SliderCreateView.as_view(), name = 'slider_add'),
    path('shop_management/products/slider_delete/<int:pk>/', SliderDeleteView.as_view(), name = 'slider_delete'),

    path('shop_management/vouchers/', VoucherListView.as_view(), name = 'vouchers'),
    path('shop_management/vouchers/<int:pk>/', VoucherDetailView.as_view(), name = 'voucher_details'),
    path('shop_management/vouchers/product_add', VoucherCreateView.as_view(), name = 'voucher_add'),
    path('shop_management/vouchers/product_delete/<int:pk>/', VoucherDeleteView.as_view(), name = 'voucher_delete'),
    path('shop_management/vouchers/product_update/<int:pk>/', VoucherUpdateView.as_view(), name = 'voucher_update'),

    path('shop_management/pictures/', PictureListView.as_view(), name = 'pictures'),
    path('shop_management/pictures/<uuid:pk>/', PictureDetailView.as_view(), name = 'picture_details'),
    path('shop_management/pictures/picture_add', PictureCreateView.as_view(), name = 'picture_add'),
    path('shop_management/pictures/picture_delete/<uuid:pk>/', PictureDeleteView.as_view(), name = 'picture_delete'),
    path('shop_management/pictures/picture_update/<uuid:pk>/', PictureUpdateView.as_view(), name = 'picture_update'),

    path('shop_management/pictures_of_the_month/', PictureOfTheMonthListView.as_view(), name = 'pictures_of_the_month'),
    path('shop_management/pictures_of_the_month/picture_of_the_month_delete/<int:pk>/', PictureOfTheMonthDeleteView.as_view(), name = 'picture_of_the_month_delete'),

]