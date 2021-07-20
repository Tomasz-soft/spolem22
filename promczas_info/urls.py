from django.conf.urls import url
from django.urls import path, re_path, include, register_converter
from promczas_info import views
from datetime import datetime


class DateConverter:
    regex = '\d{4}-\d{1,2}-\d{1,2}'

    def to_python(self, value):
        return datetime.strptime(value, '%Y-%m-%d').date()

    def to_url(self, value):
        return value


register_converter(DateConverter, 'urldate')


urlpatterns = [
    path('promczasinfo_update/<int:numerprom>/',
         views.promczasinfo_update, name='promczasinfo_update'),
    path('promczasinfo_oddo/<urldate:data_od>/<urldate:data_do>/',
         views.promczasinfo_oddo, name='promoczasinfo_oddo'),

]
