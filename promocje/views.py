# Create your views here.
from django.db.models.query import prefetch_related_objects
from sklepy.models import BazyRach
from django.http import response
from django.shortcuts import render
from datetime import datetime
# Create your views here.


# Create your views here.
from promocje.serializers import PromocjeSerializer, PozPromSerializer, SzczPromSerializer, PromocjeSerializer2
from promocje.models import Promocje, PozProm
from prominfo.views import get_prominfo
from towary.models import Towary

from django.shortcuts import render
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from datetime import datetime, timedelta
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q


@csrf_exempt
@api_view(['GET'])
def promocje_lista(request, nskl):

    if request.method == 'GET':
        try:
            promocje_li = Promocje.objects.using(nskl).all()
            promocje_serializer = PromocjeSerializer(promocje_li, many=True)
            odpowiedz = {
                'wiadomosc': "Sukces - Pobrano dane z promocje dla sklepu %s" % nskl,
                'promocje': promocje_serializer.data,
                'error':  ""
            }
            return JsonResponse(odpowiedz, status=status.HTTP_200_OK)
        except:
            error = {
                'wiadomosc': "Bład -> nie mogę odczytać promocje_lista",
                'promocje': "[]",
                'error': ""
            }
            return JsonResponse(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@csrf_exempt
@api_view(['GET'])
def promocje_oddo(request, nskl, data_od, data_do):

    if request.method == 'GET':
        try:
            # promocje_li = Promocje.objects.using(nskl).filter(data_e_prom__gte=datetime.strptime(
            #    data_od, "%y-%m-%d").date(), data_b_prom__lte=datetime.strptime(data_do, "%y-%m-%d").date())

            promocje_li = Promocje.objects.using(nskl).filter(
                data_e_prom__gt=data_od+timedelta(days=1), data_b_prom__lte=data_do, status=0)

            lista_prom = []
            for prom in promocje_li:
                if prom.id_e_prac is not None and prom.id_e_prac > 0:
                    prom.data_e_prom -= timedelta(days=1)
                lista_prom.append({
                    'status': prom.status,
                    'id_prom': prom.id_prom,
                    'data_b_prom': prom.data_b_prom,
                    'data_e_prom': prom.data_e_prom,
                    'data_d_prom': prom.data_d_prom,
                    'uwagi_prom': prom.uwagi_prom,
                    'nr_prom': prom.nr_prom,
                    'stat_prom': prom.stat_prom
                })

            promocje_serializer = PromocjeSerializer(lista_prom, many=True)
            #print('data-data:', promocje_serializer.data)

            # for prom in promocje_serializer.data:
            #     print('prom:', prom, 'prom[nr_prom]', prom['nr_prom'])

            #     nr = prom['nr_prom']
            #     if nr > 0:
            #         aa = get_prominfo(nr)

            #     print('prom_aa:', aa)

            odpowiedz = {
                'wiadomosc': "Sukces - Pobrano dane z promocje dla sklepu %s" % nskl,
                'promocje': promocje_serializer.data,
                'error':  ""
            }
            return JsonResponse(odpowiedz, status=status.HTTP_200_OK)
        except:
            error = {
                'wiadomosc': "Bład -> nie mogę odczytać promocje_lista",
                'promocje': "[]",
                'error': "error"
            }
            return JsonResponse(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@ csrf_exempt
@ api_view(['GET'])
def promocja_detail(request, nskl, nrprom):
    try:
        promocja = PozProm.objects.using(
            nskl).select_related('id_tow', 'id_prom').filter(id_prom__nr_prom=nrprom)
    except Promocje.DoesNotExist:
        exceptionError = {
            'wiadomosc': "Nie znaleziono promocja 0 id =%s" % nrprom,
            'promocje': "[]",
            'error': "Nie znaleziono - kod 404 error"
        }
        return JsonResponse(exceptionError, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        pozycje_prom = []
        for pozp in promocja:
            pozycje_prom.append({
                'status': pozp.status,
                # 'id_pprom': pozp.id_pprom,
                # 'id_prom': pozp.id_prom,
                'id_tow': pozp.id_tow.id_tow,
                'bar_kod_tow': pozp.id_tow.bar_kod_tow,
                'cena_d_tow': pozp.id_tow.cena_d_tow,
                'nazwa_tow': pozp.id_tow.nazwa_tow,
                # 'nazwa_tow': pozp.id_tow.nazwa_tow,
                'cena_d_old': pozp.cena_d_old,
                'cena_d_prom': pozp.cena_d_prom,
                'ilosc_prom': pozp.ilosc_prom,
                'obrot_prom': pozp.obrot_prom,
                'id_knt': pozp.id_knt,
                # 'data_b_prom': pozp.data_e_prom,
                # 'data_e_prom': pozp.data_e_prom,
                'stat_prom': pozp.stat_prom,
                # 'cena_zakupu': pozp.cena_zakupu,
                # 'ilosc_prog': pozp.ilosc_prog
            })

        # pozprom_serializer = PozPromSerializer(promocja, many=True)
        pozprom_serializer = SzczPromSerializer(pozycje_prom, many=True)
        odpowiedz = {
            'wiadomosc': "Odczyt promocje o nr_prom = %s" % nrprom,
            'promocje': pozprom_serializer.data,
            'error': ""
        }
        return JsonResponse(odpowiedz, status=status.HTTP_200_OK)


@ csrf_exempt
@ api_view(['GET'])
def pozprom_lista(request, nskl):
    if request.method == 'GET':
        try:
            pozprom_li = PozProm.objects.using(nskl).all()
            pozprom_serializer = PozPromSerializer(pozprom_li, many=True)
            odpowiedz = {
                'wiadomosc': "Sukces - Pobrano dane z poz_prom dla sklepu %s" % nskl,
                'pozprom': pozprom_serializer.data,
                'error':  ""
            }
            return JsonResponse(odpowiedz, status=status.HTTP_200_OK)
        except:
            error = {
                'wiadomosc': "Bład -> nie mogę odczytać poz_prom_lista",
                'pozprom': "[]",
                'error': ""
            }
            return JsonResponse(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#  -------------------------------------------------------------------------------------------------


@ csrf_exempt
@ api_view(['GET'])
def pozprom_detail(request, pk):
    try:
        pozprom = PozProm.objects.get(nr_prom=pk)
    except PozProm.DoesNotExist:
        exceptionError = {
            'wiadomosc': "Nie znaleziono pozprom 0 id =%s" % pk,
            'pozprom': "[]",
            'error': "Nie znaleziono - kod 404 error"
        }
        return JsonResponse(exceptionError, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        pozprom_serializer = PozPromSerializer(PozProm)
        odpowiedz = {
            'wiadomosc': "Odczyt pozprom o id = %s" % pk,
            'pozprom': [pozprom_serializer.data],
            'error': ""
        }
        return JsonResponse(odpowiedz, status=status.HTTP_200_OK)
