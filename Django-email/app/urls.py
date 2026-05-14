from django.urls import path
from .views import send_email , get_email

urlpatterns = [
    path('send-email/', send_email, name='send_email'),
    path('get-email/', get_email, name='get_email'),
]