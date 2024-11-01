from django.shortcuts import render
from django.views import View

# Create your views here.
def index_view(request):
    return render(request, 'fourth_task/index.html')


def shop_view(request):
    games = ["Atomic Heart", "Cyberpunk 2077"]
    context = {'games': games}
    return render(request, 'fourth_task/shop.html', context)


def cart_view(request):
    return render(request, 'fourth_task/cart.html')
