"""astro_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts import views as user_views
from django.views.generic.base import TemplateView
from newsletter import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),    
    path('', include('pages.urls')),
    path('store/', include('store.urls')),
    path('cart/', include('cart.urls')),
    path('order/', include('order.urls')),
    path('voucher/', include('voucher.urls', namespace='voucher')),
    path('contact', include('contact_us.urls')),
    path('new/', views.new, name='new'),
    path('confirm/', views.confirm, name='confirm'),
    path('delete/', views.delete, name='delete'),
    #path('newsletter/', include('newsletter.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
