from django.test import TestCase
from .models import Category, Product
from .services import *
class TestServises(TestCase):

    def setUp(self) -> None:
        category_1 = Category.objects.create(name="milk", slug="milk")
        category_2 = Category.objects.create(name="honey", slug="honey")
        product_1 = Product(
            name="Молоко", slug="milk1",
            category=Category.objects.first(),
            description="some text 1",
            qty = 15,
            price = 2000
        )        
        product_2 = Product(
            name="Мёд", slug="honey1",
            category=Category.objects.get(slug="honey"),
            description="some text 2",
            qty = 25,
            price = 4000
        )

    def test_get_all_categories(self):
        all_categories = Category.objects.all()
        all_categories_from_func = get_all_categories()
        self.assertQuerysetEqual(all_categories, all_categories_from_func)    

