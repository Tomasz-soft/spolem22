from datetime import datetime, date
from . import views
from django.urls import path, register_converter


class DateConverter:
    regex = '\d{4}-\d{1,2}-\d{1,2}'

    def to_python(self, value):
        return datetime.strptime(value, '%Y-%m-%d').date()

    def to_url(self, value):
        return value


register_converter(DateConverter, 'urldate')


urlpatterns = [
    path('promczascent_oddo/<urldate:data_od>/<urldate:data_do>/',
         views.promczascent_oddo, name='promczascent_oddo'),
    path('promczascent_szczeg/<int:nrprom>/',
         views.promczascent_detail, name='promocja_cent_szczegoly'),
    # path('promcent_dzis/',
    #     views.promcent_dzis, name='promocent_dzis'),
]
