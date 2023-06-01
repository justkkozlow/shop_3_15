from django.db import models
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование')
    content = models.TextField(verbose_name='Контент')
    date_posted = models.DateTimeField(default=timezone.now, verbose_name='Опубликовано')
    photo = models.ImageField(upload_to='blog_image/%Y/%m/%d', verbose_name='Фото', blank=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-date_posted']


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование категории')

    def get_absolute_url(self):
        return reverse('blog:category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['title']

