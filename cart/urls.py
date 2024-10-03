from . import views
from django.urls import path

urlpatterns = [
    path('', views.cart_summary, name='cart_summary'),
    path('cart_add/<int:product_id>', views.cart_add, name='cart_add'),
    path('', views.cart_delete, name='cart_delete'),
    path('', views.cart_update, name='cart_update'),
]
