from django.urls import path
from .views import get_shop_page, category_detail_page
from .api import CategoryApiView, CategoryDetailApi, ProductApiView, ProductDetailApi, ProductsByCategoryApi


urlpatterns = [
    path('shop', get_shop_page, name="shop"),
    path('category/<str:slug>', category_detail_page, name="category"),

    path('api/category', CategoryApiView.as_view()),
    path('api/category/<str:slug>', CategoryDetailApi.as_view()),
    path('api/products', ProductApiView.as_view()),
    path('api/products/<str:slug>', ProductDetailApi.as_view()),
    path('api/category-products/<str:slug>', ProductsByCategoryApi.as_view())

]