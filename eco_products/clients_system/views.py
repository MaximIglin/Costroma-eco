from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from products.services import get_product_by_slug


def get_cart_page(request):

    return render(request, "cart.html", {})
