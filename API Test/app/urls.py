from django.urls import path
from .views import jokes , JokesViewSet , validate_phone , joke_page

urlpatterns = [
    path('jokes/', jokes, name='jokes'),
    path('joke-page/', joke_page, name='joke-page'),
    path('my/jokes/' , JokesViewSet.as_view({'get': 'list', 'post': 'create'}), name='my-jokes'),
    path('validate-phone/', validate_phone, name='validate-phone'),
]