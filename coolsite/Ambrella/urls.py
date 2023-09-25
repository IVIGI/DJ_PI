from django.urls import path

from Ambrella.views import *

urlpatterns = [
    path('Ambrella/',index),
    path('Ambrella_red/',index1),
    path('RED_EROR/',index2),
    path('EROR/',ind),
    path('cat/<int:cat_id>/', categorieys),
    path('cat/<slug:cat>/', categorieys_slug),
    path('cat2/<int:cat2_id>/', categorieys2),
    path('cat3/<int:cat3_id>/', categorieys3),
    path('cat4/<int:cat4_id>/', categorieys4),
    path('spisok/<int:number>/', spisok),
    path('date/<int:datee>/',date),

]
