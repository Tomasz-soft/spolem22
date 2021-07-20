from django.urls import path
from . import views

urlpatterns = [
    path('wyb_sklep/<nskl>/', views.sklepy_detail, name='wyb_sklep'),
]
