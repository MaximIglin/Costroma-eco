from django.shortcuts import render


def get_cart_page(request):
    return render(request, "cart.html", {})
