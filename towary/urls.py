from django.urls import path
from . import views

urlpatterns = [
    path('towary/<nskl>/', views.towary_lista, name='lista_towarow'),
]
