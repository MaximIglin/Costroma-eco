from django.contrib.sessions.backends.base import UpdateError
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .services import create_order


class CreateOrderApi(APIView):
    """This api for create order and client"""

    def post(self, request):
        try:
            create_order(request, self.request.data)
            return Response({"ok": "add"}, status=status.HTTP_200_OK)
        except KeyError:
            return Response({"Ошибка введённых данных": "Проверь еблан"}, status=status.HTTP_400_BAD_REQUEST)
