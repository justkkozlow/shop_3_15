from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post, Category

admin.site.register(Post)
admin.site.register(Category)


def get_photo(self, obj):
    if obj.photo:
        return mark_safe(f'<img src="{obj.photo.url}" width="75>')


get_photo.short_description = 'Миниатура'

admin.site.site_title = "БЛОГ"
admin.site.site_header = "БЛОГ"

