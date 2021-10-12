from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .cart import Cart
from products.services import get_product_by_slug


def get_cart_page(request):
    return render(request, "cart.html", {})


class AddToCartApi(APIView):

    def post(self, request, slug):
        cart = Cart(request)
        product = get_product_by_slug(slug)
        cart.add(
            product=product,
            quantity=self.request.data['quantity'],
            update_quantity=self.request.data['update']
        )
        return Response({"ok": "Added"}, status=status.HTTP_200_OK)


class RemoveCartApi(APIView):
    def delete(self, request, slug):
        cart = Cart(request)
        product = get_product_by_slug(slug)
        cart.remove(product)
        return Response({"ok": "deleted"}, status=status.HTTP_200_OK)


class CartDetailAPi(APIView):
    def get(self, request):
        cart = Cart(request)
        return Response({'cart': cart}, status=status.HTTP_200_OK)
