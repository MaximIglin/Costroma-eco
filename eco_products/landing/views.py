from django.shortcuts import render
from products.models import Category

from products.models import Product


def render_landing_page(request):
    categories = Category.objects.all()
    products = Product.objects.all()[:5]
    return render(request, 'home.html', {'categories':categories, "products": products})