from django.shortcuts import render
from django.views import View

# Create your views here.
def index_view(request):
    return render(request, 'third_task/index.html')


def shop_view(request):
    shop_items = ["Игра 1", "Игра 2", "Игра 3"]
    context = {'shop_items': shop_items}
    return render(request, 'third_task/shop.html', context)


def cart_view(request):
    return render(request, 'third_task/cart.html')
