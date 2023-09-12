# Для хранения представления будущего приложения.
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Страница приложения Ambrella")

def categorieys(request):
    return HttpResponse("<h1> статьи по категориям </h1>")
def index1(request):
    return HttpResponse("Дополнительная страница Ambrella Код: Красный")
