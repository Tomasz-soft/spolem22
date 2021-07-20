from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from prominfo.models import PromCentInfo, PromCentInfoOnly
from prominfo.serializers import PromCentInfoSerializer, PromCentInfoOnlySerializer, PromCentInfoOnlySerializer2
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from sklepy.models import Nag_rach


@csrf_exempt
@api_view(['GET'])
def prominfo_oddo(request, data_od, data_do):
    promcentinfo = PromCentInfoOnly.objects.using('centrala').filter(
        datazak_od__gt=data_od, datazak_do__lte=data_do)

    promcentinfo_serializer = PromCentInfoOnlySerializer(
        promcentinfo, many=True)
    odpowiedz = {
        'wiadomosc': "sukces - Pobrano dane z promcemtinfo",
        'promcentinfo': promcentinfo_serializer.data,
        'error': ""
    }
    return JsonResponse(odpowiedz, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['GET'])
def prominfoc_oddo(request, data_od, data_do):
    try:
        promcentinfo = PromCentInfo.objects.using(
            'centrala').select_related('nr_prom').filter(
            datazak_od__gt=data_od, datazak_do__lte=data_do)
    except:
        error = {
            'wiadomosc': "Bład -> nie mogę odczytać promcent_oddo",
            'promocje': '',
            'error': "error"
        }
        return JsonResponse(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    promcinfo = []
    for promc in promcentinfo:
        try:
            promcinfo.append({
                'datazak_od': promc.datazak_od,
                'datazak_do': promc.datazak_do,
                'uwagi': promc.uwagi,
                'id_prac': promc.id_prac,
                'nazwa_prom': promc.nazwa_prom,
                'data_b_prom': promc.nr_prom.od_dnia,
                'data_e_prom': promc.nr_prom.do_dnia,
                'numer_rach': promc.nr_prom.numer_rach
            })

        except Nag_rach.DoesNotExist:
            promcinfo.append({
                'datazak_od': promc.datazak_od,
                'datazak_do': promc.datazak_do,
                'uwagi': promc.uwagi,
                'id_prac': promc.id_prac,
                'nazwa_prom': promc.nazwa_prom,
                'data_b_prom': None,
                'data_e_prom': None,
                'numer_rach': None
            })

    promcentinfo_serializer = PromCentInfoOnlySerializer2(
        promcinfo, many=True)
    odpowiedz = {
        'wiadomosc': "sukces - Pobrano dane z promcemtinfo",
        'promcentinfo': promcentinfo_serializer.data,
        'error': ""
    }
    return JsonResponse(odpowiedz, status=status.HTTP_200_OK)


@ csrf_exempt
@ api_view(['GET', 'PUT', 'POST', 'DELETE'])
def prominfo_update(request=None, numerprom=None):
    if numerprom == None:

        promcenterror = {
            'wiadomosc': "Nie moge pobrać danych",
            'promcentinfo': "[]",
            'error': "błąd parametru"
        }
        return JsonResponse(promcenterror, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'POST':
        # try:
        promcent_data = JSONParser().parse(request)
        print('promcent_data:', promcent_data)
        promcent_serializer = PromCentInfoOnlySerializer(
            data=promcent_data)

        if promcent_serializer.is_valid():
            promcent_serializer.save()
            print(promcent_serializer.data)
            odpowiedz = {
                'wiadomosc': "Sukces - wpisano informacje",
                'promcentinfo': [promcent_serializer.data],
                'error': ""
            }
            return JsonResponse(odpowiedz, status=status.HTTP_201_CREATED)
        else:
            promcenterror = {
                'wiadomosc': "Nie moge wpisac danych",
                'promcentinfo': "[]",
                'error': promcent_serializer.errors
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
        if (request.method == 'GET'):
            try:
                promuwagi = Nag_rach.objects.using(
                    'centrala').select_related('NagRach').get(NagRach__nr_prom=numerprom)
            except PromCentInfoOnly.DoesNotExist:
                exceptionError = {
                    'wiadomosc': "Nie znaleziono DANYCH O nr_prom =%s" % numerprom,
                    'promuwagi': "[]",
                    'error': "Nie znaleziono - kod 404 error"
                }
                return JsonResponse(exceptionError, status=status.HTTP_404_NOT_FOUND)
            try:
                pruwagi = {
                    'datazak_od': promuwagi.NagRach.datazak_od,
                    'datazak_do': promuwagi.NagRach.datazak_do,
                    'uwagi': promuwagi.NagRach.uwagi,
                    'id_prac': promuwagi.NagRach.id_prac,
                    'nazwa_prom': promuwagi.NagRach.nazwa_prom,
                    'data_b_prom': promuwagi.od_dnia,
                    'data_e_prom': promuwagi.do_dnia,
                    'numer_rach': promuwagi.numer_rach
                }
            except ObjectDoesNotExist:
                pruwagi = {
                    'datazak_od': None,
                    'datazak_do': None,
                    'uwagi': None,
                    'id_prac': None,
                    'nazwa_prom': None,
                    'data_b_prom': promuwagi.od_dnia,
                    'data_e_prom': promuwagi.do_dnia,
                    'numer_rach': promuwagi.numer_rach
                }
            promcent_serializer = PromCentInfoOnlySerializer2(pruwagi)
            odpowiedz = {
                'wiadomosc': 'Pobrano Uwaga do promocji o nr_prom = %s ' % numerprom,
                'promuwagi': [promcent_serializer.data],
                'error': ""
            }
            return JsonResponse(odpowiedz)

        elif (request.method == 'DELETE'):
            try:
                promuwagi = PromCentInfoOnly.objects.using(
                    'centrala').get(nr_prom=numerprom)
            except PromCentInfoOnly.DoesNotExist:
                exceptionError = {
                    'wiadomosc': "Nie znaleziono DANYCH O nr_prom =%s" % numerprom,
                    'promuwagi': "[]",
                    'error': "Nie znaleziono - kod 404 error"
                }
                return JsonResponse(exceptionError, status=status.HTTP_404_NOT_FOUND)

            promuwagi.delete()
            promcent_serializer = PromCentInfoOnlySerializer(promuwagi)
            odpowiedz = {
                'wiadomosc': 'Uwaga do promocji o nr_prom = %s zostala saksowana' % numerprom,
                'promuwagi': [promcent_serializer.data],
                'error': ""
            }
            return JsonResponse(odpowiedz)

        elif (request.method == 'PUT'):
            print("request:", request)
            promcentinfo_data = JSONParser().parse(request)
            nrprom = promcentinfo_data['nr_prom']
            try:
                promuwagi = PromCentInfoOnly.objects.using(
                    'centrala').get(nr_prom=nrprom)
            except PromCentInfoOnly.DoesNotExist:

                exceptionError = {
                    'wiadomosc': "Nie znaleziono DANYCH O nr_prom =%s" % nrprom,
                    'promuwagi': "[]",
                    'error': "Nie znaleziono - kod 404 error"
                }
                return JsonResponse(exceptionError, status=status.HTTP_404_NOT_FOUND)

            promcent_serializer = PromCentInfoOnlySerializer(promuwagi,
                                                             data=promcentinfo_data)

            if promcent_serializer.is_valid():
                promcent_serializer.save()
                odpowiedz = {
                    'wiadomosc': 'Zmiana w promcentinfo zakończona powodzeniem',
                    'promuwagi': "[]",
                    'error': ""
                }
                return JsonResponse(odpowiedz)
            odpowiedz = {
                'wiadomosc': 'Błąd w zapisie promcemntinfo dla nr_prom = %s' % nrprom,
                'promuwagi': [promcent_serializer.data],
                'error': promcent_serializer.errors
            }
            return JsonResponse(odpowiedz, status=status.HTTP_400_BAD_REQUEST)


def get_prominfo(nrprom):
    try:
        dane_prominfo = PromCentInfoOnly.objects.using(
            'centrala').filter(status=0).get(nr_prom=nrprom)
        prinfo = PromCentInfoOnlySerializer(dane_prominfo)
    except PromCentInfoOnly.DoesNotExist:
        prinfo = [('status_prominfo', None),
                  ('datazak_od', None),
                  ('datazak_do', None),
                  ('uwagi', None),
                  ('nr_prom', None),
                  ('id_prac', None)
                  ]

    return prinfo
