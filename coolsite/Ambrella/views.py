# Для хранения представления будущего приложения.
from django.contrib.sites import requests
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    print(request.GET)
    return HttpResponse(f"Страница приложения Ambrella ")


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

def categorieys2 (request,cat2_id):
    return HttpResponse(f"<h1> документация № {cat2_id} </h>")
def categorieys3 (request,cat3_id):
    return HttpResponse(f"<h1> Секретные документация № {cat3_id} </h>")
def categorieys4 (request,cat4_id):
    return HttpResponse(f"<h1> Документация о наработках № {cat4_id} </h>")
def spisok(request,number):
    dir={
        "1":['Игнатьев А.А. 28.06.2001'],
        "2": ['Коновалов А. 2004'],
        "3": ['Тузов А. 2004'],
        "4": ['Ковалёв А. 2002'],
        "5": ['Король Б. 2002'],
        "6": ['Снытко Р. 2004'],
        "7": ['Лебедев Д. 2004'],
        "8": ['Мартыненко Д.Д 2005'],
        "9": ['Лелетко П. 2001'],
        "10": ['Селебин А. 2004'],
               }
    if number > 0 and number < 10:
        return HttpResponse(f"<h1> Студент {dir[str(number)][0]} найден </h1>")
    else:
        return redirect('r_eror', permanent=True)
def date(request,datee):

    dir = {
        "2001": ['Игнатьев А.А. 28.06.2001','Лелетко П. 2001'],
        "2002": ['Ковалёв А. 2002','Король Б. 2002'],
        "2003": ['Студентов этого года нет'],
        "2004": ['Тузов А. 2004','Коновалов А. 2004','Снытко Р. 2004','Лебедев Д. 2004','Селебин А. 2004'],
        "2005": ['Мартыненко Д.Д 2005'],

    }
    if datee > 2001 and datee < 2005:
        return HttpResponse(f"<h1> Студенты {dir[str(datee)]} найдены </h1>")
    else:
        return redirect('eror', permanent=True)

def year_archive(request,year):
    if (int(year)) > 2023:
        raise Http404()
    if (int(year)) < 2000:
        return redirect('home', permanent=True)
    return HttpResponse(f"<h1> Год издания {year} </h1>")

def pageNotFound (request,exception):
    return HttpResponseNotFound(f"<h1> Страница не найдена <br> {exception}</h1>")

def save_data(request):
    if request.method == 'GET':
        data = request.GET.get('GET', '')
        with open('GET.txt', 'a') as file:
            file.write(data + '\n')
        return HttpResponse('Данные успешно записаны в файл')
    else:
        return HttpResponse('Метод запроса должен быть GET')

def FailServer(request):
    return HttpResponseNotFound(f"<h1> Ошибка сервера <br> </h1>")

def AccessВenied(request, exception):
    return HttpResponseNotFound(f"<h1> Запрещено в доступе <br> {exception}</h1>")

def ProcessingFail(request, exception):
    return HttpResponseNotFound(f"<h1> Неверный запрос <br> {exception}</h1>")
