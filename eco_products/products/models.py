from django.db import models
from django.core.validators import MinValueValidator


class Category(models.Model):
    """Данная модель описывает категории товаров"""
    name = models.CharField("Категория", max_length=300)
    slug = models.SlugField("слаг")
    image = models.CharField("Изображение", max_length=500)

    class Meta:
        verbose_name = "Категории"
        db_table = "category"
        ordering = ['name']

    def __str__(self):
        return self.name    

class SubCategory(models.Model):
    """Данная модель описывает подкатегории товаров"""
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField("Подкатегория", max_length=30)
    slug = models.SlugField("слаг")
    image = models.URLField("Изображение", null=True, blank = True)

    class Meta:
        verbose_name = "Подкатегории"
        db_table = "subcategory"
        ordering = ['name']

    def __str__(self):
        return self.name 


class Product(models.Model):
    """Данная модель описывает инстансы продуктов"""
    name = models.CharField("Наименование", max_length=150)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, verbose_name="Подкатегория",on_delete=models.CASCADE)
    description = models.TextField("Описание продукта")
    qty = models.PositiveIntegerField(verbose_name="Количество", default=0)
    mass = models.DecimalField(max_digits=10,  decimal_places=2, verbose_name="Масса", null=True, blank=True, validators=[MinValueValidator(0)])
    volume = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Объём", null=True, blank=True, validators=[MinValueValidator(0)])
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена", validators=[MinValueValidator(0)])
    sale = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Скидка", validators=[MinValueValidator(0)])
    images = models.JSONField(verbose_name="Изображения")

    def save(self, *args, **kwargs):
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


