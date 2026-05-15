
from django.urls import path , include
from app.views import home , save_product , product_list

urlpatterns = [
    path('', home, name='home'),
    path('save_product/', save_product, name='save_product'),
    path('product_list/', product_list, name='product_list'),
]
