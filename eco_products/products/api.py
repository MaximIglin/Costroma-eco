from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import CategorySerializer, ProductSerializer
from .services import (add_new_product, get_all_categories, get_all_products,
                       get_category_by_slug, get_product_by_slug,
                       does_not_exist_decorator, add_new_category, get_products_by_category
)


class CategoryApiView(APIView):
    """This api for all category-instance"""
    def get(self, request):
        categories = get_all_categories()
        serializer = CategorySerializer(categories, many=True, read_only=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        category = add_new_category(self.request.data)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_201_CREATED)    


class CategoryDetailApi(APIView):
    """This api for detail information about category"""

    @does_not_exist_decorator
    def get(self, request, slug):
        category = get_category_by_slug(slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductApiView(APIView):
    """This api for get all products or add new"""

    def get(self, request):
        products = get_all_products()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        product = add_new_product(self.request.data)
        serializer = ProductSerializer(product)    
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductDetailApi(APIView):
    """This api for detail information about category"""

    @does_not_exist_decorator
    def get(self, request, slug):
        product = get_product_by_slug(slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductsByCategoryApi(APIView):

    def get(self, request, slug):
        products = get_products_by_category(slug)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)