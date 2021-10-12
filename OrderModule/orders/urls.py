from django.contrib import admin
from django.urls import path

from orders import views

urlpatterns = {
    # ex: /infos/orders
    path('orders', views.orders, name='orders'),


    # ex: /infos/orders/1
    path('orders/<int:order_id>', views.certainOrder, name='getOrderByOrderId'),

}