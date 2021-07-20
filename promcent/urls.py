
from django.urls import path, register_converter
from . import views
from datetime import datetime, date


class DateConverter:
    regex = '\d{4}-\d{1,2}-\d{1,2}'

    def to_python(self, value):
        return datetime.strptime(value, '%Y-%m-%d').date()

    def to_url(self, value):
        return value


register_converter(DateConverter, 'urldate')


urlpatterns = [
    path('promcent_oddo/<urldate:data_od>/<urldate:data_do>/',
         views.promcent_oddo, name='promocent_oddo'),
    path('promcent_szczeg/<int:nrprom>/',
         views.promcent_detail, name='promocja_cent_szczegoly'),
    path('promcent_dzis/',
         views.promcent_dzis, name='promocent_dzis'),
]
