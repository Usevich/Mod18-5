from django.urls import path, include
from .views import index_view, shop_view, cart_view

urlpatterns = [
    path('', index_view, name='home'),
    path('shop/', shop_view, name='shop'),
    path('cart/', cart_view, name='cart'),
]
