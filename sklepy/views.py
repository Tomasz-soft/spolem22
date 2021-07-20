from django.db.models import query
from django.shortcuts import render

# Create your views here.
from django.http import response
from django.shortcuts import render

# Create your views here.


# Create your views here.
from sklepy.models import Sklepy
from promocje.models import Promocje
from sklepy.serializers import SklepySerializer

from rest_framework.permissions import AllowAny
from django.shortcuts import render
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from kalendarz.routers import kalendarzRouter


@csrf_exempt
@api_view(['GET'])
def sklepy_lista(request):

    if request.method == 'GET':
        try:
            sklepy_li = Sklepy.objects.filter(archive=False)
            sklepy_serializer = SklepySerializer(sklepy_li, many=True)

            odpowiedz = {
                'wiadomosc': "Sukces - Pobrano dane z sklepy.",
                'sklepy': sklepy_serializer.data,
                'error':  ""
            }
            return JsonResponse(odpowiedz, status=status.HTTP_200_OK)
        except:
            error = {
                'wiadomosc': "Bład -> nie mogę odczytać sklepy_lista",
                'sklepy': "[]",
                'error': ""
            }
            return JsonResponse(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@csrf_exempt
@api_view(['GET'])
def sklepy_detail(request, nskl):
    print("request:", request.data)
    try:
        sklepy_wyb = Sklepy.objects.get(db_name=nskl)
    except Sklepy.DoesNotExist:
        exceptionError = {
            'wiadomosc': "Nie znaleziono sklepu o db_name =%s" % nskl,
            'sklepy': "[]",
            'error': "Nie znaleziono - kod 404 error"
        }
        return JsonResponse(exceptionError, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        sklepy_serializer = SklepySerializer(sklepy_wyb)
        odpowiedz = {
            'wiadomosc': "Odczyt sklepu o db_name = %s" % nskl,
            'sklepy': [sklepy_serializer.data],
            'error': ""
        }
        return JsonResponse(odpowiedz, status=status.HTTP_200_OK)
