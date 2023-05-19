from django.urls import path
from apps.blog import views

app_name = "blog"
urlpatterns = [
    path('blog', views.blog, name='blog'),
]
