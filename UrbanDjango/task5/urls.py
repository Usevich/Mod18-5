from django.urls import path
from .views import sign_up_by_html, sign_up_by_django

urlpatterns = [
    path('', sign_up_by_html, name='html_sign_up'),
    path('django_sign_up/', sign_up_by_django, name='django_sign_up'),
]