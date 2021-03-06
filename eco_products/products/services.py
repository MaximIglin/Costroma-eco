import json

from rest_framework import status
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist


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
    category_queryset = Category.objects.all().values("id", "name", "slug", "image")
    return category_queryset


def get_category_by_slug(slug: str):
    """This function is return category by slug"""
    category = Category.objects.get(slug=slug)
    return category


def get_all_products():
    """This function is return all products"""
    product_queryset = Product.objects.all().values("id", "name", "price")
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
    if 'image' in data.keys():
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
    product.description = data['description']
    product.qty = data['qty']
    product.price = data['price']
    try:
        product.mass = data['mass']
        product.volume = data['volume']
        product.sale = data['sale']
        product.image = data['image']
        product.save()
    except KeyError:
        product.save()
    product.save()
    return product


def get_products_by_category(category_slug: str):
    """This function is return all products by category"""
    products = Product.objects.filter(category__slug=category_slug)
    return products


def parse_cart_cookie(request):
    """This function is return products and their quantity by cart"""
    cart = list(json.loads(request.COOKIES["cart"]).items())[:-1]
    products_id = []
    products_quantity = []
    for item in cart:
        products_id.append(item[0])
        products_quantity.append(item[1]["quantity"])

    cart_products_id = [int(products_id[i]) for i in range(
        len(products_id)) if int(products_quantity[i]) != 0]
    cart_products_qty = [int(qty)
                         for qty in products_quantity if int(qty) != 0]
    cart_products_queryset = Product.objects.filter(id__in=cart_products_id).values("id", "name", "price")
    return cart_products_queryset, cart_products_qty



