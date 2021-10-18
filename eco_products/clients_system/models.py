from django.db import models
from products.models import Product

class Client(models.Model):
    """This models is describe clients"""
    first_name = models.CharField("Имя", max_length=150)
    last_name = models.CharField("Фамилия", max_length=150)
    city = models.CharField("Город", max_length=150)
    full_adress = models.CharField("Адрес", max_length=150)
    phone = models.CharField("Номер телефона", max_length=20)
    email = models.EmailField("Адресс электронной потчы")
    orderings = models.PositiveIntegerField(verbose_name="Количество заказов", default=0)

    class Meta:
        db_table = "clients"
        verbose_name_plural = "Клиенты"
        ordering = ["first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.city}"

class Order(models.Model):
    """This model is describe user's order"""
    client = models.ForeignKey(to=Client, verbose_name="Клиент", on_delete=models.CASCADE, null=True)
    products = models.ManyToManyField(Product, verbose_name="Товары")
    order_list = models.TextField(verbose_name="Полный текст заказа")
    final_price = models.PositiveIntegerField(verbose_name="Финальная цена заказа")
    comment = models.TextField(verbose_name="Комментарий к заказу", blank=True, null=True)
    delivery = models.BooleanField(verbose_name="Доставка (да или нет)")
    time = models.DateTimeField(verbose_name="Время заказа")
    adress = models.CharField(verbose_name="Адрес доставки", max_length=150, blank=True, null=True)


    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        db_table = "orders"

    def __str__(self):
        return f"Заказ: {self.client.first_name} {self.client.last_name} от {self.time}"        

