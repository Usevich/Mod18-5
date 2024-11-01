
# Create your views here.
from django.shortcuts import render
from django.views import View


def function_based_view(request):
    return render(request, 'second_task/func_template.html')


class ClassBasedView(View):
    def get(self, request):
        return render(request, 'second_task/class_template.html')
    