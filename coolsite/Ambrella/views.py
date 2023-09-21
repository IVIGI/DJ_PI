# Для хранения представления будущего приложения.
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Страница приложения Ambrella")

def categorieys(request,cat_id):
    return HttpResponse(f"<h1> статьи под номером {cat_id} </h1>")
def index1(request):
    return HttpResponse("Дополнительная страница Ambrella Код: Красный")
def index2(request):
    return HttpResponse("EROR-404RED")
def ind(request):
    return HttpResponse("EROR-404 <img src=https://i.ytimg.com/vi/X5oGiXvIhxo/maxresdefault.jpg>")
def categorieys1(request):
    return HttpResponse("<h1> Документ №1 </h1>")
def categorieys_slug(request,cat):
    return HttpResponse(f"<h1> статья под категорией №  {cat} </h1>")