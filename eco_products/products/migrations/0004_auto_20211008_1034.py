# Generated by Django 3.2.8 on 2021-10-08 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20211008_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='category', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='category',
            name='image_url',
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name='Ссылка на изображение'),
        ),
    ]
