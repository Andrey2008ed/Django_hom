from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('info/<int:order_id>/', views.info, name='info'),
    path('customer/<int:customer_id>', views.show_customers_orders, name='show_customers_orders'),
    path('last_orders/<int:customer_id>', views.show_recent_orders, name='show_recent_orders'),
    path('edit_product/<int:product_id>', views.edit_product, name='edit_product'),
    path('add_product/', views.add_product, name='add_product'),


]