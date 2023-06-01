from django.urls import path

from apps.catalog import views


app_name = 'catalog'
urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog, name='catalog'),
    path('about/', views.feedback, name='about'),
    path('catalog/<int:category_id>/', views.catalog, name='catalog'),
    path('product/<int:product_id>/', views.product, name='product'),
]
