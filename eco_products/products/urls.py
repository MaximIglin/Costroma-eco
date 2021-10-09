from django.urls import path
from .views import get_shop_page, category_detail_page

from .api_router import api_urls


urlpatterns = [
    path('shop', get_shop_page, name="shop"),
    path('category/<str:slug>', category_detail_page, name="category")
]

urlpatterns += api_urls