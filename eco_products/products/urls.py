from django.urls import path
from .views import get_shop_page


urlpatterns = [
    path('shop', get_shop_page, name="shop"),
    
]