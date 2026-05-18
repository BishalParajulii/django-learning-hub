from django.urls import path 
from .views import ProductListView , search_product


urlpatterns = [
path('', ProductListView, name='product-list'),
path('search/', search_product, name='search-product'),
]
