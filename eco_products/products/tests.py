from django.test import TestCase
from .models import Category, Product
from .services import *
class TestServises(TestCase):

    def setUp(self) -> None:
        category_1 = Category()
        category_1.name = "milk"
        category_1.slug = "milk"
        category_1.save()

        category_2 = Category()
        category_2.name = "honey"
        category_2.slug = "honey"
        category_2.save()

        product_1 = Product()
        product_1.name = "Молоко"
        product_1.slug = "milk1"
        product_1.category = Category.objects.first()
        product_1.description = "some text 1"
        product_1.qty = 15
        product_1.price = 2000
        product_1.save()
        product_2 = Product()
        product_2.name = "Мёд"
        product_2.slug = "honey1"
        product_2.category = Category.objects.get(slug="honey")
        product_2.description = "some text 2"
        product_2.qty = 25
        product_2.price = 4000
        product_2.save()

    def test_get_all_categories(self):
        all_categories = Category.objects.all()
        all_categories_from_func = get_all_categories()
        self.assertQuerysetEqual(all_categories, all_categories_from_func)

    def test_get_category_by_slug(self):
        correct_category = get_category_by_slug("milk")
        category_from_function = Category.objects.get(slug="milk")
        self.assertEqual(correct_category, category_from_function)

    def test_get_all_products(self):
        all_products = Category.objects.all()
        all_products_from_func = get_all_categories()
        self.assertQuerysetEqual(all_products, all_products_from_func)

    def test_get_product_by_slug(self):
        correct_product = get_product_by_slug("milk1")
        product_from_function = Product.objects.get(slug="milk1")
        self.assertEqual(correct_product, product_from_function)

    def test_add_new_category(self):
        data = {'name':'Масло', 'slug':'butter'}
        added_category = add_new_category(data)
        for field, value in data.items():
             self.assertEqual(getattr(added_category, field), value)

    def test_new_product(self):
        data = {
            'name': "Мёд",
            'category': "honey",
            'slug': 'honey3',
            'description': "some_text_here",
            'qty': 500,
            'price': 5000,
            }
        added_product = add_new_product(data)
        for field, value in data.items():
            if field == 'category':
                self.assertEqual(added_product.category.name, data['category'])
                continue
            self.assertEqual(getattr(added_product, field), value)


    def test_get_product_by_category(self):
        correct_products = Product.objects.filter(category__slug="milk") 
        products_by_function = get_products_by_category("milk")
        self.assertQuerysetEqual(correct_products, products_by_function)               
                    


