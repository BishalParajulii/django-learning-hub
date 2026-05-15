from django.shortcuts import render, redirect
import requests
from app.models import Product


def home(request):
    response = requests.get('https://dummyjson.com/products')
    data = response.json()

    return render(request, 'app/home.html', {
        'products': data['products']
    })


def save_product(request):

    if request.method == 'POST':

        title = request.POST.get('title')
        description = request.POST.get('description')
        category = request.POST.get('category')
        price = request.POST.get('price')
        thumbnail = request.POST.get('thumbnail')
        brand = request.POST.get('brand')

        Product.objects.get_or_create(
            title=title,
            defaults={
                'description': description,
                'category': category,
                'price': price,
                'thumbnail': thumbnail,
                'brand': brand
            }
        )

    return redirect('home')


def product_list(request):

    products = Product.objects.all()

    return render(request, 'app/product_list.html', {
        'products': products
    })