from django.urls import path
from apps.blog import views


app_name = "blog"
urlpatterns = [
    path('', views.blog, name='blog'),
    path('category/<int:category_id>/', views.get_category, name='category'),
    path('article/<int:article_id>/', views.article, name='article'),
    path('add_post/', views.add_post, name='add_post'),
]
