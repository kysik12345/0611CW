from django.urls import path
from .views import (cart_detail, remove_cart,
                    update_cart_by_front,remove_product_ajax,
                    remove_product,get_cart_length)

urlpatterns = [
    path('detail/', cart_detail, name="cart_detail"),
    path('clear/', remove_cart, name="remove_cart"),
    path('update_cart_session/', update_cart_by_front, name="update_cart_session"),
    path('remove_fetch/', remove_product_ajax, name="remove_product_ajax"),
    path('remove/<int:product_id>/', remove_product, name="remove_product"),
    path('length/', get_cart_length, name="cart_length"),
    
] 
