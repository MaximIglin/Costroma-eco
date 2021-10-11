from django.urls import path
from .views import get_cart_page


urlpatterns = [
    path('cart', get_cart_page, name="cart")
    
]