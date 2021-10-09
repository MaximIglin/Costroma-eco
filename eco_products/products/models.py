import urllib
from tempfile import NamedTemporaryFile
import os

from django.db import models
from django.core.validators import MinValueValidator
from django.core.files import File



class Category(models.Model):
    """Данная модель описывает категории товаров"""
    name = models.CharField("Категория", max_length=300)
    slug = models.SlugField("слаг")
    image_url = models.URLField("Ссылка на изображение", max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to="category", verbose_name="Изображение", blank=True, null=True)

    def save(self, *args, **kwargs):

        if self.image_url and not self.image:
            temporary_image = NamedTemporaryFile(delete=True)
            temporary_image.write(urllib.request.urlopen(self.image_url).read())
            temporary_image.flush()
            self.image.save(f"{self.slug}.png", File(temporary_image))
        if self.image:    
            self.image.name = f"{self.slug}.png"    
        super(Category, self).save(*args, *kwargs)   


    class Meta:
        verbose_name = "Категории"
        db_table = "category"
        ordering = ['id']

    def __str__(self):
        return self.name    

class Product(models.Model):
    """Данная модель описывает инстансы продуктов"""
    name = models.CharField("Наименование", max_length=150)
    slug = models.SlugField("слаг", blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE, related_name="products")
    description = models.TextField("Описание продукта")
    qty = models.PositiveIntegerField(verbose_name="Количество", default=0)
    mass = models.DecimalField(max_digits=10,  decimal_places=2, verbose_name="Масса", null=True, blank=True, validators=[MinValueValidator(0)])
    volume = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Объём", null=True, blank=True, validators=[MinValueValidator(0)])
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена", validators=[MinValueValidator(0)])
    sale = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Скидка", validators=[MinValueValidator(0)])
    image = models.ImageField(upload_to="products", verbose_name="Изображение", blank=True, null=True)

    def save(self, *args, **kwargs):
        self.image.name = f"{self.slug}.jpeg"
        if self.sale > 0:
            self.price = self.price - self.price * (self.sale / 100)
        self.price = self.price    
        super(Product, self).save(*args, **kwargs)

    class Meta:
        ordering = ['category']
        verbose_name = "Продукт"
        db_table = "product"

    def __str__(self):
        return f"{self.name}: {self.price}"        


