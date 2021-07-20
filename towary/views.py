# Create your views here.
from towary.serializers import TowarySerializer
from towary.models import Towary

from django.shortcuts import render
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from django.http import HttpResponse, response
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view


@csrf_exempt
@api_view(['GET', 'POST', 'DELETE'])
def towary_lista(request, nskl):
    if request.method == 'GET':
        try:
            towary_li = Towary.objects.using(nskl).all()
            towary_serializer = TowarySerializer(towary_li, many=True)
            odpowiedz = {
                'wiadomosc': "Sukces - Pobrano dane z towary dla sklepu %s" % nskl,
                'towary': towary_serializer.data,
                'error':  ""
            }
            return JsonResponse(odpowiedz, status=status.HTTP_200_OK)
        except:
            error = {
                'wiadomosc': "Bład -> nie mogę odczytać towary_lista",
                'towary': "[]",
                'error': ""
            }
            return JsonResponse(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == 'POST':
        try:
            towary_data = JSONParser().parse(request)
            towary_serializer = TowarySerializer(data=towary_data)

            if towary_serializer.is_valid():
                towary_serializer.save()
                print(towary_serializer.data)
                odpowiedz = {
                    'wiadomosc': "Sukces - pobrano Promocja o id = %d" % id,
                    'towary': [towary_serializer.data],
                    'error': ""
                }
                return JsonResponse(odpowiedz, status=status.HTTP_201_CREATED)
            else:
                error = {
                    'wiadomosc': "Nie mogę pobrać danych",
                    'towary': "[]",
                    'error': towary_serializer.error
                }
                return JsonResponse(error, status=status.HTTP_400_BAD_REQUEST)
        except:
            exceptionError = {
                'wiadomosc': "Błąd w pobieraniu danych",
                'towary': "[]",
                'error': "Wystąpił błąd"
            }
            return JsonResponse(exceptionError, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == 'DELETE':
        try:
            Towary.objects.all().delete()
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)
        except:
            exceptionError = {
                'wiadomosc': " nie można skutecznie skasować danych",
                'towary': "[]",
                'error': 'Wystąpił błąd'
            }
            return JsonResponse(exceptionError, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def towary_detail(request, pk):
    try:
        promocja = Towary.objects.get(pk=pk)
    except Towary.DoesNotExist:
        exceptionError = {
            'wiadomosc': "Nie znaleziono promocja 0 id =%s" % pk,
            'towary': "[]",
            'error': "Nie znaleziono - kod 404 error"
        }
        return JsonResponse(exceptionError, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        towary_serializer = TowarySerializer(Towary)
        odpowiedz = {
            'wiadomosc': "Odczyt towary o id = %s" % pk,
            'towary': [towary_serializer.data],
            'error': ""
        }
        return JsonResponse(odpowiedz, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        try:
            towary_data = JSONParser().parse(request)
            towary_serializer = TowarySerializer(Towary, data=towary_data)

            if towary_serializer.is_valid():
                towary_serializer.save()
                odpowiedz = {
                    'wiadomosc': "Zmiana w towary zakończona powodzeniem dla id = %s" % pk,
                    'towary': [towary_serializer],
                    'error': ""
                }
                return JsonResponse(odpowiedz)
            odpowiedz = {
                'wiadomosc': "Błąd w zapisie w towary dla id = %s" % pk,
                'towary': [towary_serializer.data],
                'error': towary_serializer.error
            }
            return JsonResponse(odpowiedz, status=status.HTTP_400_BAD_REQUEST)
        except request.method == 'DELETE':
            print("kasowanie towary o id=%s" % pk)
            Towary.delete()
            towary_serializer = TowarySerializer(Towary)
            odpowiedz = {
                'wiadomosc': " Promocja o id = %s został skasowany" % pk,
                'towary': [towary_serializer.data],
                'error': ""
            }
            return JsonResponse(odpowiedz)
