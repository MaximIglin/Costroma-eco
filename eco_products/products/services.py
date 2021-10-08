from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status

from .models import Category, Product



def does_not_exist_decorator(function):
    """This decorator is needed in order to handle exceptions for non-existent instances"""
    def wrapped(self, request, slug):
        try:
            return function(self, request, slug)
        except ObjectDoesNotExist:
            return Response({"Error": "Object does not exist or was deleted"}, status=status.HTTP_404_NOT_FOUND)
    return wrapped

def get_all_categories():
    """This function is return all categories"""
    category_queryset = Category.objects.all()
    return category_queryset


def get_category_by_slug(slug: str):
    """This function is return category by slug"""
    category = Category.objects.get(slug=slug)
    return category

def get_all_products():
    """This function is return all products"""
    product_queryset = Product.objects.all()
    return product_queryset

def get_product_by_slug(slug: str):
    """This function is return prodcut by slug"""
    product = Product.objects.get(slug=slug)
    return product


def add_new_category(data: dict):
    """This function for add new category """
    category = Category()
    category.name = data['name']
    category.slug = data['slug']
    category.image = data['image']
    category.save()
    return category

def add_new_product(data: dict):
    """This function for create new product instance"""
    product = Product()
    product.name = data['name']
    category = Category.objects.get(name=data['category'])
    product.category = category
    product.slug = data['slug']
    product.description = data['descriprion']
    product.qty = data['qty']
    if 'mass' in data.keys():
        product.mass = data['mass']
    elif 'volume' in data.keys():
        product.volume = data['volume']
    product.price = data['price']
    product.sale = data['sale']
    product.image = data['image']
    product.save()
    return product  


def get_products_by_category(category_slug: str):
    """This function is return all products by category"""
    products = Product.objects.filter(category__slug=category_slug)
    print(products)
    return products
