from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('produk/', views.produk_list, name='produk_list'),
    path('produk/<int:id>/', views.produk_detail, name='produk_detail'),
    path('kontak/', views.kontak, name='kontak'),
]
