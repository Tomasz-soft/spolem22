from django.urls import path, register_converter
from . import views
from datetime import datetime


class DateConverter:
    regex = '\d{4}-\d{1,2}-\d{1,2}'

    def to_python(self, value):
        return datetime.strptime(value, '%Y-%m-%d')

    def to_url(self, value):
        return value


register_converter(DateConverter, 'urldate')


urlpatterns = [
    path('promocje/<nskl>/', views.promocje_lista, name='lista_promocji'),
    path('pozycje_promocji/<nskl>/', views.pozprom_lista, name='pozycje_promocji'),
    path('promocja_szczeg/<nskl>/<int:nrprom>/',
         views.promocja_detail, name='promocja_szczegoly'),
    path('promocje_oddo/<nskl>/<urldate:data_od>/<urldate:data_do>/',
         views.promocje_oddo, name='promocja_oddo'),

]
