from django.urls import path
from .api import CategoryApiView, CategoryDetailApi, ProductApiView, ProductDetailApi, ProductsByCategoryApi, CartDetailApi


api_urls = [
    path('api/category', CategoryApiView.as_view()),
    path('api/category/<str:slug>', CategoryDetailApi.as_view()),
    path('api/products', ProductApiView.as_view()),
    path('api/products/<str:slug>', ProductDetailApi.as_view()),
    path('api/category-products/<str:slug>', ProductsByCategoryApi.as_view()),
    path('api/cart_detail', CartDetailApi.as_view())
]
