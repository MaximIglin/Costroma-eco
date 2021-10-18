from django.shortcuts import render
from products.models import Category

from products.models import Product
from products.services import get_all_products


def render_landing_page(request):
    categories = Category.objects.all()
    products = get_all_products()[:5]
    return render(request, 'home.html', {'categories':categories, "products": products})