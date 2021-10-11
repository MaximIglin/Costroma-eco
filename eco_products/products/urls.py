from django.urls import path
from .views import get_shop_page, category_detail_page, product_detail

from .api_router import api_urls


urlpatterns = [
    path('shop', get_shop_page, name="shop"),
    path('category/<str:slug>', category_detail_page, name="category"),
    path('products/<str:slug>', product_detail, name="product_detail")

]

urlpatterns += api_urls
