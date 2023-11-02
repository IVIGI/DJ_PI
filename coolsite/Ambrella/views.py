# Для хранения представления будущего приложения.
from contextvars import Context
from django.contrib.sites import requests
from django.core.exceptions import SuspiciousOperation, PermissionDenied
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from django.template.loader import render_to_string



menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Домашняя', 'url_name': 'home'},
        {'title': 'Красивый css', 'url_name': 'cub'},
        ]
def show_spisok(request, spisok_id):
    return HttpResponse(f"Отображение списка студента = {spisok_id}")

spisok_db = [
    {'id' : 1, 'title' : 'Игнатьев А.А.', 'content': '28.06.2001','is_published': True},
    {'id': 2, 'title': 'Коновалов А.', 'content': '2004','is_published': True},
    {'id': 3, 'title': 'Тузов А.', 'content': '2004','is_published': True},
    {'id': 4, 'title': 'Ковалёв А.', 'content': '2002','is_published': True},
    {'id': 5, 'title': 'Король Б.', 'content': '2002','is_published': True},
    {'id': 6, 'title': 'Снытко Р.', 'content': '2004','is_published': True},
    {'id': 7, 'title': 'Лебедев Д.', 'content': '2004','is_published': False},
    {'id': 8, 'title': 'Мартыненко Д.', 'content': '2005','is_published': True},
    {'id': 9, 'title': 'Лелетко П.', 'content': '2001','is_published': True},
    {'id': 10, 'title': 'Селебин А.', 'content': '2004','is_published': True},
]

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
]

class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
def index(request):
    # t = render_to_string('Ambrella/index.html')
    # return HttpResponse(t) // Пример ниже !!!!  можно так как 1 пример, можно как ниже!
    data = {'title': 'главная страница',
            'menu':menu,
            'value': 1,
            'url': slugify ("OCHEN KRUTOY KURSACH"),
            'int': 2023,
            'tup': [1,2.0,"hello"],
            'bool': True,
            'float': 28.56,
            'list': [1, 2, 'abc', True],
            'set': {1, 1, 2, 3, 2, 5},
            'dict': {'Key_1': 'value_1|', 'key_2': 'value_2'},
            'obj': MyClass(10,20),
            'get':(request.GET),
            'posts': data_db,
            'spisok':spisok_db,

            }

    return render(request,'Ambrella/index.html',context=data)
    # // пример передачи параметра 1
    # return render(request, 'Ambrella/index.html', {'title': 'Главная страница'})
def about(request):
    return render(request, 'Ambrella/about.html', context={'menu': menu})
def cub(request):
    return render(request, 'Ambrella/3D_kub.html', context={'menu': menu, 'title':'красивый css'})
def post_detail(request):
    get_vuv = dict(request.GET)
    if get_vuv:
        print(request.GET)
        for k,v in get_vuv.items():
            print(k,v)
        response_string = ''
        for kluch, value in get_vuv.items():
            response_string += f'{kluch} = {value[0]} |'
        return HttpResponse(response_string)
    else:
        return HttpResponse("GET Empty")
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
    if (int(year)) == 2024:
        raise SuspiciousOperation
    if (int(year)) == 2025:
        raise PermissionDenied
    if (int(year)) == 2026:
        raise Context
    if (int(year)) > 2027:
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

def about(request):
    return render(request, 'Ambrella/about.html', context={'menu': menu, 'title': 'О программе'})

def split_line(line, sep):
    if not line:
        return ['']
    list1=[]
    strok=""
    cavuchka = False
    for i in line:
        if '"'  in i:
            cavuchka = not cavuchka
        if sep in i and cavuchka == False :
            list1.append(strok.replace('"',''))
            strok = ""
        else:
            strok += i
    list1.append(strok.replace('"',''))
    return list1

def read_split_line_tests():
    example_1_line = 'Александр Александрович Александров,,2005,11'
    example_1_sep = ','
    example_1_res = ['Александр Александрович Александров', '', '2005', '11']

    print(split_line(example_1_line, example_1_sep), example_1_res)

    example_2_line = 'Евгений Сергеевич Дёмин;;'
    example_2_sep = ';'
    example_2_res = ['Евгений Сергеевич Дёмин', '', '']

    print(split_line(example_2_line, example_2_sep), example_2_res)

    example_3_line = 'Анна Павловна Иванова,"[запись 1, запись 2, запись 3]", ,2'
    example_3_sep = ','
    example_3_res = ['Анна Павловна Иванова', '[запись 1, запись 2, запись 3]', ' ', '2']

    print(split_line(example_3_line, example_3_sep), example_3_res)

    print('Все тесты прошли успешно!')

def split_line1(request):

    return HttpResponse(f"<h1></h1>")