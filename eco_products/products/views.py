from django.shortcuts import render


def get_shop_page(request):
    return render(request, "shop.html", {})
