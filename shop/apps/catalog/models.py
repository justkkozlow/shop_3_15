from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=50, verbose_name='Название категории')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', verbose_name='Родитель')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(max_length=80, verbose_name='Наименование')
    price = models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    photo = models.ImageField(upload_to='catalog_images', verbose_name='Фото', blank=True)
    chosen = models.BooleanField(default=False, verbose_name='Добавить в избранное')
    slider = models.BooleanField(default=False, verbose_name='Добавить в слайдер')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Image(models.Model):
    image = models.ImageField(upload_to='images')
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name = "Изоображения"
        verbose_name_plural = "Изоображения"
