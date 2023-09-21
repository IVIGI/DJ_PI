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
def index2(request):
    return HttpResponse("EROR-404RED")
def ind(request):
    return HttpResponse("EROR-404 <img src=https://i.ytimg.com/vi/X5oGiXvIhxo/maxresdefault.jpg>")
def categorieys1(request):
    return HttpResponse("<h1> Документ №1 </h1>")
