from django.urls import path
from .views import CreateOrderApi



urlpatterns = [
    path("api/create-order", CreateOrderApi.as_view())
]
