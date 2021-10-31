from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path

from orders import views

urlpatterns = {
    # ex: /infos/orders

    # path('orders', views.orders, name='orders'),

    re_path(r'^orders', views.ordersWithField, name='ordersWithField'),
    # ex: /infos/orders/1
    path('orders/<int:order_id>', views.certainOrder, name='getOrderByOrderId'),

}
