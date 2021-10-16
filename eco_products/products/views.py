from django.shortcuts import render

from .services import get_all_categories, get_all_products, get_products_by_category, get_product_by_slug



def get_shop_page(request):
    context = {
        "categories": get_all_categories(),
        "products": get_all_products()
    }
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
