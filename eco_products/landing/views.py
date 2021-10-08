from django.shortcuts import render
from products.models import Category


def render_landing_page(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories':categories})