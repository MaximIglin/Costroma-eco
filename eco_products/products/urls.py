from django.urls import path
from .views import get_shop_page
from .api import CategoryApiView, CategoryDetailApi, ProductApiView, ProductDetailApi


urlpatterns = [
    path('shop', get_shop_page, name="shop"),

    path('api/category', CategoryApiView.as_view()),
    path('api/category/<str:slug>', CategoryDetailApi.as_view()),
    path('api/products', ProductApiView.as_view()),
    path('api/products/<str:slug>', ProductDetailApi.as_view())

]