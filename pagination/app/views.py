
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product
from django.db.models import Q

# Create your views here.
def ProductListView(request):
    products = Product.objects.all().order_by('-id')
    paginator = Paginator(products, 10)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app/list.html', {'page_obj': page_obj , 'mode' : 'list'})


def search_product(request):
    query = request.GET.get('q', '')

    results = Product.objects.none()

    if query:
        results = Product.objects.filter(
            Q(name__icontains=query)
        )

    return render(request, 'app/list.html', {
        'search_results': results,
        'query': query,
        'mode': 'search'   
    })
    