from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from promczas_info.models import PromCzasInfoOnly, PromCzasInfo
from promczas_info.serializers import PromCzasInfoOnlySerializer
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view


@csrf_exempt
@api_view(['GET'])
def promczasinfo_oddo(request, data_od, data_do):
    try:
        promczasinfo = PromCzasInfoOnly.objects.using('centrala').filter(
            datazak_od__gt=data_od, datazak_do__lte=data_do)

        promczasinfo_serializer = PromCzasInfoOnlySerializer(
            promczasinfo, many=True)
        odpowiedz = {
            'wiadomosc': "sukces - Pobrano dane z promcemtinfo",
            'promcentinfo': promczasinfo_serializer.data,
            'error': ""
        }
        return JsonResponse(odpowiedz, status=status.HTTP_200_OK)
    except:
        error = {
            'wiadomosc': "Bład -> nie mogę odczytać promocje_czasowe",
            'promocje': "[]",
            'error': ""
        }
        return JsonResponse(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@csrf_exempt
@api_view(['GET', 'PUT', 'POST', 'DELETE'])
def promczasinfo_update(request=None, numerprom=None):
    if request.method == 'POST':
        # try:
        promczasinfo_data = JSONParser().parse(request)
        print('promczasinfo_data:', promczasinfo_data)
        promczasinfo_serializer = PromCzasInfoOnlySerializer(
            data=promczasinfo_data)

        if promczasinfo_serializer.is_valid():
            promczasinfo_serializer.save()
            print(promczasinfo_serializer.data)
            odpowiedz = {
                'wiadomosc': "Sukces - wpisano informacje",
                'promcentinfo': [promczasinfo_serializer.data],
                'error': ""
            }
            return JsonResponse(odpowiedz, status=status.HTTP_201_CREATED)
        else:
            promcenterror = {
                'wiadomosc': "Nie moge wpisac danych",
                'promcentinfo': "[]",
                'error': promczasinfo_serializer.errors
            }
            return JsonResponse(promcenterror, status=status.HTTP_400_BAD_REQUEST)
        # except:
        #     exceptionError = {
        #         'wiadomosc': "Błąd w pobieraniu danych",
        #         'promcentifo': "[]",
        #         'error': "Wystąpił błąd"
        #     }
        return JsonResponse(exceptionError, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    else:
        if (request.method == 'GET') or (request.method == 'DELETE'):
            print("kaaassssowwwanie nrprom:", numerprom)
            try:
                promczasuwagi = PromCzasInfoOnly.objects.using(
                    'centrala').get(nr_prom=numerprom)
            except PromCzasInfoOnly.DoesNotExist:
                exceptionError = {
                    'wiadomosc': "Nie znaleziono DANYCH O nr_prom =%s" % numerprom,
                    'promuwagi': "[]",
                    'error': "Nie znaleziono - kod 404 error"
                }
                return JsonResponse(exceptionError, status=status.HTTP_404_NOT_FOUND)
            if (request.method == 'GET'):
                promczasinfo_serializer = PromCzasInfoOnlySerializer(
                    promczasuwagi)
                odpowiedz = {
                    'wiadomosc': 'Pobrano Uwaga do promocji o nr_prom = %s ' % numerprom,
                    'promuwagi': [promczasinfo_serializer.data],
                    'error': ""
                }
                return JsonResponse(odpowiedz)
            else:
                print('request.method:', request.method)
                print("dudududududdu", "numerprom:",
                      numerprom, "data:", request.data)

                promczasuwagi.delete()
                promczasinfo_serializer = PromCzasInfoOnlySerializer(
                    promczasuwagi)
                odpowiedz = {
                    'wiadomosc': 'Uwaga do promocji o nr_prom = %s zostala saksowana' % numerprom,
                    'promuwagi': [promczasinfo_serializer.data],
                    'error': ""
                }
                return JsonResponse(odpowiedz)

        elif (request.method == 'PUT'):
            print("request:", request)
            promczasinfo_data = JSONParser().parse(request)
            print("aaaaaaaaaaaaa:", promczasinfo_data)
            nrprom = promczasinfo_data['nr_prom']
            try:
                promuwagi = PromCzasInfoOnly.objects.using(
                    'centrala').get(nr_prom=nrprom)
            except PromCzasInfoOnly.DoesNotExist:

                exceptionError = {
                    'wiadomosc': "Nie znaleziono DANYCH O nr_prom =%s" % nrprom,
                    'promuwagi': "[]",
                    'error': "Nie znaleziono - kod 404 error"
                }
                return JsonResponse(exceptionError, status=status.HTTP_404_NOT_FOUND)

            promczasinfo_serializer = PromCzasInfoOnlySerializer(promuwagi,
                                                                 data=promczasinfo_data)

            if promczasinfo_serializer.is_valid():
                promczasinfo_serializer.save()
                odpowiedz = {
                    'wiadomosc': 'Zmiana w promcentinfo zakończona powodzeniem',
                    'promuwagi': "[]",
                    'error': ""
                }
                return JsonResponse(odpowiedz)
            odpowiedz = {
                'wiadomosc': 'Błąd w zapisie promcemntinfo dla nr_prom = %s' % nrprom,
                'promuwagi': [promczasinfo_serializer.data],
                'error': promczasinfo_serializer.errors
            }
            return JsonResponse(odpowiedz, status=status.HTTP_400_BAD_REQUEST)
