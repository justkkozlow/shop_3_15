from django.shortcuts import render, redirect

from .models import Post, Category
from .forms import PostForm


def blog(request):
    posts = Post.objects.all()
    blog_categories = Category.objects.all()
    context = {
        'posts': posts,
        'title': 'Категории',
        'blog_categories': blog_categories,
    }
    return render(request, 'blog/blog.html', context)


def article(request, article_id):
    posts = Post.objects.all()
    article_item = Post.objects.get(pk=article_id)

    return render(request, 'blog/article.html', {'article_item': article_item})


def get_category(request, category_id):
    posts = Post.objects.filter(category_id=category_id)
    blog_categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    data = {'posts': posts,
            'blog_categories': blog_categories,
            'category': category
            }

    return render(request, 'blog/category.html', data)


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/blog')
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})
