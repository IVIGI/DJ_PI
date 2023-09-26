from django.urls import path, register_converter
from Ambrella.classconverctor import  FourDigitYearConverter
from Ambrella.views import *





register_converter(FourDigitYearConverter, "yyyy")

urlpatterns = [
    path('',index, name='home'),
    path('Ambrella_red/',index1, name='red'),
    path('RED_EROR/',index2, name='r_eror'),
    path('EROR/',ind, name='eror'),
    path('cat/<int:cat_id>/', categorieys, name='cat'),
    path('cat/<slug:cat>/', categorieys_slug, name = 'cat_slug'),
    path('cat2/<int:cat2_id>/', categorieys2, name = 'cat2'),
    path('cat3/<int:cat3_id>/', categorieys3,name = 'cat3'),
    path('cat4/<int:cat4_id>/', categorieys4, name = 'cat4'),
    path('spisok/<int:number>/', spisok, name = 'spisok'),
    path('date/<int:datee>/',date, name = 'date'),
    path("articles/<yyyy:year>/", year_archive, name = 'year'),

]
