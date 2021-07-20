from django.conf.urls import url
from django.urls import path, re_path, include, register_converter
from prominfo import views
from datetime import datetime


class DateConverter:
    regex = '\d{4}-\d{1,2}-\d{1,2}'

    def to_python(self, value):
        return datetime.strptime(value, '%Y-%m-%d')

    def to_url(self, value):
        return value


register_converter(DateConverter, 'urldate')

urlpatterns = [
    path('prominfo/',
         views.prominfo_update, name='prominfo_update'),
    path('prominfo/<int:numerprom>/', views.prominfo_update, name='prominfo_get'),
    path('prominfo_oddo/<urldate:data_od>/<urldate:data_do>/',
         views.prominfoc_oddo, name='prominfo_oddo')

]
