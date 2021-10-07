from django.urls import path
from .views import render_landing_page

urlpatterns = [
    path('', render_landing_page)
]