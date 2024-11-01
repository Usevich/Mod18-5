from django.urls import path, include
from .views import function_based_view, ClassBasedView

urlpatterns = [
    path('function/', function_based_view, name='function_view'),
    path('class/', ClassBasedView.as_view(), name='class_view'),
    ]