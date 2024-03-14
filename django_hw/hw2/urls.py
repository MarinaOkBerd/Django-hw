from django.urls import path
from . import views

urlpatterns = [
    path('', views.hw2, name='hw2'),
    path('customers/', views.customers, name='customers'),
    path('products/', views.products, name='products'),
    path('orders/', views.orders, name='orders'),
]