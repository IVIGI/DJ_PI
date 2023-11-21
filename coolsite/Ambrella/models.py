# #Для хранения ORM-моделей и для представления данных из базы данных
from django.db import models
#
# data_db = [{'id': 1, 'FIO': 'Снытко Руслан Николаевич', 'intresting': 'вязание, дизайн, верстка, вышивание крестиком',
#             'diplom_red': True},
#            {'id': 2, 'FIO': 'Король Богдан Александрович',
#             'intresting': 'парашутный спорт, бокс , страйкбол,спортивный туризм', 'diplom_red': True},
#            {'id': 3, 'FIO': 'Тузов Александр Максимович', 'intresting': 'курение, автомобили, спорт, компьютерные игры',
#             'diplom_red': False},
#
#            ]s

class  Students (models.Model):
    fio = models.CharField(max_length=50)
    interesting = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    dipolom_red = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255,db_index=True, unique=True,verbose_name='URL')
#

class Book (models.Model):
    NAME_BOOK = models.CharField(max_length=50)
    AUFTOR = models.CharField(max_length=50)
    PRICE = models.IntegerField(default=0)

def __str__(self):
    return self.PRICE