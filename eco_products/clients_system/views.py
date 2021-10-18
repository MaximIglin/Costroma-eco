from django.contrib.sessions.backends.base import UpdateError
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Client, Order
from .services import validate_and_add_client, create_order


class CreateOrderApi(APIView):
    """This api for create order and client"""

    def post(self, request):
        try:
            create_order(request, self.request.data)
            return Response({"ok":"add"})
        except KeyError:
            return Response({"Ошибка введённых данных":"Проверь еблан"})    


