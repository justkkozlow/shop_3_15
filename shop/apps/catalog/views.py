from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from apps.catalog.models import Category, Product
from apps.catalog.forms import ContactForm


def index(request):
    data = {'slider_list': Product.objects.filter(slider=True),
            'chosen_list': Product.objects.filter(chosen=True)}

    return render(request, 'catalog/index.html', context=data)


def catalog(request, category_id=None):
    request_order = request.GET.get('order')
    sort_order = request_order if request_order else '?'
    products = Product.objects.all()
    if category_id:
        category = get_object_or_404(Category, pk=category_id)
        children = category.get_descendants(include_self=True)
        products = products.filter(category__in=children)
    products = products.order_by(sort_order)
    paginator = Paginator(products, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {
        'page_obj': page_obj,
        'current_id': category_id,
        'sort_order': sort_order
    }
    return render(request, 'catalog/catalog.html', data)


def product(request, product_id):
    data = {}
    product = get_object_or_404(Product, pk=product_id)
    data['product'] = product
    data['similar_products'] = Product.objects.filter(
        category=product.category
    ).exclude(id=product_id).order_by('chosen')[:4]

    return render(request, 'catalog/product.html', data)


def feedback(request):
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(form.cleaned_data['subject'],
                      form.cleaned_data['content'],
                      'kozlov.khv@gmail.com', ['kozlov.khv@gmail.com'],
                      )
            context = {'success': 1}
    else:
        form = ContactForm()

    context['form'] = form
    return render(request, 'catalog/about.html', context)
