from django.conf.urls import url
from django.urls import path, re_path, include
from pracownicy import views

urlpatterns = [
    path('prac/', views.pracownik_login, name='pracownik_inne'),
]
