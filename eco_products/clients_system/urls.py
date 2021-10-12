from django.urls import path
from .views import get_cart_page, AddToCartApi, CartDetailAPi, RemoveCartApi


urlpatterns = [
    path('cart', get_cart_page, name="cart"),
    path('add_to_cart/<str:slug>', AddToCartApi.as_view(), name="add_to_cart"),
    path('cart_remove/<str:slug>', RemoveCartApi.as_view(), name="remove_from_cart"),
    path('cart_detail_api', CartDetailAPi.as_view(), name="cart_detail")

    
]