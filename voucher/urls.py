from django.urls import path
from . import views

app_name = 'voucher'

urlpatterns = [
    path('apply/', views.voucher_apply, name='apply'),
]