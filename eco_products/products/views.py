from django.shortcuts import render

from .services import get_all_categories, get_all_products, get_products_by_category, get_product_by_slug
from .models import Product
import json

def get_shop_page(request):
    context = {
        "categories": get_all_categories(),
        "products": get_all_products()
    }
    try:
        cart = list(json.loads(request.COOKIES["cart"]).items())[:-1]
        products_id = []
        products_quantity = []
        for item in cart:
            products_id.append(item[0])
            products_quantity.append(item[1]["quantity"])

        cart_products_id = [int(products_id[i]) for i in range(0, len(products_id)) if int(products_quantity[i]) != 0 ]
        cart_products_qty = [int(qty) for qty in products_quantity if int(qty) !=0 ]


        cart_products_queryset = Product.objects.filter(id__in=cart_products_id)
        print(cart_products_queryset)
        print(cart)
        print(len(products_id))
        print(len(products_quantity))
        print(len(cart_products_id))
        print(len(cart_products_qty))
        print(f"id продуктов  -- -- -- {cart_products_id}")
        print(f"Количество продуктов {cart_products_qty}")
        return render(request, "shop.html", context)
    except KeyError:    
        return render(request, "shop.html", context)


def category_detail_page(request, slug):
    context = {
        "categories": get_all_categories(),
        "category_products": get_products_by_category(slug)
    }
    return render(request, "shop.html", context)


def product_detail(request, slug):
    product = get_product_by_slug(slug)
    context = {
        "categories": get_all_categories(),
        "product": product
    }
    return render(request, 'product_detail.html', context)
